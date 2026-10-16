# Skill catalogue status

Snapshot of what is active in `skills/`, where each imported skill came from,
and what to re-derive when the tooling moves. The example gate compiles under
TypeScript 7.0.2 with Bun 1.4.3.

## Active skills

### Router

- `typescript-router` — main entry point: the four opening questions, the
  route list, the testing hierarchy, pairing rules, and escalation. Line
  envelope: 200, because it names every skill. References: `routing-matrix.md`.

### Language spine

- `typescript-types-and-apis` — narrowing, generics, overloads, variance,
  branded types, exhaustive unions, `unknown` versus `any`, assertions,
  `satisfies`, suppression discipline, and the greenfield and brownfield
  strictness ratchet. References: `strictness-ratchet.md`,
  `narrowing-and-guards.md`, `generics-and-variance.md`,
  `suppression-discipline.md`. Fixture: `diagnostics/strictness-switches.ts`.
- `typescript-data-and-state` — absence versus `undefined` versus `null`,
  identity, immutable updates, discriminated state machines, deterministic
  transitions, serializable state, model versus transport. References:
  `absence-and-identity.md`, `state-machines.md`, `model-vs-transport.md`.
  Fixture: `positive/exhaustive-state.ts`.
- `typescript-boundaries-and-validation` — the boundary catalogue, parse not
  validate, schema library selection, environment and configuration, generated
  clients, IPC and worker messages, plugins and native bindings. References:
  `boundary-catalogue.md`, `schema-library-selection.md`,
  `generated-clients.md`.
- `typescript-errors-and-outcomes` — thrown versus returned, one error class
  with a `code`, causes, cancellation versus timeout versus failure, wire
  shapes for errors, logging ownership. References: `outcome-shapes.md`,
  `cancellation-timeout-failure.md`, `serializing-errors.md`.
- `typescript-async-and-concurrency` — promise ownership, scopes,
  `AbortSignal`, bounded fan-out, backpressure policies, yield versus batch,
  the off-thread threshold, the worker abstraction matrix, and the vocabulary
  that keeps a logical worker apart from a thread. References:
  `promise-ownership.md`, `bounded-concurrency-and-backpressure.md`,
  `workers-and-pools.md`, `vocabulary.md`.
- `typescript-modules-and-packaging` — module settings by project kind,
  `.ts` imports, `exports` maps, `development` conditions, dual packages and
  declarations, `publint`, `attw`, packed-install smoke tests, generated code
  ownership. References: `esm-cjs-and-exports.md`,
  `declarations-and-dual-packages.md`, `consumer-checks.md`,
  `generated-code.md`.

### Runtime and architecture

- `browser-main-thread-performance` — the decision sequence: state the
  objective, eliminate work, hand presentation to CSS, shape main-thread work,
  offload coarse CPU work, keep the vocabulary; the latency versus throughput
  trade; the three rings of enforcement. References:
  `objective-and-elimination.md`, `css-state-membrane.md`,
  `main-thread-shaping.md`. Fixture: `positive/yielding-scheduler.ts`.
- `react-and-accessible-ui` — state and effect ownership, derived state,
  external systems, controlled APIs, transitions, the CSS membrane inside
  components, accessible interaction, localization, component testing.
  References: `state-and-effect-ownership.md`, `transitions-and-scheduling.md`,
  `accessible-interaction-and-i18n.md`, `component-testing.md`.
- `node-bun-and-processes` — lifecycle and signals, draining, exit codes,
  streams and backpressure, child processes, worker threads, native modules,
  Node and Bun divergences, CLI contract. References:
  `process-lifecycle-and-signals.md`, `streams-and-child-processes.md`,
  `node-bun-compatibility.md`, `cli-behaviour.md`.
- `electron-and-ipc` — privilege separation and its migration, typed and
  validated IPC, privileged commands, cancellation across processes, protocol
  versioning, native add-ons, PTY batching, renderer scheduling, shutdown.
  References: `privilege-separation-migration.md`, `typed-ipc-protocol.md`,
  `native-modules-and-shutdown.md`, `renderer-scheduling.md`. Fixture:
  `positive/typed-ipc-registry.ts`.
- `arch-typescript-package-design` — public surface, dependency direction and
  layering, shared protocol packages, plugin and extension protocols,
  compatibility and stability tags. References: `public-surface.md`,
  `dependency-direction-and-layering.md`, `plugins-and-extension-protocols.md`,
  `compatibility.md`.

### Assurance

- `typescript-testing` — the testing hierarchy from the type system to proof,
  compile-time type tests, unit versus integration, virtual time and
  deterministic schedulers, component tests, end-to-end, benchmarks, runner
  choice. References: `testing-hierarchy.md`, `compile-time-type-tests.md`,
  `virtual-time-and-schedulers.md`, `integration-and-e2e.md`. Fixture:
  `diagnostics/type-contract.ts`.
- `typescript-verification` — the question-first selector between ordinary
  tests, compile-time tests, `fast-check` properties, stateful and race
  exploration, mutation testing, and LemmaScript proof; the layering rule; what
  none of them establish. References: `selection-matrix.md`,
  `mutation-testing.md`, `state-and-race-exploration.md`.

### Tools and transition

- `typescript-quality-tools` — one owner per static concern, the three rings
  of enforcement, the `prefer-css-state` proposal and its fixture policy,
  Stylelint and CSS policy, the Oxlint JS plugin facts as of a review date, and
  what must stay runtime evidence. References: `static-owners-matrix.md`,
  `prefer-css-state.md`, `stylelint-and-css-policy.md`, `oxlint-js-plugins.md`.
