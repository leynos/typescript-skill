"""The TypeScript example gate and the fixtures it compiles.

Positive examples show the shape a skill recommends; diagnostics fixtures prove
that a strictness switch or type-level contract fires. Both are compiled by
``make examples`` under the TypeScript release pinned in ``examples/package.json``.
These tests check the wiring the compiler cannot: that every fixture is linked
from the skill it claims to illustrate, that every diagnostics fixture asserts
at least one expected error, and that the gate reaches every file.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from tests.catalogue import read, relative_links, skill_dirs

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
LINKED_FROM = re.compile(
    r"^// Linked from (?P<skill>skills/[^/\s]+)/SKILL\.md\.", re.MULTILINE
)
EXPECT_ERROR = re.compile(r"^\s*// @ts-expect-error\b", re.MULTILINE)


def _fixtures(kind: str) -> list[Path]:
    return sorted((EXAMPLES / kind).glob("*.ts"))


@pytest.mark.parametrize(
    "fixture", _fixtures("positive") + _fixtures("diagnostics"), ids=str
)
def test_fixture_declares_and_is_linked_from_its_skill(
    repo_root: Path, fixture: Path
) -> None:
    """Each fixture names its skill in a header, and that skill links back."""
    match = LINKED_FROM.search(read(fixture))

    assert match, (
        f"{fixture.name} has no '// Linked from skills/<name>/SKILL.md.' header"
    )
    skill_md = repo_root / match.group("skill") / "SKILL.md"
    assert skill_md.is_file(), f"{fixture.name} names a skill that does not exist"
    targets = {(skill_md.parent / t).resolve() for t in relative_links(read(skill_md))}
    relative = fixture.relative_to(repo_root)
    assert fixture.resolve() in targets, (
        f"{match.group('skill')}/SKILL.md does not link to {relative}"
    )


@pytest.mark.parametrize("fixture", _fixtures("diagnostics"), ids=str)
def test_diagnostics_fixture_expects_at_least_one_error(fixture: Path) -> None:
    """A diagnostics fixture without an expected error proves nothing."""
    assert EXPECT_ERROR.search(read(fixture)), f"{fixture.name} has no @ts-expect-error"


@pytest.mark.parametrize("fixture", _fixtures("positive"), ids=str)
def test_positive_example_expects_no_error(fixture: Path) -> None:
    """A positive example that needs an expected error belongs in diagnostics."""
    assert not EXPECT_ERROR.search(read(fixture)), (
        f"{fixture.name} carries @ts-expect-error"
    )


def test_example_links_from_skills_point_at_real_files(repo_root: Path) -> None:
    """A skill that links to an example must link to one that exists."""
    broken = [
        f"{skill_dir.name} -> {target}"
        for skill_dir in skill_dirs(repo_root)
        for target in relative_links(read(skill_dir / "SKILL.md"))
        if "examples/" in target and not (skill_dir / target).resolve().is_file()
    ]

    assert not broken, f"skills link to missing examples: {broken}"


def test_tsconfig_includes_both_fixture_directories() -> None:
    """The gate must reach every fixture, or a broken one passes unnoticed."""
    raw = read(EXAMPLES / "tsconfig.json")
    without_comments = re.sub(r"^\s*//.*$", "", raw, flags=re.MULTILINE)
    config = json.loads(without_comments)

    assert "positive/**/*.ts" in config["include"], "the gate skips positive fixtures"
    assert "diagnostics/**/*.ts" in config["include"], (
        "the gate skips diagnostics fixtures"
    )
    assert config["compilerOptions"]["noEmit"] is True, "the gate must not emit output"


def test_examples_pin_an_exact_typescript_release() -> None:
    """The gate's evidence is only as good as the compiler it names."""
    package = json.loads(read(EXAMPLES / "package.json"))
    version = package["devDependencies"]["typescript"]

    assert re.fullmatch(r"\d+\.\d+\.\d+", version), (
        f"typescript is not pinned exactly: {version}"
    )
    assert version.startswith("7."), "the example gate must run the TypeScript 7 line"
