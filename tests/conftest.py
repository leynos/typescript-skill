"""Shared fixtures for the catalogue's contract suite."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def repo_root() -> Path:
    """Locate the catalogue's checkout root.

    Returns
    -------
    Path
        The repository root, derived from this file's location rather than
        the working directory, so the suite is insensitive to where pytest
        was invoked from.
    """
    return REPO_ROOT
