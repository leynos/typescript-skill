#!/usr/bin/env python3
"""Check whether Effect 4 APIs exist in the installed packages.

Usage:
    has_export.py [--root DIR] Module.member [Module.member ...]
    has_export.py [--root DIR] Module            # list a module's exports

Examples:
    has_export.py Effect.catchAll Effect.catch Layer.scoped Schema.TaggedError
    has_export.py HttpClient.filterStatusOk NodeRuntime.runMain Flag.Int
    has_export.py Stream

For each query the script locates `<Module>.d.ts` under `node_modules/effect/dist`
(including area folders such as `http/`, `cli/`, `testing/`) and under every installed
`@effect/*` package, then reports the declaration line and its `@since` / `@stability`
JSDoc tags. When a member is missing it searches the bundled v3→v4 rename tables
(`references/renames/`) and prints any replacement guidance it finds.

Exit status: 0 when every queried member exists, 1 otherwise, 2 on usage errors.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent
RENAMES = SKILL_DIR / "references" / "renames"


def find_node_modules(start: pathlib.Path) -> pathlib.Path | None:
    for directory in [start, *start.parents]:
        candidate = directory / "node_modules" / "effect" / "package.json"
        if candidate.is_file():
            return directory / "node_modules"
    return None


def package_dists(node_modules: pathlib.Path) -> list[tuple[str, pathlib.Path]]:
    dists: list[tuple[str, pathlib.Path]] = [("effect", node_modules / "effect" / "dist")]
    scoped = node_modules / "@effect"
    if scoped.is_dir():
        for pkg in sorted(scoped.iterdir()):
            if (pkg / "dist").is_dir():
                dists.append((f"@effect/{pkg.name}", pkg / "dist"))
    return dists


def module_files(dists: list[tuple[str, pathlib.Path]], module: str) -> list[tuple[str, pathlib.Path]]:
    found = []
    for pkg, dist in dists:
        for path in dist.rglob(f"{module}.d.ts"):
            if "internal" in path.parts:
                continue
            rel = path.relative_to(dist).with_suffix("").with_suffix("")
            specifier = pkg if rel.as_posix() == module and pkg != "effect" else f"{pkg}/{rel.as_posix()}"
            found.append((specifier, path))
    return found


DECL = r"^export declare (?:const|function|class|let|enum|abstract class) {name}\b"
NAMESPACE = r"^export declare namespace {name}\b"
TYPE_DECL = r"^export (?:declare )?(?:interface|type) {name}\b"
STAR = r"^export \* as {name}\b"


def export_blocks(text: str) -> list[tuple[int, list[tuple[str, str]]]]:
    """Return (line index, [(local, exported)]) for every `export { ... }` block, comments stripped."""
    blocks = []
    # blank out comments first (keeping newlines) so `{@link …}` inside JSDoc cannot end a block early
    text = re.sub(r"/\*.*?\*/", lambda c: "\n" * c.group(0).count("\n"), text, flags=re.S)
    for m in re.finditer(r"^export \{(.*?)\}", text, re.M | re.S):
        body = re.sub(r"//[^\n]*", "", m.group(1))
        pairs = []
        for item in body.split(","):
            item = item.strip()
            if not item:
                continue
            item = re.sub(r"^type\s+", "", item)
            local, _, exported = item.partition(" as ")
            pairs.append((local.strip(), (exported or local).strip()))
        blocks.append((text.count("\n", 0, m.start()), pairs))
    return blocks


def find_member(text: str, member: str) -> int | None:
    lines = text.splitlines()
    for pattern in (DECL, TYPE_DECL, STAR, NAMESPACE):
        regex = re.compile(pattern.format(name=re.escape(member)))
        for i, line in enumerate(lines):
            if regex.search(line):
                return i
    for index, pairs in export_blocks(text):
        for local, exported in pairs:
            if exported == member:
                decl = re.compile(rf"^(?:export )?declare (?:const|function|class) {re.escape(local)}\b")
                for i, line in enumerate(lines):
                    if decl.search(line):
                        return i
                return index
    return None


def jsdoc_tags(lines: list[str], index: int) -> str:
    tags = []
    j = index - 1
    while j >= 0:
        stripped = lines[j].strip()
        if stripped.startswith("/**") or not (stripped.startswith("*") or stripped == "*/"):
            break
        for tag in ("@since", "@stability", "@deprecated"):
            if stripped.startswith(f"* {tag}"):
                tags.append(stripped[2:])
        j -= 1
    return ", ".join(reversed(tags))


def list_exports(text: str) -> list[str]:
    """List exported names using the same declaration forms `find_member` recognizes."""
    names = set(re.findall(r"^export declare (?:const|function|class|let|enum|abstract class) (\w+)", text, re.M))
    names.update(re.findall(r"^export declare namespace (\w+)", text, re.M))
    names.update(re.findall(r"^export (?:declare )?(?:interface|type) (\w+)", text, re.M))
    names.update(re.findall(r"^export \* as (\w+)", text, re.M))
    for _, pairs in export_blocks(text):
        names.update(exported for _, exported in pairs)
    return sorted(n for n in names if re.fullmatch(r"\w+", n))


def rename_entries(text: str) -> list[str]:
    """Return each `- ` list item of a rename table as one whitespace-normalized line.

    The tables are wrapped at 80 columns, so an item's replacement and guidance
    may continue on indented lines; those belong to the item above them.
    """
    entries: list[str] = []
    for line in text.splitlines():
        if line.startswith("- "):
            entries.append(line[2:].strip())
        elif entries and line.startswith("  ") and line.strip():
            entries[-1] = f"{entries[-1]} {line.strip()}"
        else:
            entries.append("")  # a blank or unrelated line ends the item
    return [entry for entry in entries if entry]


def rename_hints(query: str) -> list[str]:
    if not RENAMES.is_dir():
        return []
    needle = f"`{query}` ->"
    hits = []
    for path in sorted(RENAMES.glob("*.md")):
        for entry in rename_entries(path.read_text(encoding="utf-8")):
            if entry.startswith(needle):
                hits.append(f"{path.name}: {entry}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("queries", nargs="+")
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd(),
                        help="project directory (searched upwards for node_modules)")
    args = parser.parse_args()

    node_modules = find_node_modules(args.root.resolve())
    if node_modules is None:
        print("No node_modules/effect found from", args.root, "- falling back to rename tables only.")
    else:
        version = re.search(r'"version":\s*"([^"]+)"',
                            (node_modules / "effect" / "package.json").read_text(encoding="utf-8"))
        print(f"effect {version.group(1) if version else '?'} at {node_modules}")
    dists = package_dists(node_modules) if node_modules else []

    ok = True
    for query in args.queries:
        module, _, member = query.partition(".")
        files = module_files(dists, module) if dists else []
        if not member:
            if not files:
                print(f"\n{module}: no such module installed")
                ok = False
            for specifier, path in files:
                exports = list_exports(path.read_text(encoding="utf-8"))
                print(f"\n{module} ({specifier}): {len(exports)} exports\n  " + " ".join(exports))
            continue

        hit = False
        for specifier, path in files:
            text = path.read_text(encoding="utf-8")
            index = find_member(text, member)
            if index is not None:
                lines = text.splitlines()
                tags = jsdoc_tags(lines, index)
                decl = lines[index].strip()
                print(f"\nOK   {query}  [{specifier}]{'  ' + tags if tags else ''}\n     {decl[:200]}")
                hit = True
                break
        if not hit:
            ok = False
            where = ", ".join(s for s, _ in files) or "module not installed"
            print(f"\nMISS {query}  ({where})")
            hints = rename_hints(query)
            for h in hints[:5]:
                print(f"     hint {h[:400]}")
            if not hints:
                print("     no rename entry; list the module with: has_export.py", module)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
