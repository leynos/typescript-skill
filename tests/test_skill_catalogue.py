"""Contract tests binding the router's routing table to the skills on disk.

The router is the catalogue's entry point: if it names a skill that does not
exist, the route dead-ends, and if a skill exists that no route reaches, it is
unreachable. Neither failure is visible from reading either file alone.

Only positive route declarations count as references: the destination of a
"Route by question" entry, or a cell in the routing matrix's skill columns.
Prose elsewhere mentions skills without routing to them, so counting it would
let a skill look reachable when nothing actually routes there.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tests.catalogue import (
    BACKTICKED,
    ROUTER,
    bullets,
    frontmatter,
    read,
    route_destinations,
    section,
    skill_dirs,
    skill_file,
    skill_names,
    table_rows,
)

# First-class skills carry judgement and stay short; comparison tables and
# worked examples live in references. Imported deep dives are procedural and
# carry larger envelopes, as does the router, which must name every skill and
# carry the testing hierarchy. Both are recorded here and in
# docs/skill-catalogue-status.md.
SKILL_LINE_BUDGET = 160
DEEP_DIVE_LINE_ENVELOPES: dict[str, int] = {
    "effect-v4": 260,
    "typescript-router": 200,
    "fast-check": 230,
    "lemmascript": 230,
    "zod4-typescript": 540,
}

# Each imported deep dive has exactly one owner inside the catalogue: the
# skill whose decision surface decides when the deep dive is worth loading.
# The owner must link to it, so the route into the deep dive is unambiguous.
DEEP_DIVE_OWNERS: dict[str, str] = {
    "effect-v4": "typescript-errors-and-outcomes",
    "fast-check": "typescript-verification",
    "lemmascript": "typescript-verification",
    "zod4-typescript": "typescript-boundaries-and-validation",
}

ALLOWED_FRONTMATTER_KEYS = frozenset(
    {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
)


def _matrix(repo_root: Path) -> str:
    return read(repo_root / "skills" / ROUTER / "references" / "routing-matrix.md")


def _matrix_destinations(matrix: str) -> set[str]:
    """Extract skill names from the routing matrix's two skill columns."""
    names: set[str] = set()
    for row in table_rows(matrix):
        for cell in row[1:3]:
            names.update(BACKTICKED.findall(cell))
    return names


@pytest.fixture(scope="session")
def names(repo_root: Path) -> frozenset[str]:
    """Return every skill directory name under ``skills/``."""
    return skill_names(repo_root)


@pytest.fixture(scope="session")
def routed(repo_root: Path) -> frozenset[str]:
    """Return every skill the router positively routes to."""
    router = read(skill_file(repo_root, ROUTER))
    destinations: set[str] = set()
    for targets in route_destinations(router).values():
        destinations.update(targets)
    return frozenset(destinations | _matrix_destinations(_matrix(repo_root)))


def test_every_skill_directory_has_a_skill_file(repo_root: Path) -> None:
    """A directory under skills/ without a SKILL.md is not a loadable skill."""
    missing = [p.name for p in skill_dirs(repo_root) if not (p / "SKILL.md").is_file()]

    assert not missing, f"skill directories without SKILL.md: {missing}"


def test_frontmatter_name_matches_directory(repo_root: Path) -> None:
    """The frontmatter name is how a skill is invoked; it must match its path."""
    mismatched = {
        path.name: frontmatter(read(path / "SKILL.md")).get("name")
        for path in skill_dirs(repo_root)
        if frontmatter(read(path / "SKILL.md")).get("name") != path.name
    }

    assert not mismatched, f"frontmatter name != directory name: {mismatched}"


def test_frontmatter_uses_only_schema_keys(repo_root: Path) -> None:
    """Anything beyond the Agent Skills schema belongs under ``metadata``."""
    offenders = {
        path.name: sorted(
            set(frontmatter(read(path / "SKILL.md"))) - ALLOWED_FRONTMATTER_KEYS
        )
        for path in skill_dirs(repo_root)
        if set(frontmatter(read(path / "SKILL.md"))) - ALLOWED_FRONTMATTER_KEYS
    }

    assert not offenders, f"frontmatter keys outside the schema: {offenders}"


def test_metadata_is_a_string_mapping_with_globs(repo_root: Path) -> None:
    """``skills-ref`` coerces non-string metadata, so reject it here."""
    problems: dict[str, str] = {}
    for path in skill_dirs(repo_root):
        metadata = frontmatter(read(path / "SKILL.md")).get("metadata")
        if not isinstance(metadata, dict):
            problems[path.name] = "metadata is not a mapping"
            continue
        if any(not isinstance(value, str) for value in metadata.values()):
            problems[path.name] = "metadata carries a non-string value"
        elif not str(metadata.get("globs", "")).strip():
            problems[path.name] = "metadata lacks a globs hint"

    assert not problems, f"metadata problems: {problems}"


