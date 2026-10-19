"""Prose-style contract for the catalogue's own skills and documents.

AGENTS.md asks for en-GB-oxendict prose without first- or second-person
address in the catalogue-owned material. A review found six skills addressing
the reader as "you" and one scenario asking what "we" need; this test keeps the
whole set clean. The first-person singular pronoun is left out of the pattern
because "I" also names `I/O` and loop variables in prose. Imported skills keep
their original voice (ADR 0003) and the README is a welcome page, so both are
exempt.
"""

from __future__ import annotations

import re
from pathlib import Path

from tests.catalogue import markdown_files, read, skills_root, strip_fences

IMPORTED_SKILLS = frozenset(
    {"biome-typescript", "effect-v4", "fast-check", "lemmascript", "zod4-typescript"}
)
PERSONAL_ADDRESS = re.compile(
    r"\b(?:you|your|yours|yourself|yourselves|we|us|our|ours|ourselves)\b",
    re.IGNORECASE,
)
INLINE_CODE = re.compile(r"`[^`]*`")


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
    """Catalogue-owned skills and documents use neutral voice, never "you" or "we"."""
    offenders = [
        f"{path.relative_to(repo_root)}:{number}: {line.strip()}"
        for path in _catalogue_owned(repo_root)
        for number, line in enumerate(strip_fences(read(path)).splitlines(), start=1)
        if PERSONAL_ADDRESS.search(INLINE_CODE.sub("", line))
    ]

    assert not offenders, f"personal address in catalogue prose: {offenders}"
