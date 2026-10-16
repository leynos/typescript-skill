---
name: typescript-router
description: Route TypeScript and JavaScript work to the smallest useful skill. Use for type modelling, runtime data and state, trust boundaries and validation, errors and outcomes, async and worker ownership, modules and packaging, browser main-thread performance, React and accessible UI, Node and Bun processes, Electron and IPC, package design, testing, verification, quality tools, and the TypeScript 7 transition.
metadata:
  globs: "**/tsconfig*.json, **/package.json, **/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.js, **/*.jsx, **/*.mjs, **/*.cjs"
---

# TypeScript router

Load this first for non-trivial TypeScript or JavaScript work, then load only
the smallest useful follow-on skill. The catalogue is about choosing the right
execution context, boundary, evidence, and enforcement mechanism for JavaScript
that happens to be engineered with TypeScript. It is not a tutorial on syntax.

## Working stance

- Route by pressure, not by brand. "This project uses React" is context; the
  diagnosis is what is hard: type modelling, untrusted input, asynchronous
  ownership, packaging, frame responsiveness, IPC privilege, evidence, or lint
  policy.
- Types disappear at runtime. Load type-system material for `.ts`, `.tsx`, and
  checked JavaScript; load runtime, browser, process, and packaging material
  for any JavaScript file, including `.js`, `.jsx`, `.mjs`, and `.cjs`.
- Load the smallest useful pair: one language skill plus at most one runtime,
  domain, architecture, or assurance skill.
- Read `tsconfig*.json` and `package.json` before advising. The strictness
  posture, module settings, and TypeScript line decide what is good advice.
- Use `leta` for navigation and refactors and `grepai` for semantic search.
- When a fix needs `any`, a non-null assertion, `@ts-expect-error`, an unbounded
  `Promise.all`, or a `setTimeout` to "let things settle", re-check the design
  before keeping the patch.

## Opening questions

1. Where does this code execute: browser main thread, Web Worker, Node or Bun
   process, worker thread, Electron main, renderer, or preload, or a durable
   external worker?
2. Is this source application code, a public package, generated code, build
   tooling, or a protocol shared across processes?
3. Is the problem about correctness, responsiveness, throughput, durability,
   API shape, packaging, or evidence?
4. Which boundary owns cancellation, failure, validation, and shutdown?

Answer these before opening a skill. The first two pick the runtime or
architecture companion; the third picks the language or assurance skill; the
fourth decides where the fix belongs.

## Route by question

- Narrowing, generics, overloads, variance, branded types, exhaustive unions,
  `unknown` versus `any`, assertions, `satisfies`, suppression discipline, or
  how strict a greenfield or brownfield `tsconfig` should be:
  `typescript-types-and-apis`
- Runtime data shapes, identity, absence versus `undefined` versus `null`,
  immutable updates, discriminated state machines, deterministic transitions,
  serializable state, or model versus transport types:
  `typescript-data-and-state`
- HTTP, JSON, environment, CLI arguments, storage, IPC messages, worker
  messages, plugins, native bindings, generated clients, schema validation, or
  where a trust boundary belongs: `typescript-boundaries-and-validation`
- Thrown errors versus explicit outcomes, `unknown` catches, error causes,
  cancellation versus timeout versus failure, cross-process error
  serialization, or who logs: `typescript-errors-and-outcomes`
- Promise ownership, structured lifetime, `AbortSignal`, bounded fan-out,
  backpressure, event-loop scheduling, Web Workers, worker threads, pools, or
  the line between a logical worker and a thread:
  `typescript-async-and-concurrency`
- ESM and CJS, module resolution, `exports` maps, declaration emit, `.ts`
  import behaviour, dual packages, packed-artifact testing, code generation,
  `publint`, or `attw`: `typescript-modules-and-packaging`
- Zod 4 schemas, the Zod 3 migration, `zod/mini`, codecs, or JSON Schema
  output, once a boundary has been placed: `zod4-typescript`
- A codebase that already uses Effect: services, layers, `Schema`, typed
  errors, fibers, or the v3 to v4 renames: `effect-v4`
- Interaction latency, dropped frames, long tasks, layout thrashing, CSS versus
  JavaScript for presentation, yielding, or whether to offload to a Web Worker:
  `browser-main-thread-performance`
- Component state and effect ownership, derived state, controlled APIs,
  transitions, accessible interaction, localization, or component tests:
  `react-and-accessible-ui`
- Process lifecycle, signals and shutdown, streams, child processes, worker
  threads, native modules, CLI behaviour, or Node versus Bun differences:
  `node-bun-and-processes`
- Electron main, renderer, and preload separation, context isolation, typed
  IPC, privileged commands, native add-ons, or renderer scheduling:
  `electron-and-ipc`
- Public surface, dependency direction, package layering, shared protocol
  packages, plugin APIs, or compatibility promises:
  `arch-typescript-package-design`
