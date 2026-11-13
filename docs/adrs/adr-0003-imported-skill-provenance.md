# ADR 0003: imported deep dives keep their content and gain a manifest

Date: 2026-10-16

Status: accepted

## Context

Five skills were imported rather than written here: `fast-check` and
`lemmascript` from `agent-helper-scripts/skills/`, `zod4-typescript` and
`biome-typescript` from the same repository, and `effect-v4` from a skill bundle
(`effect-v4.skill`, a zip archive) built on 2026-10-15 against `effect@4.0.5`.
Each was written to a different house style: American spelling, longer
`SKILL.md` files, a routing table inside the skill, and in the Effect case two
Python helper scripts and a verbatim copy of upstream documentation under an
MIT licence.

This catalogue's own skills follow a 160-line budget, British spelling with
Oxford `-ize`, and the pattern of judgement in `SKILL.md` and recipes in
`references/`.

## Decision

Imported skills keep their content. The changes made on import are limited to
what the catalogue's gates require:

- `metadata.globs` added to the frontmatter, because every skill in this
  catalogue carries a glob hint;
- `agents/openai.yaml` added with `allow_implicit_invocation: false`, so the
  router keeps the routing decision;
- Markdown reflowed by `make fmt` (table alignment and 80-column wrapping).
  The reflow changes whitespace only. Upstream verbatim material under
  `effect-v4/references/upstream/` and the generated rename tables under
  `effect-v4/references/renames/` are excluded from the Markdown lint, so their
  content is never edited to satisfy a rule.

Each imported skill has a line envelope recorded in
`tests/test_skill_catalogue.py` and in the catalogue status, larger than the
160-line budget, and an owner skill that links to it. The Effect helper scripts
are shipped as part of the skill and are outside the repository's Python lint
scope, because they are the skill's artefacts rather than this repository's
tooling.

Spelling is not normalized. A spelling gate is deferred (see the design
principles) because rewriting imported prose is churn and excluding it would
weaken the gate.

## Consequences

- A reader of an imported skill will notice a different voice. That is
  accepted in exchange for a faithful copy.
- Upgrading an imported skill means re-importing from its source, re-applying
  the three manifest changes, and re-running `make fmt`. The catalogue status
  names the source and version of each.
- If an imported skill is later rewritten to the house style, this ADR should
  be superseded for that skill and the envelope removed.
