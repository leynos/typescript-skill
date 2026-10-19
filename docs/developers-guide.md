# Developers' guide

This guide covers working on the repository: the Markdown catalogue, the pytest
contract suite, the TypeScript example gate, and the `Makefile` that ties them
together. It does not cover using the skills; see
[the users' guide](users-guide.md).

## Prerequisites

- `uv`, for the pinned `dev` dependency group (pytest, mypy, Ruff, PyYAML,
  `skills-ref`, `yamllint`).
- `bun`, for the TypeScript example gate. `examples/package.json` pins the
  TypeScript release and `bun.lock` pins its platform binaries.
- `markdownlint-cli2`, `nixie`, and `mdtablefix` (0.6.1 or later) on `PATH`.
  These are external tools the lint gates call directly.

`pyproject.toml` sets `requires-python = ">=3.14"` and
`[tool.uv] package = false`: the repository is not an installable package, only
a source of test tooling for the catalogue.

## The gates

`.DEFAULT_GOAL := check`, so a bare `make` runs the full commit gate.

| Target                      | What it does                                                   |
| --------------------------- | -------------------------------------------------------------- |
| `make help`                 | Show the target list                                           |
| `make fmt`                  | Format Python, reflow Markdown tables and wrapping, lint fixes |
| `make check-fmt`            | Markdown lint, Ruff format check, `mdtablefix --check`         |
| `make markdownlint`         | Lint every Markdown file                                       |
| `make nixie`                | Validate every Mermaid diagram                                 |
| `make skill-manifest-check` | Frontmatter lint plus Agent Skills schema validation           |
| `make lint`                 | The three above plus `ruff check`                              |
| `make typecheck`            | Strict mypy over `tests/`                                      |
| `make examples`             | Install pinned TypeScript, compile `examples/`                 |
| `make test`                 | Run the pytest contract suite                                  |
| `make check`                | Default goal; every gate above except `fmt`                    |

_Table 1: Makefile targets and what each one does._

`make fmt` rewrites files with Ruff,
`mdtablefix --in-place --git
--include-untracked --wrap --renumber --breaks --ellipsis --fences`,
and `markdownlint-cli2 --fix`. It is not part of `check` because a commit gate
should not mutate the working tree. `check-fmt` runs the same `mdtablefix`
command with `--check`.

Every `uv` call goes through the vendored `scripts/uv_gate.py`, which cleans
the environment, uses the global cache, runs offline first, and goes online at
most once. `make prepare` installs the locked environment; the gates that run
Python depend on it.

## The skill manifest contract

Every `skills/<name>/SKILL.md` opens with YAML frontmatter carrying `name`,
`description`, and `metadata.globs`. `make skill-frontmatter-lint` extracts the
block with `awk` and pipes it through `yamllint`;
`make skill-manifest-validate` runs `skills-ref validate` over each directory.
`tests/test_skill_manifests.py` checks that both targets reject malformed
fixtures in any list position and that every non-router skill ships
`agents/openai.yaml` with implicit invocation disabled.

## What the contract suite covers

| Test module                 | Invariant                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test_skill_catalogue.py`   | Directory and manifest names agree; every route resolves; every skill is routed; the status doc matches the tree; deep dives have one owner; line budgets hold |
| `test_router_contract.py`   | The four opening questions are present; pinned routes and matrix rows keep their destination; the pairing cap is stated                                        |
| `test_reference_links.py`   | Every relative link resolves; every reference is linked from its skill (grepped directories count by name)                                                     |
| `test_routing_scenarios.py` | Scenario rows name real skills; the six design scenarios keep their route                                                                                      |
| `test_versioned_claims.py`  | Compiler-version claims appear only in versioned material; the transition skill names a release and a date                                                     |
| `test_examples.py`          | Fixtures declare and are linked from their skill; diagnostics fixtures expect an error; the gate reaches both directories; TypeScript is pinned exactly        |
| `test_makefile.py`          | `check` is the default goal, reaches every gate, and never rewrites                                                                                            |
| `test_skill_manifests.py`   | Manifest targets reject malformed fixtures; invocation policy                                                                                                  |
| `test_ci_workflow.py`       | The Tests workflow runs the `check` prerequisites in order, installs every external tool first, and pins each install                                          |
| `test_effect_scripts.py`    | The Effect skill's `has_export.py` returns a whole wrapped rename-table row as one hint; every shipped row names a replacement; both scripts work end to end   |
| `test_prose_style.py`       | Catalogue-owned skills and documents never address the reader in the first or second person; imported skills and the README are exempt                         |

_Table 2: Test modules and the invariants each one holds._

The parsers the tests share live in `tests/catalogue.py`. The conventions they
read are the catalogue's structural contract: a "Route by question" list whose
bullets end with a colon and the backticked destination skill, a three-column
routing matrix, backticked skill names in the status document's "Active skills"
section, and a "Linked from" header comment in each fixture. Change the parser
and the convention together.

## The example gate

`examples/tsconfig.json` models the greenfield strictness posture and includes
`positive/**/*.ts` and `diagnostics/**/*.ts`. `make examples` runs
`bun install --frozen-lockfile` and then `tsc -p tsconfig.json` with `noEmit`.
A diagnostics fixture passes when every `@ts-expect-error` has an error under
it; an unused marker is itself an error, so the fixture proves the diagnostic
fires. Bump the TypeScript pin deliberately: `examples/package.json`,
`bun.lock`, and `typescript-7-transition`'s review date move together.

## Continuous integration

Two workflows run on pull requests and on pushes to `main`. `Markdown lint`
runs the markdownlint action on its own so a prose failure is visible at a
glance. `Tests` installs `uv`, Bun, `mdtablefix`, `markdownlint-cli2`, and
`nixie`, then runs `make check-fmt`, `make lint`, `make typecheck`,
`make examples`, and `make test`: the same gates, in the same order, as a local
`make check`. `tests/test_ci_workflow.py` reads the workflow and the Makefile
and fails when the step list stops matching the `check` prerequisites or an
install step loses its version pin. Add a tool to the Makefile and to the
workflow together.

## Adding or importing a skill

1. Create `skills/<name>/SKILL.md` with the manifest, `references/`, and
   `agents/openai.yaml`.
2. Add a "Route by question" bullet, at least one routing-matrix row, and a
   status-document entry.
3. If the skill is imported, keep its content, add the manifest fields, run
   `make fmt`, add its line envelope and owner to
   `tests/test_skill_catalogue.py`, and record its source in the catalogue
   status.
4. If the skill carries a fixture, add the `// Linked from` header and link it
   from the skill.
5. Run `make check`.
