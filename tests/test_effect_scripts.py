"""Behavioural tests for the Effect skill's helper scripts.

The rename tables are wrapped at 80 columns, so a row's replacement and
guidance can continue on indented lines. A review of the catalogue found that
the lookup returned only the first physical line, which for wrapped rows
contained neither a replacement nor import guidance. These tests pin the whole
item being returned.
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from types import ModuleType

import pytest

SCRIPT = Path("skills/effect-v4/scripts/has_export.py")

TABLE = """\
<!-- Generated; wrapped at 80 columns. -->
# `effect/FastCheck` v3 → v4

- `FastCheck.AsyncPropertyHookFunction` ->
  `FastCheck.AsyncPropertyHookFunction`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.array` -> `FastCheck.array`: Depend on fast-check and import it
  directly. The API is unchanged in fast-check v4.
- `FastCheck.assert` -> `FastCheck.assert`: One line only.

Prose after a blank line is not part of any item.
"""


def _load(repo_root: Path, renames: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("has_export", repo_root / SCRIPT)
    assert spec is not None and spec.loader is not None, f"cannot load {SCRIPT}"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    setattr(module, "RENAMES", renames)  # noqa: B010 - dynamically loaded module
    return module


@pytest.fixture
def rename_hints(repo_root: Path, tmp_path: Path) -> Callable[[str], list[str]]:
    """Return the script's lookup bound to a two-row fixture table."""
    renames = tmp_path / "renames"
    renames.mkdir()
    (renames / "effect-FastCheck.md").write_text(TABLE, encoding="utf-8")
    hints: Callable[[str], list[str]] = _load(repo_root, renames).rename_hints
    return hints


def test_replacement_on_the_next_line_is_returned(
    rename_hints: Callable[[str], list[str]],
) -> None:
    """A row whose replacement starts on a continuation line is complete."""
    assert rename_hints("FastCheck.AsyncPropertyHookFunction") == [
        "effect-FastCheck.md: `FastCheck.AsyncPropertyHookFunction` -> "
        "`FastCheck.AsyncPropertyHookFunction`: Depend on fast-check and import "
        "it directly. The API is unchanged in fast-check v4."
    ]


def test_guidance_spanning_lines_is_joined(
    rename_hints: Callable[[str], list[str]],
) -> None:
    """Wrapped guidance is returned as one normalized line."""
    (hint,) = rename_hints("FastCheck.array")
    assert hint.endswith(
        "import it directly. The API is unchanged in fast-check v4."
    ), f"guidance was not joined: {hint!r}"
    assert "\n" not in hint, f"hint spans lines: {hint!r}"


def test_adjacent_items_do_not_leak(rename_hints: Callable[[str], list[str]]) -> None:
    """Continuation text belongs to the item above it, never the next one."""
    assert rename_hints("FastCheck.assert") == [
        "effect-FastCheck.md: `FastCheck.assert` -> `FastCheck.assert`: One line only."
    ]


def test_unknown_query_has_no_entry(rename_hints: Callable[[str], list[str]]) -> None:
    """An unknown symbol still reports no entry."""
    assert rename_hints("FastCheck.missing") == []


def test_every_shipped_row_yields_a_replacement(repo_root: Path) -> None:
    """Every `->` row in the shipped tables returns a hint naming a replacement."""
    renames = repo_root / "skills/effect-v4/references/renames"
    module = _load(repo_root, renames)
    entries: Callable[[str], list[str]] = module.rename_entries
    incomplete = [
        f"{path.name}: {entry[:60]}"
        for path in sorted(renames.glob("effect-*.md"))
        for entry in entries(path.read_text(encoding="utf-8"))
        if "` -> " in entry and "`:" not in entry.split(" -> ", 1)[1]
    ]
    assert not incomplete, f"rows without a replacement and reason: {incomplete}"


def _run(
    repo_root: Path, script: str, *arguments: str
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-I", str(repo_root / script), *arguments],
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )


def test_pattern_scanner_reports_v3_calls_and_spares_v4_forms(
    repo_root: Path, tmp_path: Path
) -> None:
    """`check_v3_patterns.py` flags removed calls without false positives."""
    source = tmp_path / "sample.ts"
    source.write_text(
        'const a = Schema.Literal("a", "b");\n'  # v3: variadic literals
        'const b = Schema.Literal("a,b");\n'  # one literal containing a comma
        "const c = Schema.decode({ decode, encode });\n"  # v4 operation form
        "const d = Schema.decodeUnknown(schema);\n"  # v3 decoder
        'const e = Schema.Literal("a\\"b", "c");\n'  # escaped quote, two args
        "const f = Schema.Literal('a\\'b', 'c');\n"  # same with single quotes
        'const g = Schema.Literal("a\\"b");\n',  # escaped quote, one arg
        encoding="utf-8",
    )
    result = _run(
        repo_root, "skills/effect-v4/scripts/check_v3_patterns.py", str(source)
    )

    assert result.returncode == 1, result.stdout + result.stderr
    reported = {int(line) for line in re.findall(r"sample\.ts:(\d+):", result.stdout)}
    assert reported == {1, 4, 5, 6}, f"reported lines {reported}: {result.stdout}"


def test_export_check_lists_types_and_reports_members(
    repo_root: Path, tmp_path: Path
) -> None:
    """`has_export.py` lists declared types and finds or misses members."""
    dist = tmp_path / "node_modules" / "effect" / "dist"
    dist.mkdir(parents=True)
    (dist.parent / "package.json").write_text('{"version": "4.0.5"}', encoding="utf-8")
    (dist / "Widget.d.ts").write_text(
        "export declare const make: () => Widget;\n"
        "export interface Widget { readonly id: string }\n"
        "export type WidgetId = string;\n"
        "export declare namespace Widget { interface Options {} }\n",
        encoding="utf-8",
    )
    script = "skills/effect-v4/scripts/has_export.py"

    listing = _run(repo_root, script, "--root", str(tmp_path), "Widget")
    assert listing.returncode == 0, listing.stdout + listing.stderr
    assert "Widget (effect/Widget): 3 exports" in listing.stdout, listing.stdout
    assert "WidgetId" in listing.stdout and "make" in listing.stdout, listing.stdout

    members = _run(
        repo_root, script, "--root", str(tmp_path), "Widget.make", "Widget.gone"
    )
    assert members.returncode == 1, members.stdout + members.stderr
    assert "OK   Widget.make" in members.stdout, members.stdout
    assert "MISS Widget.gone" in members.stdout, members.stdout
