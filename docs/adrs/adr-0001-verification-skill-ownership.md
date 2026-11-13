# ADR 0001: the TypeScript catalogue owns the verification deep dives

Date: 2026-10-16

Status: accepted

## Context

The `fast-check` and `lemmascript` skills were written as TypeScript
verification deep dives and merged into the `agent-helper-scripts` repository
on 2026-08-14 (PR #25), before a TypeScript catalogue existed. That merge added
the two deep dives but not the question-first selector that decides between
ordinary tests, compile-time type tests, properties, stateful or race
exploration, mutation testing, and proof.

This catalogue adds that selector as `typescript-verification`. A selector that
routes to deep dives living in a different repository would be fragile: the
deep dives would be installed or not depending on which repository a user
pulled, and edits to the boundary between selector and deep dive would span two
repositories and two review queues.

## Decision

The two deep dives move into this catalogue under their existing names,
`fast-check` and `lemmascript`, and `typescript-verification` is their owner:
it is the skill whose decision surface decides when each deep dive is worth
loading, and the contract suite checks that it links to both.

This catalogue is their canonical home from this change onward. The copies in
`agent-helper-scripts/skills/` are to be removed in that repository, and its
installer updated to pull the TypeScript catalogue, in a follow-up change
there. Until that change lands, the two copies are byte-identical apart from
the manifest additions this repository requires (`metadata.globs` and
`agents/openai.yaml`).

Two alternatives were rejected: leaving the deep dives where they are and
linking across repositories, and rewriting them from scratch here. The first
splits one boundary across two review queues; the second manufactures
divergence.

## Consequences

- `tests/test_skill_catalogue.py` carries an ownership table mapping each deep
  dive to its owner and asserts the owner links to it. Moving a deep dive to a
  different owner is a deliberate edit to that table.
- The router routes verification questions to `typescript-verification` and
  names the deep dives after a semicolon, matching the Rust and Python
  catalogues; a parser-guard test asserts the deep dives stay reachable.
- A StrykerJS deep dive is deliberately absent. The selector reserves mutation
  testing's place and gives guidance; a specialist arrives when a project in
  the estate adopts the tool.
- The installer manifest change in `agent-helper-scripts` is tracked outside
  this repository and is not a precondition for this catalogue to be correct.
