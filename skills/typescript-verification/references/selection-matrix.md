# Verification selection matrix

Use this after the testing hierarchy has ruled out a named example, a finite
table, and an obvious lightweight property. The matrix chooses an escalation
target; it is not a reason to escalate.

## At a glance

| Concern         | Compile-time test               | fast-check                         | fast-check commands or scheduler                  | Mutation testing            | LemmaScript                                       |
| --------------- | ------------------------------- | ---------------------------------- | ------------------------------------------------- | --------------------------- | ------------------------------------------------- |
| Engine          | The type checker                | Generation plus shrinking          | Generated operation sequences; promise reordering | Mutation of production code | Specification plus a prover (Dafny, Lean)         |
| Answers         | Does the type reject this?      | Does the relation survive?         | Does a sequence or interleaving break it?         | Would the suite notice?     | Does it hold for every input?                     |
| Best on         | Public vocabularies, registries | Pure functions, codecs, invariants | Stores, protocols, async coordination             | Fast, stable suites         | Small pure kernels with load-bearing invariants   |
| Worst on        | Runtime behaviour               | Heavy I/O per case                 | Models that mirror the implementation             | Slow or flaky suites        | `async`, closures over mutable state, floats, I/O |
| Cadence         | Every type check                | Every CI run                       | Every CI run (default runs)                       | Nightly or pre-release      | On change to the kernel; on demand                |
| Counter-example | Compiler diagnostic             | Shrunk input with seed and path    | Shrunk command sequence                           | Surviving mutant diff       | Prover failure at a named obligation              |

_Table 1: The approaches compared._

## Pick by question

- "This type must reject that shape." → Compile-time test; no runtime tool
  helps.
- "The same relation should hold over many values and built-in arbitraries
  describe them." → Lightweight `fast-check`; no selector ceremony.
- "Valid data has dependent fields or recursive structure." → `fast-check`
  with composed arbitraries (`chain`, `letrec`); never heavy filtering.
- "The bug depends on a sequence of operations." → `fast-check` commands with
  a simplified model.
- "The bug depends on which promise resolves first." → `fast-check` scheduler.
- "Tests pass; I do not trust that they would catch a defect." → Mutation
  testing on the modules that matter.
- "A violation would be severe, the function is pure, and sampling is not
  enough." → LemmaScript, with the property kept beneath it.

## When to leave the cluster

- **Rendering and accessibility:** component and end-to-end tests.
- **Integration:** one real boundary per test.
- **Timing and throughput:** traces, frame timing, benchmarks.
- **Package consumers:** packed-install smoke tests, `publint`, `attw`.

## Common mis-applications

- Replacing a transition table with generated values. The table is the
  specification; the property checks a relation across it.
- A model-based test whose model is the implementation copied.
- Proving a function that the type system already constrains, or "proving"
  a timeout, a schedule, or an IPC round trip.
- Mutation testing over generated code, adapters, or an end-to-end suite.
- Running the long property tier, mutation, and proofs on every push with no
  stated assurance target.
- A fast-check property that passes at 100 runs and fails at 1000, "fixed" by
  lowering `numRuns`.

## Determinism fences

Model-based tests, scheduled runs, and proofs need the system under test to be
deterministic given its inputs. Inject the clock, the random source, and the
identifier allocator; forbid `Date.now()` and `Math.random()` in the core with
a lint rule; and run the same-seed double-run gate so a leak is caught early.
Route the design to `typescript-data-and-state`.
