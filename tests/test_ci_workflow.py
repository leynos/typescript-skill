"""Contract tests keeping the hosted Tests workflow aligned with ``make check``.

The first hosted run of the workflow failed because ``make check-fmt`` reached
``markdownlint-cli2`` and the job had never installed it. The job now runs the
same gates as a local ``make check`` and installs every external tool those
gates call. These tests read the workflow and the Makefile so the two cannot
drift apart silently again.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pytest
import yaml

WORKFLOW = Path(".github/workflows/tests.yml")

# External commands the Makefile gates call, mapped to the text that the
# installing workflow step must contain.
EXTERNAL_TOOLS: dict[str, str] = {
    "markdownlint-cli2": "markdownlint-cli2@",
    "nixie": "install-nixie@",
    "mdtablefix": "install-mdtablefix@",
    "bun": "setup-bun@",
    "uv": "setup-uv@",
}


def _workflow_steps(repo_root: Path) -> list[dict[str, Any]]:
    document = yaml.safe_load((repo_root / WORKFLOW).read_text(encoding="utf-8"))
    jobs = document["jobs"]
    assert list(jobs) == ["tests"], "the workflow has one job named tests"
    steps = jobs["tests"]["steps"]
    assert isinstance(steps, list)
    return [step for step in steps if isinstance(step, dict)]


def _make_targets(steps: list[dict[str, Any]]) -> list[str]:
    targets: list[str] = []
    for step in steps:
        run = step.get("run")
        if isinstance(run, str):
            targets.extend(re.findall(r"^make\s+([a-z-]+)\s*$", run, re.MULTILINE))
    return targets


def _check_prerequisites(repo_root: Path) -> list[str]:
    makefile = (repo_root / "Makefile").read_text(encoding="utf-8")
    match = re.search(r"^check:\s*([^#\n]*)", makefile, re.MULTILINE)
    assert match is not None, "the Makefile declares a check target"
    return match.group(1).split()


def test_workflow_runs_the_check_gates_in_order(repo_root: Path) -> None:
    """The hosted job runs exactly the gates `make check` runs, in its order."""
    assert _make_targets(_workflow_steps(repo_root)) == _check_prerequisites(repo_root)


@pytest.mark.parametrize(("tool", "marker"), sorted(EXTERNAL_TOOLS.items()))
def test_workflow_installs_every_external_tool(
    repo_root: Path, tool: str, marker: str
) -> None:
    """Every external command a gate calls has an installing step before it."""
    steps = _workflow_steps(repo_root)
    first_gate = next(
        index for index, step in enumerate(steps) if _make_targets([step])
    )
    installers = steps[:first_gate]
    assert any(
        marker in str(step.get("uses", "")) or marker in str(step.get("run", ""))
        for step in installers
    ), f"{tool} is not installed before the first gate"


def test_installed_tools_are_pinned(repo_root: Path) -> None:
    """Tool installs name an exact version or a full commit SHA."""
    for step in _workflow_steps(repo_root):
        uses = step.get("uses")
        if isinstance(uses, str):
            assert re.search(r"@[0-9a-f]{40}$", uses.strip()), uses
        run = step.get("run")
        if isinstance(run, str) and "install -g" in run:
            assert re.search(r"@\d+\.\d+\.\d+\s*$", run.strip()), run
