---
name: typescript-verification
description: Select the verification approach for TypeScript when examples are not enough, choosing between ordinary tests, compile-time type tests, fast-check properties, stateful and race exploration, mutation testing, and LemmaScript proof by the evidence required rather than by perceived tool strength.
metadata:
  globs: "**/*.test.ts, **/*.test-d.ts, **/*.property.ts, **/LemmaScript-files.txt, **/*.dfy, **/stryker.config.*"
---

# TypeScript verification

Use this when the required evidence is unclear or the task has outgrown named
examples and an obvious property. Do not insert a selector ceremony between a
clear, cheap invariant and a ten-line `fc.assert`; load `fast-check` directly
for that case.

The tools here answer different questions. They form an escalation map, not a
single scale from weak to strong.

## Before escalating

- One named scenario, exact output, or finite normative table belongs in
  `typescript-testing`.
- A public type vocabulary that must reject shapes belongs in a compile-time
  test, also in `typescript-testing`.
- One invariant over a broad, cheap, repeatable input space belongs directly
  in `fast-check`.
- Load this selector when valid data needs a model, operation history matters,
  interleavings matter, the property must hold for every input, or the question
  is whether the suite would detect wrong code.

## The questions each approach answers

- **Compile-time type test**: *Does the type system reject this shape?*
  Assignability, inference, forbidden fields, closed vocabularies.
- **`fast-check` property**: *Does this relation survive generated inputs?*
  Round trips, idempotence, oracles, invariants, metamorphic relations, with
  shrinking to a minimal counter-example.
- **`fast-check` commands and scheduler**: *Does an operation sequence or an
  async interleaving break an invariant?* Model-based testing against a
  simplified model; scheduled runs that reorder promises.
- **Mutation testing (StrykerJS)**: *Would the suite notice if the production
  code were wrong?* It measures test sensitivity, not correctness.
- **LemmaScript proof**: *Does this hold for every input in the supported pure
  subset?* A specification in `//@` comments discharged by Dafny or Lean, with
  trusted boundaries stated.

## Selection by question

| Question                                                                        | Route                                              |
| ------------------------------------------------------------------------------- | -------------------------------------------------- |
| Are there a few named behaviours?                                               | `typescript-testing`, rung 1 or 2                  |
| Is the contract about assignability, inference, or forbidden fields?            | Compile-time test, `typescript-testing`            |
| Does a deterministic invariant span many inputs?                                | `fast-check`                                       |
| Is it a state machine or an async interleaving problem?                         | `fast-check` commands or scheduler                 |
| Do tests fail when the implementation is deliberately broken?                   | Mutation testing; guidance here, no specialist yet |
| Must a load-bearing property hold for all inputs in a supported pure subset?    | `lemmascript`                                      |
| Is the claim about rendering, integration, accessibility, timing, or consumers? | Leave this cluster; see `typescript-testing`       |

*Table 1: The selector, one question per row.*

See [selection-matrix.md](references/selection-matrix.md) for the at-a-glance
comparison and common mis-applications.

## Working stance

- Name the failure mode before naming the tool.
- Each approach is additive: a proof does not replace the property beneath it,
  and a property does not replace the named regression.
- Run cheap adversaries on every change; reserve expensive sweeps for code
  where they pay back.
- The effort is not finished until a deliberate mutation of the production
  code is caught by it.
- Determinism is a precondition. Model-based tests, scheduled runs, and proofs
  all need the code's clock, randomness, and identifiers injected.

## Layering rule

Climb only when the layer below is clean; bugs found higher up are harder to
diagnose.

1. Types and compile-time tests close the shapes the compiler can see.
2. Named examples and tables anchor concrete expectations.
3. `fast-check` widens inputs; a scheduled run shakes the interleaving.
4. Mutation testing checks that the suite can fail.
5. LemmaScript proves the load-bearing kernel for every input.

## What none of them establish

- A passing property run is not a proof outside the sampled domain; a passing
  proof says nothing about code outside the supported fragment or about the
  trusted boundaries it names.
- Race conditions need scheduler-aware exploration, not more cases.
- Rendering, accessibility, and integration need their own tests.
- Performance needs traces and benchmarks.
- A wrong contract survives every tool; review the specification as
  adversarially as the code.

## Red flags

- A direct invariant routed through several documents before anyone writes
  the obvious `fc.assert`.
- A property that filters most inputs; construct valid data instead.
- A model that mirrors the implementation; it proves nothing.
- A shrunk counter-example left as a seed in a comment instead of promoted to
  a named test.
- A `.test-d.ts` file nothing compiles.
- A proof target that differs from the shipped function, or a `//@ assume`
  added to silence the prover.
- Mutation testing run as a pull-request gate over a slow or flaky suite.
- A verification job with no stated assurance target in its name or comment.

## Routing into deep dives

- Arbitraries, the filtering trap, commands, the scheduler, replay, and CI
  tiering: [`fast-check`](../fast-check/SKILL.md).
- Annotations, the edit loop, backends, trusted boundaries, and brownfield
  proof strategy: [`lemmascript`](../lemmascript/SKILL.md).
- Mutation testing: [mutation-testing.md](references/mutation-testing.md)
  carries the guidance until a project adopts StrykerJS and earns a specialist.
- Stateful and race exploration, and when to go to proof instead:
  [state-and-race-exploration.md](references/state-and-race-exploration.md).
