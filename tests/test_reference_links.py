"""Every relative link resolves and every reference document is reachable.

A reference nobody links to is dead weight an agent will never load, and a
link to a moved reference is a route that dead-ends mid-task. Both are only
visible by walking the tree.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tests.catalogue import (
    BACKTICKED,
    markdown_files,
    read,
    relative_links,
    skill_dirs,
    skills_root,
    strip_fences,
)

# Directories of many small files that a skill grep rather than reads. Naming
# the directory from the skill counts as linking every file inside it.
GREPPED_DIRECTORIES = ("references/renames/", "references/upstream/")


def _resolve(source: Path, target: str) -> Path:
    return (source.parent / target).resolve()


def _is_verbatim_upstream(path: Path) -> bool:
    """Say whether a file is a verbatim upstream copy the catalogue never edits.

    Such copies may link to files that were not copied; fixing those links
    would mean editing the copy, which ADR 0003 rules out.
    """
    return "references/upstream/" in path.as_posix()


def test_every_relative_link_resolves(repo_root: Path) -> None:
    """Relative links in skills, docs, and the root documents must exist."""
    broken = [
        f"{path.relative_to(repo_root)} -> {target}"
        for path in markdown_files(repo_root)
        if not _is_verbatim_upstream(path)
        for target in relative_links(read(path))
        if not _resolve(path, target).exists()
    ]

    assert not broken, f"broken relative links: {broken}"


@pytest.mark.parametrize(
    "skill_dir",
    [
        p
        for p in skill_dirs(Path(__file__).resolve().parents[1])
        if (p / "references").is_dir()
    ],
    ids=lambda p: str(p.name),
)
def test_every_reference_document_is_linked_from_its_skill(skill_dir: Path) -> None:
    """A reference exists to be loaded; something in the skill must point at it."""
    docs = sorted(skill_dir.rglob("*.md"))
    linked: set[Path] = set()
    mentioned_dirs: set[Path] = set()
    for doc in docs:
        text = read(doc)
        linked.update(_resolve(doc, target) for target in relative_links(text))
        for token in BACKTICKED.findall(strip_fences(text)):
            # A backticked `references/<file>.md` is a pointer too: imported
            # skills name their references in a table rather than linking.
            if token.startswith("references/") and token.endswith(".md"):
                linked.add((skill_dir / token).resolve())
            for directory in GREPPED_DIRECTORIES:
                if token.startswith(directory):
                    mentioned_dirs.add((skill_dir / directory).resolve())

    def reachable(reference: Path) -> bool:
        if reference.resolve() in linked:
            return True
        return any(parent in mentioned_dirs for parent in reference.resolve().parents)

    orphans = [
        str(doc.relative_to(skill_dir))
        for doc in sorted((skill_dir / "references").rglob("*.md"))
        if not reachable(doc)
    ]

    assert not orphans, f"{skill_dir.name} has unlinked references: {orphans}"


# Links that leave `skills/` are evidence pointers into the repository. The
# users' guide documents that a copied installation lacks exactly these two
# directories, so the set must not grow silently.
EVIDENCE_DIRECTORIES = ("examples", "docs")


def test_links_out_of_skills_point_only_at_evidence_directories(
    repo_root: Path,
) -> None:
    """A skill may link upward only into the documented evidence directories."""
    skills = skills_root(repo_root).resolve()
    offenders = [
        f"{path.relative_to(repo_root)} -> {target}"
        for path in markdown_files(repo_root)
        if skills in path.resolve().parents and not _is_verbatim_upstream(path)
        for target in relative_links(read(path))
        if skills not in _resolve(path, target).parents
        and _resolve(path, target).relative_to(repo_root).parts[0]
        not in EVIDENCE_DIRECTORIES
    ]

    assert not offenders, f"skills link outside the evidence directories: {offenders}"


def test_grepped_directories_are_named_only_where_they_exist(repo_root: Path) -> None:
    """The directory allowance is not a loophole: it applies to real directories."""
    offenders: list[str] = []
    for skill_dir in skill_dirs(repo_root):
        text = read(skill_dir / "SKILL.md")
        for token in BACKTICKED.findall(strip_fences(text)):
            for directory in GREPPED_DIRECTORIES:
                if token.startswith(directory) and not (skill_dir / directory).is_dir():
                    offenders.append(f"{skill_dir.name}: {token}")

    assert not offenders, (
        f"skills name grepped directories they do not ship: {offenders}"
    )
