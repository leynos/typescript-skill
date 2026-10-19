"""Contract tests for shipped Agent Skills manifests.

Each shipped skill's ``SKILL.md`` opens with YAML frontmatter that a strict
loader reads before the skill is usable. Each sub-skill also ships an
``agents/openai.yaml`` that opts it out of implicit invocation, leaving the
router as the catalogue's discovery surface. The Makefile targets exercised
here are the ones ``make lint`` depends on, so a manifest that a loader could
not use fails the commit gate rather than reaching an installation untouched.

These run in the checkout rather than in a scratch repository: the manifest
targets resolve their tools through the uv helper, which needs the real
``pyproject.toml`` and ``uv.lock``.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from tests.catalogue import ROUTER, skill_dirs

REPO_ROOT = Path(__file__).resolve().parents[1]
SHIPPED = skill_dirs(REPO_ROOT)
IMPLICIT_INVOCATION = "allow_implicit_invocation"

BROKEN_MANIFEST = "---\nname: [unclosed\n---\n\n# Broken\n"
VALID_MANIFEST = (
    "---\nname: z-valid\ndescription: A conformant trailing fixture.\n---\n\n# Valid\n"
)
INVALID_MANIFEST = "---\nname: b-invalid\n---\n\n# Fixture\n"
BROKEN_SYNTAX_ERROR = "syntax error: expected ',' or ']', but got '<document start>'"


def _run_make(target: str, *skill_dirs_: Path) -> subprocess.CompletedProcess[str]:
    arguments = ["make", target]
    if skill_dirs_:
        arguments.append("SKILL_DIRS=" + " ".join(f"{d}/" for d in skill_dirs_))
    return subprocess.run(
        arguments, cwd=REPO_ROOT, text=True, capture_output=True, check=False
    )


def _write_manifest(skill_dir: Path, body: str) -> Path:
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(body, encoding="utf-8")
    return skill_dir


def _openai_policy(skill_dir: Path) -> dict[str, object] | None:
    config = skill_dir / "agents" / "openai.yaml"
    if not config.is_file():
        return None
    parsed = yaml.safe_load(config.read_text(encoding="utf-8"))
    assert isinstance(parsed, dict), f"{config} is not a YAML mapping"
    policy = parsed.get("policy")
    assert isinstance(policy, dict), f"{config} carries no policy mapping"
    return policy


def test_shipped_skill_manifests_satisfy_the_contract() -> None:
    """Every shipped skill passes YAML and Agent Skills schema validation."""
    result = _run_make("skill-manifest-check")

    assert result.returncode == 0, result.stdout + result.stderr


def test_default_skill_dirs_reach_every_shipped_skill() -> None:
    """The Makefile's own ``SKILL_DIRS`` default validates every shipped skill."""
    result = _run_make("skill-manifest-validate")

    assert result.returncode == 0, result.stdout + result.stderr
    validated = {
        line.removeprefix("Valid skill: ")
        for line in result.stdout.splitlines()
        if line.startswith("Valid skill: ")
    }
    shipped = {str(path.relative_to(REPO_ROOT)) for path in SHIPPED}

    assert validated == shipped, (
        f"default SKILL_DIRS missed {sorted(shipped - validated)} "
        f"and added {sorted(validated - shipped)}"
    )


@pytest.mark.parametrize(
    ("case", "frontmatter", "expected"),
    [
        (
            "missing-name",
            "description: Lacks a name.\n",
            "Missing required field in frontmatter: name",
        ),
        (
            "empty-name",
            'name: ""\ndescription: Empty name.\n',
            "Field 'name' must be a non-empty string",
        ),
        (
            "missing-description",
            "name: missing-description\n",
            "Missing required field in frontmatter: description",
        ),
    ],
)
def test_manifest_check_rejects_an_unusable_manifest(
    tmp_path: Path, case: str, frontmatter: str, expected: str
) -> None:
    """Both required fields are enforced, present but unusable included."""
    skill_dir = _write_manifest(
        tmp_path / case, f"---\n{frontmatter}---\n\n# Fixture\n"
    )

    result = _run_make("skill-manifest-check", skill_dir)

    assert result.returncode != 0, result.stdout + result.stderr
    assert expected in result.stderr, result.stdout + result.stderr


@pytest.mark.parametrize(
    "skill", [p for p in SHIPPED if p.name != ROUTER], ids=lambda p: str(p.name)
)
def test_sub_skills_disable_implicit_invocation(skill: Path) -> None:
    """Every skill but the router opts out of implicit invocation."""
    policy = _openai_policy(skill)

    assert policy is not None, f"{skill.name} ships no agents/openai.yaml"
    assert policy.get(IMPLICIT_INVOCATION) is False, (
        f"{skill.name} must set {IMPLICIT_INVOCATION}: false, got {policy!r}"
    )


def test_router_keeps_its_own_invocation_policy() -> None:
    """The router stays implicitly invocable, so the catalogue is discoverable."""
    policy = _openai_policy(REPO_ROOT / "skills" / ROUTER)

    assert policy is None or policy.get(IMPLICIT_INVOCATION) is not False, (
        f"the router must stay implicitly invocable, got {policy!r}"
    )


def test_frontmatter_lint_reports_an_early_failure(tmp_path: Path) -> None:
    """A failure in any skill fails the target, not just one in the final skill."""
    broken = _write_manifest(tmp_path / "a-broken", BROKEN_MANIFEST)
    valid = _write_manifest(tmp_path / "z-valid", VALID_MANIFEST)

    result = _run_make("skill-frontmatter-lint", broken, valid)

    assert result.returncode != 0, result.stdout + result.stderr
    assert BROKEN_SYNTAX_ERROR in result.stdout, result.stdout + result.stderr


@pytest.mark.parametrize(
    "invalid_first", [True, False], ids=["invalid-first", "invalid-last"]
)
def test_manifest_validate_reports_a_failure_in_any_position(
    tmp_path: Path, *, invalid_first: bool
) -> None:
    """A non-conformant directory fails the target wherever it sits in the list."""
    valid = _write_manifest(tmp_path / "z-valid", VALID_MANIFEST)
    invalid = _write_manifest(tmp_path / "b-invalid", INVALID_MANIFEST)
    dirs = (invalid, valid) if invalid_first else (valid, invalid)

    result = _run_make("skill-manifest-validate", *dirs)

    assert result.returncode != 0, result.stdout + result.stderr
    assert "Missing required field in frontmatter: description" in result.stderr, (
        result.stdout + result.stderr
    )
