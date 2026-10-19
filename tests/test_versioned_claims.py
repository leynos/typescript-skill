"""Compiler-version claims live in versioned material, not evergreen skills.

The transition from TypeScript 6 to 7 is a moving fault line: option removals,
the missing programmatic API, and tool compatibility gaps will all change. The
catalogue keeps that material in one review-dated skill so the evergreen
skills do not quietly rot. This test makes the boundary executable.
"""

from __future__ import annotations

import re
from pathlib import Path

from tests.catalogue import ROUTER, read, skill_dirs

VERSIONED_SKILL = "typescript-7-transition"

# Where compiler-version claims are allowed: the versioned skill itself, the
# router (which must name the trigger), the imported Effect skill (which pins
# its own TypeScript floor), and the Biome skill (whose rule tables cite the
# TypeScript release they were checked against).
ALLOWED = frozenset({VERSIONED_SKILL, ROUTER, "effect-v4", "biome-typescript"})

VERSION_CLAIM = re.compile(
    r"\btsgo\b|native-preview|@typescript/typescript6|\btsc6\b"
    r"|\b(?:TypeScript|TS) [5-7](?:\.\d+)?\b|typescript@[5-7]"
)


def test_version_claims_stay_in_versioned_material(repo_root: Path) -> None:
    """Evergreen skills must not pin compiler versions or transition tooling."""
    leaks: list[str] = []
    for skill_dir in skill_dirs(repo_root):
        if skill_dir.name in ALLOWED:
            continue
        for path in sorted(skill_dir.rglob("*.md")):
            for number, line in enumerate(read(path).splitlines(), start=1):
                if VERSION_CLAIM.search(line):
                    leaks.append(
                        f"{path.relative_to(repo_root)}:{number}: {line.strip()}"
                    )

    assert not leaks, (
        "compiler-version claims outside versioned material:\n" + "\n".join(leaks)
    )


def test_versioned_skill_states_its_review_date(repo_root: Path) -> None:
    """A version-pinned skill names the release and the date it was checked."""
    text = read(repo_root / "skills" / VERSIONED_SKILL / "SKILL.md")

    assert re.search(r"\b7\.0\.\d+\b", text), (
        "the transition skill names no 7.0.x release"
    )
    assert re.search(r"\b2026-\d{2}-\d{2}\b", text), (
        "the transition skill carries no review date"
    )
