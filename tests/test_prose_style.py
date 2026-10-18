"""Prose-style contract for the catalogue's own skills and documents.

AGENTS.md asks for en-GB-oxendict prose without second-person address in the
catalogue-owned material. A review found six skills addressing the reader as
"you"; this test keeps the whole set clean. Imported skills keep their original
voice (ADR 0003) and the README is a welcome page, so both are exempt.
"""

from __future__ import annotations

import re
from pathlib import Path

from tests.catalogue import markdown_files, read, skills_root, strip_fences

IMPORTED_SKILLS = frozenset(
    {"biome-typescript", "effect-v4", "fast-check", "lemmascript", "zod4-typescript"}
)
SECOND_PERSON = re.compile(r"\b(?:you|your|yours|yourself|yourselves)\b", re.IGNORECASE)


def _catalogue_owned(repo_root: Path) -> list[Path]:
    skills = skills_root(repo_root).resolve()
    owned: list[Path] = []
    for path in markdown_files(repo_root):
        resolved = path.resolve()
        if resolved.name == "README.md" and resolved.parent == repo_root.resolve():
            continue
        if (
            skills in resolved.parents
            and resolved.relative_to(skills).parts[0] in IMPORTED_SKILLS
        ):
            continue
        owned.append(path)
    return owned


def test_catalogue_prose_does_not_address_the_reader(repo_root: Path) -> None:
    """Catalogue-owned skills and documents use neutral voice, never "you"."""
    offenders = [
        f"{path.relative_to(repo_root)}:{number}: {line.strip()}"
        for path in _catalogue_owned(repo_root)
        for number, line in enumerate(strip_fences(read(path)).splitlines(), start=1)
        if SECOND_PERSON.search(line)
    ]

    assert not offenders, f"second-person address in catalogue prose: {offenders}"
