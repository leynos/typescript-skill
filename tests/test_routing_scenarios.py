"""The routing scenarios name real skills and keep the design's answers.

``docs/routing-scenarios.md`` is the router's evaluation set: each row is a
request drawn from the estate, the primary skill it should load, and the
companion. The rows that shaped the catalogue's boundaries are pinned here, so
a boundary moves on purpose or not at all.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tests.catalogue import BACKTICKED, read, skill_names, table_rows

# Scenario fragment -> (primary, companion). These are the six scenarios the
# design document used to justify the catalogue's shape.
PINNED_SCENARIOS: dict[str, tuple[str, str]] = {
    "Parsing a large GeoJSON payload freezes Wildside": (
        "browser-main-thread-performance",
        "typescript-async-and-concurrency",
    ),
    "Make Simulacat's ESM/CJS exports pass consumer checks": (
        "typescript-modules-and-packaging",
        "arch-typescript-package-design",
    ),
    "Prove DigitalPuddle never applies a transition before its virtual timestamp": (
        "typescript-verification",
        "fast-check",
    ),
    "Add a privileged Velocetty command": (
        "electron-and-ipc",
        "typescript-boundaries-and-validation",
    ),
    "Introduce exact optional properties into Velocetty": (
        "typescript-types-and-apis",
        "None",
    ),
    "Prevent direct style toggles in Wildside": (
        "typescript-quality-tools",
        "browser-main-thread-performance",
    ),
}


@pytest.fixture(scope="module")
def scenarios(repo_root: Path) -> list[list[str]]:
    """Return the body rows of every table in the scenarios document."""
    return table_rows(read(repo_root / "docs" / "routing-scenarios.md"))


def test_scenarios_exist(scenarios: list[list[str]]) -> None:
    """An empty evaluation set would make every other test here vacuous."""
    assert len(scenarios) >= len(PINNED_SCENARIOS)


def test_scenario_rows_name_real_skills(
    repo_root: Path, scenarios: list[list[str]]
) -> None:
    """Primary and companion cells name shipped skills or the literal None."""
    names = skill_names(repo_root)
    bad: list[str] = []
    for row in scenarios:
        assert len(row) >= 3, f"scenario row needs scenario, primary, companion: {row}"
        primary = BACKTICKED.findall(row[1])
        if len(primary) != 1 or primary[0] not in names:
            bad.append(f"primary of {row[0]!r}: {row[1]}")
        if row[2] != "None":
            companion = BACKTICKED.findall(row[2])
            if len(companion) != 1 or companion[0] not in names:
                bad.append(f"companion of {row[0]!r}: {row[2]}")

    assert not bad, f"scenario cells that are not a single real skill: {bad}"


@pytest.mark.parametrize(("fragment", "expected"), sorted(PINNED_SCENARIOS.items()))
def test_pinned_scenarios_keep_their_route(
    scenarios: list[list[str]], fragment: str, expected: tuple[str, str]
) -> None:
    """The design's scenarios route where the design said they should."""
    matches = [row for row in scenarios if fragment in row[0]]

    assert len(matches) == 1, f"expected one scenario containing {fragment!r}"
    primary = BACKTICKED.findall(matches[0][1])
    companion = (
        matches[0][2]
        if matches[0][2] == "None"
        else BACKTICKED.findall(matches[0][2])[0]
    )

    assert (primary[0], companion) == expected