def test_description_is_within_discovery_budget(repo_root: Path) -> None:
    """Descriptions drive discovery; keep them usable and inside the schema cap."""
    problems: dict[str, int] = {}
    for path in skill_dirs(repo_root):
        description = frontmatter(read(path / "SKILL.md")).get("description")
        length = len(description) if isinstance(description, str) else 0
        if not 20 <= length <= 1024:
            problems[path.name] = length

    assert not problems, f"description length outside 20..1024: {problems}"


def test_skill_files_stay_inside_their_line_budget(repo_root: Path) -> None:
    """Judgement stays short; long material moves to references."""
    over: dict[str, tuple[int, int]] = {}
    for path in skill_dirs(repo_root):
        budget = DEEP_DIVE_LINE_ENVELOPES.get(path.name, SKILL_LINE_BUDGET)
        lines = len(read(path / "SKILL.md").splitlines())
        if lines > budget:
            over[path.name] = (lines, budget)

    assert not over, f"SKILL.md over budget (lines, budget): {over}"


def test_deep_dive_envelopes_name_real_skills(names: frozenset[str]) -> None:
    """An envelope for a renamed or removed skill would silently stop applying."""
    stale = sorted(set(DEEP_DIVE_LINE_ENVELOPES) - names)

    assert not stale, f"line envelopes for skills that do not exist: {stale}"


def test_routes_resolve_to_real_skills(
    routed: frozenset[str], names: frozenset[str]
) -> None:
    """Every route destination must exist on disk."""
    broken = sorted(routed - names)

    assert not broken, f"routes point at non-existent skills: {broken}"


def test_every_skill_is_routed_to(
    routed: frozenset[str], names: frozenset[str]
) -> None:
    """A skill no route reaches cannot be selected by the router."""
    unrouted = sorted(names - routed - {ROUTER})

    assert not unrouted, f"skills nothing routes to: {unrouted}"


def test_deep_dives_are_routed_to(routed: frozenset[str]) -> None:
    """Guard the parser itself.

    The deep dives are reached through entries that trail a semicolon rather
    than a colon. If the parser regresses to taking one token per entry they
    vanish silently, and every other assertion here still passes.
    """
    missing = sorted(set(DEEP_DIVE_OWNERS) - routed)

    assert not missing, f"deep dives no route reaches: {missing}"


@pytest.mark.parametrize(("deep_dive", "owner"), sorted(DEEP_DIVE_OWNERS.items()))
def test_each_deep_dive_has_one_owner_that_links_to_it(
    repo_root: Path, deep_dive: str, owner: str
) -> None:
    """The owning selector links to its deep dive, so ownership is explicit."""
    owner_text = read(skill_file(repo_root, owner))

    assert f"../{deep_dive}/SKILL.md" in owner_text, (
        f"{owner} does not link to ../{deep_dive}/SKILL.md"
    )


def test_deep_dive_owners_exist(names: frozenset[str]) -> None:
    """Both sides of the ownership table must be shipped skills."""
    stale = sorted((set(DEEP_DIVE_OWNERS) | set(DEEP_DIVE_OWNERS.values())) - names)

    assert not stale, f"ownership table names unknown skills: {stale}"


def test_routing_matrix_rows_have_three_cells(repo_root: Path) -> None:
    """Symptom, primary, companion. A fourth column would hide a skill name."""
    short = [row for row in table_rows(_matrix(repo_root)) if len(row) != 3]

    assert not short, f"routing matrix rows without exactly three cells: {short}"


def test_routing_matrix_companion_is_a_skill_or_none(
    repo_root: Path, names: frozenset[str]
) -> None:
    """The companion cell names one skill or the literal ``None``."""
    bad: list[list[str]] = []
    for row in table_rows(_matrix(repo_root)):
        companion = row[2]
        if companion == "None":
            continue
        found = BACKTICKED.findall(companion)
        if len(found) != 1 or found[0] not in names:
            bad.append(row)

    assert not bad, f"companion cells that are neither a skill nor None: {bad}"


def test_catalogue_status_lists_every_skill(
    repo_root: Path, names: frozenset[str]
) -> None:
    """The catalogue status doc is the inventory; it must not drift."""
    status = read(repo_root / "docs" / "skill-catalogue-status.md")
    listed = {
        entry[0]
        for bullet in bullets(section(status, "Active skills"))
        if (entry := BACKTICKED.findall(bullet))
    }
    missing = sorted(names - listed)
    extra = sorted(listed - names)

    assert not missing, f"skills absent from skill-catalogue-status.md: {missing}"
    assert not extra, f"skill-catalogue-status.md lists unknown skills: {extra}"


def test_catalogue_status_records_the_deep_dive_envelopes(repo_root: Path) -> None:
    """The envelope table in the test is mirrored in prose so readers see it."""
    status = read(repo_root / "docs" / "skill-catalogue-status.md")
    unmentioned = [
        skill
        for skill, budget in DEEP_DIVE_LINE_ENVELOPES.items()
        if f"`{skill}`" not in status or str(budget) not in status
    ]

    assert not unmentioned, f"status doc omits envelope for: {unmentioned}"
