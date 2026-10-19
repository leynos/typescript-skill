# Agent instructions

Guidance for agents working in this repository. Read this before changing
tracked files.

## Commit gates

Use the Makefile targets and run them sequentially, never in parallel: the uv
cache, the Bun install, and the TypeScript build cache are shared, and
sequential runs benefit from them.

```bash
make check
```

`make check` is the default goal and runs `check-fmt`, `lint`, `typecheck`,
`examples`, and `test` in order, stopping at the first failure. Run it before
every commit. `make fmt` rewrites files and is deliberately not part of `check`.

## Changes under `skills/`

Every skill is a directory containing a `SKILL.md` whose YAML frontmatter is an
Agent Skills manifest. The manifest `name` is the discovery name.

- Keep the directory name equal to the manifest `name`.
- Keep the frontmatter to `name`, `description`, `license`, `allowed-tools`,
  `metadata`, and `compatibility`. Put anything else under `metadata`.
- Keep `metadata` a mapping of strings to strings with a comma-separated
  `globs` hint. `skills-ref` coerces other shapes with `str(v)` rather than
  rejecting them.
- Ship `agents/openai.yaml` with `policy.allow_implicit_invocation: false`
  for every skill except `typescript-router`, so the router keeps the routing
  decision.
- Name every new skill in the router's "Route by question" list, in
  `skills/typescript-router/references/routing-matrix.md`, and in
  `docs/skill-catalogue-status.md`. The contract suite enforces all three.
- Keep `SKILL.md` within 160 lines. The router and the imported deep dives
  carry larger envelopes recorded in `tests/test_skill_catalogue.py` and the
  catalogue status. Push comparison tables and worked examples into
  `references/`, and link every reference from the skill.
- Keep compiler-version claims (`tsgo`, native preview, `TypeScript 7.x`)
  inside `typescript-7-transition`, the router, and the imported skills that
  pin their own floor. `tests/test_versioned_claims.py` enforces this.
- Give each imported deep dive exactly one owning skill that links to it, and
  record the pair in the ownership table in `tests/test_skill_catalogue.py`.

Do not weaken a check to make a skill pass. Fix the skill instead.

To check one skill while iterating:

```bash
make skill-manifest-check SKILL_DIRS=skills/typescript-router/
```

## Executable examples

Claims about compiler behaviour are evidenced, not remembered.

- Put complete TypeScript under `examples/positive/` (must compile) or
  `examples/diagnostics/` (each expected error marked with
  `// @ts-expect-error <reason>`). The gate compiles both under the TypeScript
  release pinned in `examples/package.json`.
- Start every fixture with `// Linked from skills/<name>/SKILL.md.` and link
  it from that skill. The contract suite enforces the pair.
- Do not add a second compiler to the gate. TypeScript 6 behaviour is
  described in `typescript-7-transition`, not compiled here.

## Documentation and prose

- Changes that alter skill discovery, installation, or naming belong in
  [the users' guide](docs/users-guide.md). Changes to gates, scripts,
  dependencies, or tests belong in
  [the developers' guide](docs/developers-guide.md).
- Record notable changes in [the changelog](CHANGELOG.md), which follows
  Common Changelog.
- Write en-GB-oxendict prose (`-ize`, `-our`) in the catalogue's own skills
  and documents, wrapped at 80 columns, with sentence-case headings, dash
  bullets, and language-labelled fences. Imported skills keep their original
  spelling; see [ADR 0003](docs/adr/0003-imported-skill-provenance.md).
- Caption every table (`_Table N: …_`) and diagram (`_Figure N: …_`), with a
  screen-reader description before each diagram, and use `plaintext` for fences
  that hold no code.
- Keep [the source inventory](docs/source-inventory.md) dated and cite a file
  path for every estate fact used in a skill.
- Make atomic commits with imperative subjects and reasons in the body.

## Python

Any Python added here, including tests, is formatted and linted by Ruff and
type-checked by strict mypy through the `dev` dependency group. The vendored
`scripts/uv_gate.py` is copied byte for byte from `shared-actions` and is never
edited in place. The Effect skill's helper scripts under
`skills/effect-v4/scripts/` are the skill's artefacts and are outside the
repository's Python lint scope.
