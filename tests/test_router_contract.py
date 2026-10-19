"""Pin the router's shape and the ownership boundaries it must state.

Reachability alone cannot catch a reassigned route: another entry would still
name the skill. These tests pin the entries and matrix rows that carry a design
decision, so moving a boundary is a deliberate edit here as well as there.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from tests.catalogue import (
    ROUTER,
    read,
    route_destinations,
    section,
    skill_file,
    table_rows,
)

# The four questions the router opens with. Routing is by pressure, not by
# brand, so the questions ask where code runs, what role it plays, which
# quality is unhealthy, and which boundary owns lifecycle.
OPENING_QUESTIONS = (
    "Where does this code execute",
    "Is this source application code, a public package",
    "Is the problem about correctness, responsiveness, throughput",
    "Which boundary owns cancellation, failure, validation, and shutdown",
)

# Routing entries whose destination is a design decision.
PINNED_ROUTES: dict[str, frozenset[str]] = {
    (
        "Choosing between ordinary tests, compile-time type tests, properties, "
        "stateful or race exploration, mutation testing, and proof"
    ): frozenset({"typescript-verification", "fast-check", "lemmascript"}),
    (
        "Upgrading from TypeScript 6 to 7, removed options, side-by-side "
        "checking, compiler-output comparison, or a tool that still needs the "
        "6.0 programmatic API"
    ): frozenset({"typescript-7-transition"}),
}

# Routing matrix rows that pin an ownership boundary.
PINNED_ROWS: dict[str, tuple[str, str]] = {
    "Style toggles should become CSS state": (
        "`typescript-quality-tools`",
        "`browser-main-thread-performance`",
    ),
    "Invariant must hold for every input, not sampled ones": (
        "`typescript-verification`",
        "`lemmascript`",
    ),
    "Case table keeps growing to sample one invariant": (
        "`fast-check`",
        "`typescript-testing`",
    ),
    "Renderer needs a privileged operation": (
        "`electron-and-ipc`",
        "`typescript-boundaries-and-validation`",
    ),
    "`tsc` from TypeScript 7 rejects an option TypeScript 6 accepted": (
        "`typescript-7-transition`",
        "None",
    ),
}


@pytest.fixture(scope="module")
def router(repo_root: Path) -> str:
    """Return the router's SKILL.md text."""
    return read(skill_file(repo_root, ROUTER))


@pytest.fixture(scope="module")
def matrix(repo_root: Path) -> dict[str, tuple[str, ...]]:
    """Map each routing-matrix symptom to its primary skill and companion."""
    text = read(repo_root / "skills" / ROUTER / "references" / "routing-matrix.md")
    return {row[0]: tuple(row[1:3]) for row in table_rows(text)}


def test_router_opens_with_the_four_questions(router: str) -> None:
    """The opening questions are the routing method; they must stay present."""
    body = section(router, "Opening questions")
    numbered = re.findall(r"^\d+\. ", body, re.MULTILINE)
    missing = [q for q in OPENING_QUESTIONS if q not in body]

    assert len(numbered) == 4, (
        f"expected four numbered questions, found {len(numbered)}"
    )
    assert not missing, f"opening questions missing: {missing}"


@pytest.mark.parametrize(("trigger", "destination"), sorted(PINNED_ROUTES.items()))
def test_pinned_routes_keep_their_destination(
    router: str, trigger: str, destination: frozenset[str]
) -> None:
    """Each pinned trigger routes to exactly the skills the design chose."""
    routes = route_destinations(router)

    assert routes.get(trigger) == destination, (
        f"{trigger!r} routes to {routes.get(trigger)}, expected {destination}"
    )


@pytest.mark.parametrize(("symptom", "expected"), sorted(PINNED_ROWS.items()))
def test_pinned_matrix_rows_keep_their_owner(
    matrix: dict[str, tuple[str, ...]], symptom: str, expected: tuple[str, str]
) -> None:
    """Each pinned row names the primary skill and companion the design chose."""
    assert matrix.get(symptom) == expected, (
        f"{symptom!r} is {matrix.get(symptom)}, expected {expected}"
    )


def test_router_states_the_smallest_pair_rule(router: str) -> None:
    """One language skill plus at most one companion is the loading rule."""
    stance = section(router, "Working stance")

    assert "at most one" in stance, "the router no longer states the pairing cap"


def test_router_separates_runtime_from_static_semantics(router: str) -> None:
    """JavaScript files trigger runtime guidance; type material stays with TS."""
    assert "**/*.js" in router or "**/*.mjs" in router, (
        "the router's globs no longer include JavaScript files"
    )
    assert "Types disappear at runtime" in router, (
        "the router no longer separates runtime and static semantics"
    )
