"""Helpers shared by the catalogue contract tests.

The catalogue is Markdown, so every contract here is a small parser over a
convention the skills follow: frontmatter at the top of ``SKILL.md``, a
``## Route by question`` list in the router, pipe tables in the routing matrix
and the scenario document, and relative links between a skill and its
references. Keeping the parsers in one place means a convention changes in one
file and every test sees the same reading of it.
"""

from __future__ import annotations

import re
import typing as typ
from pathlib import Path

import yaml

if typ.TYPE_CHECKING:
    import collections.abc as cabc

ROUTER = "typescript-router"
"""The only skill that stays implicitly invocable."""

BACKTICKED = re.compile(r"`([^`\n]+)`")
RELATIVE_LINK = re.compile(r"\]\((?P<target>(?!https?://|mailto:|#)[^)\s]+)\)")
FENCE = re.compile(r"^(`{3,}|~{3,}).*?^\1", re.MULTILINE | re.DOTALL)


def skills_root(repo_root: Path) -> Path:
    """Return the directory holding every shipped skill."""
    return repo_root / "skills"


def skill_dirs(repo_root: Path) -> list[Path]:
    """Return every skill directory, sorted by name."""
    return sorted(p for p in skills_root(repo_root).iterdir() if p.is_dir())


def skill_names(repo_root: Path) -> frozenset[str]:
    """Return the name of every skill directory."""
    return frozenset(p.name for p in skill_dirs(repo_root))


def skill_file(repo_root: Path, skill: str) -> Path:
    """Return the path of a skill's ``SKILL.md``."""
    return skills_root(repo_root) / skill / "SKILL.md"


def read(path: Path) -> str:
    """Read a UTF-8 text file."""
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, object]:
    """Parse the YAML frontmatter block that opens a skill manifest.

    Parameters
    ----------
    text : str
        The full ``SKILL.md`` text.

    Returns
    -------
    dict of str to object
        The parsed mapping, with keys coerced to strings.

    Raises
    ------
    AssertionError
        When the document does not open with a fence, the fence is not
        closed, or the block is not a mapping.
    """
    lines = text.splitlines()
    assert lines and lines[0] == "---", (
        "manifest does not open with a frontmatter fence"
    )
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        msg = "frontmatter has no closing fence"
        raise AssertionError(msg) from error
    parsed = yaml.safe_load("\n".join(lines[1:closing]))
    assert isinstance(parsed, dict), "frontmatter is not a mapping"
    return {str(key): value for key, value in parsed.items()}


def section(text: str, heading: str) -> str:
    """Return the body of a level-two section, excluding later sections."""
    parts = text.split(f"\n## {heading}\n", 1)
    if len(parts) != 2:
        msg = f"section '## {heading}' not found"
        raise AssertionError(msg)
    return parts[1].split("\n## ", 1)[0]


def bullets(body: str) -> cabc.Iterator[str]:
    """Yield each top-level list item of a section with wrapped lines folded in."""
    current: list[str] = []
    for line in body.splitlines():
        if line.startswith("- "):
            if current:
                yield " ".join(current)
            current = [line[2:].strip()]
        elif current and line.startswith("  "):
            current.append(line.strip())
        else:
            if current:
                yield " ".join(current)
            current = []
    if current:
        yield " ".join(current)


def table_rows(text: str) -> list[list[str]]:
    """Return the cells of every body row of every pipe table in ``text``.

    Header rows are skipped by dropping the row that precedes each delimiter
    row, so callers see only data rows.
    """
    rows: list[list[str]] = []
    pending: list[str] | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            pending = None
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(set(cell) <= set("-: ") for cell in cells):
            pending = None  # the row before this delimiter was the header
            continue
        if pending is not None:
            rows.append(pending)
        pending = cells
    if pending is not None:
        rows.append(pending)
    return rows


def route_destinations(router_text: str) -> dict[str, frozenset[str]]:
    """Map each "Route by question" trigger to the skills it routes to.

    Every entry states its trigger, then a colon, then the destination. The
    destination may name several skills, so every backticked token after the
    final colon counts.
    """
    routes: dict[str, frozenset[str]] = {}
    for bullet in bullets(section(router_text, "Route by question")):
        trigger, _, destination = bullet.rpartition(":")
        routes[trigger.strip()] = frozenset(BACKTICKED.findall(destination))
    return routes


def strip_fences(text: str) -> str:
    """Remove fenced code blocks so links inside examples are not followed."""
    return FENCE.sub("", text)


def relative_links(text: str) -> list[str]:
    """Return the relative link targets in ``text``, ignoring fenced code.

    Anchors are stripped from each target, and URLs and in-page anchors are
    excluded.
    """
    return [
        match.group("target").split("#", 1)[0]
        for match in RELATIVE_LINK.finditer(strip_fences(text))
    ]


def markdown_files(repo_root: Path) -> list[Path]:
    """Return every Markdown file the documentation contracts check."""
    files = [
        path
        for root in (skills_root(repo_root), repo_root / "docs")
        for path in sorted(root.rglob("*.md"))
    ]
    files.extend(
        repo_root / name
        for name in ("README.md", "AGENTS.md", "CHANGELOG.md")
        if (repo_root / name).is_file()
    )
    return files
