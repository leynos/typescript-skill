"""Behavioural tests for the Makefile gate wiring.

The recipes are planned with ``make -n`` so the commands they would run are
observed rather than read from the recipe text. Nothing here executes the
external tools.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest


def _plan(repo_root: Path, *targets: str) -> str:
    result = subprocess.run(
        ["make", "--no-print-directory", "-n", *targets],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_default_goal_is_check(repo_root: Path) -> None:
    """Running make with no target must plan exactly what `make check` plans."""
    assert _plan(repo_root) == _plan(repo_root, "check")


@pytest.mark.parametrize(
    "command",
    [
        "markdownlint-cli2",
        "nixie",
        "skills-ref validate",
        "yamllint",
        "ruff format --check",
        "ruff check",
        "mdtablefix --check",
        "mypy",
        "pytest",
        "bun run check",
    ],
)
def test_check_reaches_every_gate(repo_root: Path, command: str) -> None:
    """`check` aggregates formatting, lint, manifests, types, examples, tests."""
    assert command in _plan(repo_root, "check"), f"{command} is not reached by check"


def test_check_never_rewrites_files(repo_root: Path) -> None:
    """`fmt` rewrites files, so the gate may check but must never rewrite."""
    plan = _plan(repo_root, "check")

    assert "--in-place" not in plan, "check plans an in-place mdtablefix"
    assert "--fix" not in plan, "check plans a markdownlint --fix"
    assert not re.search(r"\bruff format(?! --check)\b", plan), (
        "check plans a rewriting ruff format"
    )


def test_fmt_rewrites_python_tables_and_markdown(repo_root: Path) -> None:
    """`fmt` formats Python, reflows tables, then applies markdownlint fixes."""
    plan = _plan(repo_root, "fmt")

    assert "ruff format tests" in plan
    assert "mdtablefix --in-place --git --include-untracked" in plan
    assert plan.rstrip().endswith('markdownlint-cli2 --fix "**/*.md"')


def test_examples_gate_installs_with_a_frozen_lockfile(repo_root: Path) -> None:
    """The example gate must not float the TypeScript release it pins."""
    plan = _plan(repo_root, "examples")

    assert "bun install --frozen-lockfile --cwd examples" in plan
    assert "bun run check" in plan