- `typescript-7-transition` — version-pinned to TypeScript 7.0.2 (reviewed
  2026-10-16): new defaults, removed options and replacements, semantic
  changes, side-by-side installation through npm aliases, the compare script,
  the programmatic API gap and the tools it blocks, and the estate's three
  transition states. References: `defaults-and-removed-options.md`,
  `side-by-side-and-aliases.md`, `programmatic-api-gap.md`,
  `estate-transition-states.md`.

### Imported deep dives

- `biome-typescript` — Biome configuration, file targeting, lint solutions,
  strict rules beyond recommended, ESLint and Prettier migration, CI and git
  hooks. Owner: `typescript-quality-tools`. Source: `agent-helper-scripts`
  `skills/biome-typescript` as of 2026-10-16. Line envelope: 400. References:
  `lint-solutions.md`, `strict-rules.md`, `migration.md`, `ci-hooks.md`.

- `fast-check` — arbitraries, the filtering trap, model-based testing, the
  scheduler for races, 4.x versus 3.x idioms, replay, CI tiering. Owner:
  `typescript-verification`. Source: `agent-helper-scripts` `skills/fast-check`
  (merged 2026-08-14, PR #25; copied 2026-10-16). Line envelope: 230.
  References: `arbitraries.md`, `model-based-testing.md`.
- `lemmascript` — `//@` annotations, the Dafny and Lean backends, the edit
  loop, trusted boundaries, brownfield strategy. Owner:
  `typescript-verification`. Source: `agent-helper-scripts`
  `skills/lemmascript` (merged 2026-08-14, PR #25; copied 2026-10-16). Line
  envelope: 230. References: `annotations.md`, `workflow.md`.

- `zod4-typescript` — Zod 4 schemas, parsing, errors, inference, the Zod 3
  migration traps, `zod/mini`, codecs, and JSON Schema. Owner:
  `typescript-boundaries-and-validation`. Source: `agent-helper-scripts`
  `skills/zod4-typescript` as of 2026-10-16. Line envelope: 540. References:
  `zod-mini-mapping.md`, `codec-recipes.md`, `json-schema-options.md`.
- `effect-v4` — Effect 4.x house style, the v3 reflexes that break, the
  package and import map, and the per-module rename tables. Owner:
  `typescript-errors-and-outcomes`. Source: `effect-v4.skill` bundle built
  2026-10-15 against `effect@4.0.5`, upstream material from `Effect-TS/effect`
  commit `5a67e0b3`. Line envelope: 260. References: `core.md`, `schema.md`,
  `streams.md`, `platform.md`, `testing.md`, `migration.md`,
  `renames/<module>.md`, `upstream/`. Scripts: `has_export.py`,
  `check_v3_patterns.py`.

## Documentation

- [Agent instructions](../AGENTS.md) — commit gates and the rules for changes
  under `skills/`.
- [README](../README.md) — installation and quick start.
- [Users' guide](users-guide.md) — invocation and routing.
- [Developers' guide](developers-guide.md) — gates, the contract suite, and
  the example gate.
- [Design principles](design-principles.md) — inheritance, governing
  principles, rejected alternatives.
- [Source inventory](source-inventory.md) — what the six estate repositories
  contain, dated.
- [Routing scenarios](routing-scenarios.md) — the router's evaluation set,
  with the six design scenarios pinned by the contract suite.
- [ADR 0001](adr/0001-verification-skill-ownership.md) — the verification
  deep dives move here and `typescript-verification` owns them.
- [ADR 0002](adr/0002-typescript-7-versioned-boundary.md) — why the
  TypeScript 7 material is version-pinned.
- [ADR 0003](adr/0003-imported-skill-provenance.md) — how imported skills are
  adapted and what is left alone.

## Maintenance

- **`typescript-7-transition`** is version-pinned material. Revisit it when
  TypeScript 7.1 ships its programmatic API: re-derive the blocked-tool table,
  the `typescript/unstable/*` subpath list, the removed-option list against the
  release notes, and the estate states against the source inventory. Set a new
  review date in the skill and its references.
- **`oxlint-js-plugins.md`** in `typescript-quality-tools` is review-dated
  (Oxlint 1.88.0, JS plugins alpha). Revise when the alpha label drops or a
  `RuleTester` equivalent appears.
- **`biome-typescript`** describes Biome 2.x; npm showed 2.5.15 on 2026-10-16.
  Recheck rule names against `biome rage` output at the next import.
- **Example gate.** `examples/package.json` pins TypeScript 7.0.2. Bump it
  with `typescript-7-transition`'s review date and re-run `make examples`.
- **`zod4-typescript`** describes Zod 4.3.x. Recheck the `zod/mini` mapping
  and the JSON Schema options when Zod 4.4 or 5 ships (npm showed 4.6.7 on
  2026-10-16; the skill's examples still apply but the "latest" line is stale).
- **`effect-v4`** describes `effect@4.0.5`. The rename tables are generated
  from upstream; regenerate from the bundle's source when a 4.x minor adds or
  removes modules. Its scripts assume Python 3 on `PATH`.
- **`fast-check`** describes 4.x (npm showed 4.10.2 on 2026-10-16) and
  **`lemmascript`** names 0.5.22 while npm showed 0.6.4. Recheck the
  LemmaScript CLI flags and supported fragment at the next import.
- **Worker abstraction versions** named in
  `typescript-async-and-concurrency/references/workers-and-pools.md` were
  checked on 2026-10-16 (Comlink 4.4.2, `workerpool` 10.0.3, Piscina 5.3.2).

## Open questions

- Whether to add a spelling gate. Imported skills are American-spelled;
  rewriting them is churn and excluding them weakens the gate. Deferred until
  the imported set is stable.
- Whether `effect-v4`'s Python scripts should move under the repository's
  Ruff scope. They are the skill's artefacts and ship with it; deferred.
