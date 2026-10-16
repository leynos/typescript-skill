---
name: typescript-testing
description: Use for testing TypeScript and JavaScript, including named examples, tables, compile-time type tests, unit tests, component tests, integration tests, accessibility tests, browser and Electron end-to-end tests, virtual time, and deterministic schedulers.
metadata:
  globs: "**/*.test.ts, **/*.test.tsx, **/*.spec.ts, **/*.test-d.ts, **/*.pw.ts, **/*.e2e.ts, **/tests/**, **/test/**, **/vitest.config.*, **/bunfig.toml, **/playwright.config.*"
---

# TypeScript testing

Use this when the question is which test to write and at what level: a named
example, a table, a compile-time type test, a component test, an integration
test, or an end-to-end run. Choose the evidence first, then the tool.

## Working stance

- A test is a specification someone can read. Its name says why the case
  belongs; its body shows one behaviour. A table removes duplicated bodies; it
  does not impersonate coverage of an open domain.
- The type system is the first test. A shape the compiler rejects needs no
  runtime test; a public type vocabulary that must reject shapes needs a
  compile-time test that proves it does.
- Determinism is a property of the code under test, not of the runner. Clocks,
  randomness, identifiers, and scheduling are injected so a test can control
  them; a test that needs `setTimeout` to "settle" is testing the scheduler.
- Test through the boundary the consumer uses: a component by role and name, a
  package through its `exports` map, a CLI through its `bin`, a protocol
  through its schemas.
- The runner is a project decision, made once: `bun test`, Vitest, or
  `node:test`. Do not mix them in one package.

## Testing hierarchy

Pick the first rung whose evidence matches the question, and stop there.

0. **The type system.** Make the illegal state unrepresentable. Route to
   `typescript-types-and-apis`. A compile-time test (`.test-d.ts` with
   `@ts-expect-error` and `satisfies`) proves a public vocabulary rejects what
   it should; see
   [compile-time-type-tests.md](references/compile-time-type-tests.md) and the
   [type-contract.ts](../../examples/diagnostics/type-contract.ts) fixture.
1. **Named example.** One scenario, boundary, regression, rendered output, or
   error contract.
2. **Table.** A finite truth table or standards corpus where each row carries
   meaning. A transition table is the canonical case.
3. **Lightweight property.** One relation over many cheap generated inputs.
   Route to `fast-check`; no selector ceremony is needed for an obvious
   invariant.
4. **Model-based or scheduled property.** Operation sequences, dependent data,
   or async interleavings. Stay with `fast-check`.
5. **Proof.** A load-bearing property that must hold for every input in a
   supported pure subset. Route through `typescript-verification` to
   `lemmascript`.

Mutation testing sits beside the hierarchy: it audits whether the suite would
notice a defect. See [the hierarchy reference](references/testing-hierarchy.md).

Leave the hierarchy when the failure depends on rendering, a real service, a
process boundary, a schedule under load, or a package consumer. Those need a
component test, an integration test, a benchmark, an end-to-end run, or a
packed-install check. See
[integration-and-e2e.md](references/integration-and-e2e.md).

## Decision surface

- **Unit versus integration.** A unit test injects every port (clock, storage,
  transport) and runs in milliseconds. An integration test uses one real
  boundary (a database, a file system, a child process) and is tagged so the
  fast loop can skip it.
- **Virtual time.** Fake timers for debounce, timeout, retry, and scheduling
  logic; a virtual clock injected through a port for domain code. A test that
  advances time explicitly documents the timing contract. See
  [virtual-time-and-schedulers.md](references/virtual-time-and-schedulers.md).
- **Deterministic schedulers.** A logical worker that drains transitions in
  virtual-time order is tested by advancing the clock and asserting the
  journal; the same-seed double-run equality is a property, not a test.
- **Component tests.** Role and name queries, user-event, the real provider
  stack, an accessibility assertion on representative screens. Route to
  `react-and-accessible-ui`.
- **End-to-end.** Playwright for browser and Electron. A fast smoke on every
  push; the deep suite on pull requests; accessibility scans and
  accessibility-tree snapshots on key screens; flakes quarantined with an
  issue, not retried into green.
- **Concurrency in the runner.** Run suites concurrently and shuffled by
  default so order dependence surfaces; a suite that needs serialization says
  so with a reason.
- **Snapshots.** For rendered output and generated artefacts, reviewed on
  change. A snapshot is an example, never the specification of an invariant.

## Red flags

- `await new Promise((r) => setTimeout(r, 50))` in a test.
- A test that mocks the module under test's own collaborators to the point of
  asserting the mock.
- A table whose rows sample one invariant with different numbers; that is a
  property.
- A `.test-d.ts` file that nothing compiles.
- `test.skip` or a retry count added to make a flaky test pass.
- A component test that queries by test ID or class name.
- An integration test that runs in the unit loop and needs a network.
- Coverage thresholds treated as the goal; a mutation score says more.

## Pairing

- Pair with `fast-check` when rows keep multiplying for one relation.
- Pair with `typescript-verification` when the rung is unclear.
- Pair with `react-and-accessible-ui` for component tests.
- Pair with `typescript-modules-and-packaging` for packed-install tests.