- Named examples, tables, compile-time type tests, component tests,
  integration tests, end-to-end runs, virtual time, or runner choice:
  `typescript-testing`
- Choosing between ordinary tests, compile-time type tests, properties,
  stateful or race exploration, mutation testing, and proof:
  `typescript-verification`; deep dives in `fast-check` and `lemmascript`
- Which tool should own a static concern across the compiler, Biome, Oxlint
  and the shared `df12-lints` plugin, Stylelint, Semgrep, package checks, and
  accessibility checks, or what static analysis must not pretend to know:
  `typescript-quality-tools`; Biome configuration, migration, and rule
  semantics in `biome-typescript`
- Upgrading from TypeScript 6 to 7, removed options, side-by-side checking,
  compiler-output comparison, or a tool that still needs the 6.0 programmatic
  API: `typescript-7-transition`

## Testing hierarchy

This is a decision hierarchy, not a prestige ranking. Pick the first rung whose
evidence matches the question, and stop there.

0. **The type system**: make the illegal state unrepresentable, and pin a
   public vocabulary with a compile-time test. Route to
   `typescript-types-and-apis`, then `typescript-testing`.
1. **Named example**: one scenario, boundary, regression, rendered output, or
   error contract matters. Use `typescript-testing`.
2. **Table**: a finite truth table where each row means something, such as a
   transition table. Use `typescript-testing`.
3. **Lightweight property**: one relation over many cheap generated inputs.
   Use `fast-check` directly; no selector ceremony is needed.
4. **Model-based or scheduled property**: operation sequences, dependent
   data, or async interleavings. Stay with `fast-check`.
5. **Proof**: a load-bearing property that must hold for every input in a
   supported pure subset. Go through `typescript-verification` to `lemmascript`.

Mutation testing sits beside the hierarchy: load `typescript-verification` when
the question is whether the suite would notice a defect. Leave the hierarchy
for rendering, integration, accessibility, timing, and package consumers;
`typescript-testing` names the specialist test for each.

## Pairing rules

- Boundary work pairs `typescript-boundaries-and-validation` with
  `typescript-errors-and-outcomes`; the first decides what is accepted, the
  second decides what happens when it is not.
- State-machine work pairs `typescript-data-and-state` with
  `typescript-types-and-apis` only when the public type vocabulary is itself
  the deliverable.
- Async work at a process or worker edge pairs
  `typescript-async-and-concurrency` with `typescript-errors-and-outcomes`.
- Publishing work pairs `typescript-modules-and-packaging` with
  `typescript-types-and-apis` when declaration shape is the problem.
- Browser responsiveness pairs `browser-main-thread-performance` with
  `typescript-async-and-concurrency` for backpressure and the worker threshold,
  or with `react-and-accessible-ui` when the fix is inside a component.
- Electron work pairs `electron-and-ipc` with
  `typescript-boundaries-and-validation` for a new privileged command, or with
  `browser-main-thread-performance` for renderer frames.
- Server and CLI work pairs `node-bun-and-processes` with
  `typescript-async-and-concurrency` or `typescript-errors-and-outcomes`.
- Library architecture pairs `arch-typescript-package-design` with
  `typescript-modules-and-packaging`; the first decides what, the second how.
- A clear lightweight invariant goes straight to `fast-check`. Load
  `typescript-verification` when the rung or the escalation path is unclear,
  then choose one primary adversary.
- A proof pairs `lemmascript` with `fast-check` for the regression net beneath
  it and for the boundary code the proof trusts.
- Turning a settled policy into a rule pairs `typescript-quality-tools` with
  the skill that owns the policy, most often `browser-main-thread-performance`.
- A compiler upgrade pairs `typescript-7-transition` with
  `typescript-types-and-apis` when the new `strict` default meets brownfield
  directories, or with `typescript-modules-and-packaging` when `module` and
  `moduleResolution` need replacing.
- If two language skills both seem necessary, load the one that explains the
  failure and keep the other in reserve.

## Escalate when

- a type error is silenced with `any`, `as`, `!`, or `@ts-expect-error` without
  a comment naming the invariant the checker cannot see,
- a `tsconfig` is made stricter or looser wholesale instead of per directory
  with a stated ratchet,
- a `catch` block swallows `unknown` without classifying it,
- a promise is created that nobody awaits, cancels, or bounds,
- a package's `exports` map is edited without a consumer check,
- a boundary accepts a parsed shape without a schema or a hand-written guard,
- a table keeps growing rows to sample one invariant,
- a passing suite gives no evidence that its assertions detect wrong
  behaviour,
- a lint rule is asked to decide something only a trace can show,
- `ignoreDeprecations` is treated as an upgrade.

Read [routing-matrix.md](references/routing-matrix.md) only when the route is
still unclear.
