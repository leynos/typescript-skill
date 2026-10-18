"""Behavioural tests for the Effect skill's `has_export.py` rename-hint lookup.

The rename tables are wrapped at 80 columns, so a row's replacement and
guidance can continue on indented lines. A review of the catalogue found that
the lookup returned only the first physical line, which for wrapped rows
contained neither a replacement nor import guidance. These tests pin the whole
item being returned.
"""

from __future__ import annotations

import importlib.util
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
    assert spec is not None and spec.loader is not None
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
    assert hint.endswith("import it directly. The API is unchanged in fast-check v4.")
    assert "\n" not in hint


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
