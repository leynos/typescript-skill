# Users' guide

This guide covers installation, invocation, the routing rules, and when to
reach for the assurance and tooling skills.

## Installation

Copy the catalogue under the agent's skill directory:

```bash
mkdir -p ~/.codex/skills
cp -a skills/* ~/.codex/skills/
```

The same layout works for `~/.claude/skills`. Each `skills/<name>/` directory
carries a `SKILL.md`, a `references/` directory, and (for every skill but the
router) an `agents/openai.yaml` that opts it out of implicit invocation. A
strict loader discovers a skill by its directory and identifies it by the
manifest `name`; the two always match in a checkout that has passed
`make check`.

A few skills link upward out of `skills/`: five point at the compiled fixtures
under `examples/`, and three references cite `docs/source-inventory.md`. Those
are evidence links. The skill states the claim in its own text and the link
shows where the gate proves it; nothing routes through them at runtime, so a
copied installation loses nothing but the proof. To keep the links live,
install from a checkout instead of copying:

```bash
git clone https://github.com/leynos/typescript-skill.git ~/src/typescript-skill
ln -s ~/src/typescript-skill/skills/* ~/.codex/skills/
```

`tests/test_reference_links.py` keeps upward links confined to `examples/` and
`docs/`, so the set of directories an installation may lack stays those two.

## Invocation

The router is the entry point:

```text
Use $typescript-router to route this task, then help me make the IPC
handler for "shell:run" validate its arguments.
```

The router asks four questions (where the code executes, what role it plays,
which quality is unhealthy, and which boundary owns lifecycle) and resolves to
one skill plus, usually, one companion. Each skill loads only its own
`SKILL.md` until a reference is needed.

When the pressure is already known, call the skill directly:

```text
Use $typescript-async-and-concurrency to review this fan-out for
unbounded concurrency and missing cancellation.
```

## Routing rules

The language spine owns the questions that are about the code itself:

- *Type modelling, strictness posture, suppression discipline* →
  `typescript-types-and-apis`.
- *Runtime values, absence, identity, state transitions, serialization* →
  `typescript-data-and-state`.
- *Data arriving from outside typed code* →
  `typescript-boundaries-and-validation`; Zod questions go on to
  `zod4-typescript`.
- *What happens when something fails* → `typescript-errors-and-outcomes`;
  Effect codebases go on to `effect-v4`.
- *Who owns async work, how many run at once, which thread* →
  `typescript-async-and-concurrency`.
- *How code is resolved, built, and consumed* →
  `typescript-modules-and-packaging`.

The runtime and architecture skills own the questions that are about where code
runs and what it is:

- *Interaction latency, frames, long tasks, CSS versus script, worker offload*
  → `browser-main-thread-performance`.
- *Component ownership, effects, accessibility, localization, component
  tests* → `react-and-accessible-ui`.
- *Process lifecycle, signals, streams, child processes, CLI contract, Node
  versus Bun* → `node-bun-and-processes`.
- *Electron privilege separation, typed IPC, native add-ons, renderer
  scheduling* → `electron-and-ipc`.
- *Public surface, layering, shared protocol packages, plugins,
  compatibility* → `arch-typescript-package-design`.

The assurance and tooling skills own evidence and enforcement:

- *Which test to write and at what level* → `typescript-testing`.
- *Cheap invariant over many inputs* → `fast-check` directly.
- *Choosing between tests, type tests, properties, stateful or race
  exploration, mutation testing, and proof* → `typescript-verification`, then
  `fast-check` or `lemmascript`.
- *Which tool owns a static concern; what no linter may claim* →
  `typescript-quality-tools`; Biome itself → `biome-typescript`.
- *Upgrading from TypeScript 6 to 7, removed options, a tool that needs the
  6.0 API* → `typescript-7-transition`.

Pairing rules:

- Boundary work pairs boundaries with errors: what is accepted, then what
  happens when it is not.
- Async work at a process or worker edge pairs async with errors.
- Publishing work pairs modules and packaging with types and APIs when
  declaration shape is the problem.
- Browser responsiveness pairs the browser skill with async for backpressure,
  or with React when the fix is inside a component.
- Electron work pairs with boundaries for a new privileged command.
- A clear invariant goes straight to `fast-check`; `typescript-verification`
  chooses when the rung is unclear.
- Two language skills are never both primary. Load the one that explains the
  failure.

## Strictness postures

The catalogue serves both greenfield and brownfield code. A greenfield project
takes the full switch set from the first commit; a brownfield project ratchets
one switch at a time per directory and never relaxes the base. The types skill
carries the order and the measurements. The example gate's own `tsconfig`
models the greenfield posture.

## Testing hierarchy

Pick the first rung whose evidence matches the question:

0. **The type system**, with a compile-time test for a public vocabulary.
1. **Named example**: one scenario, regression, or error contract.
2. **Table**: a finite truth table where each row means something.
3. **Lightweight property**: one relation over many cheap inputs.
4. **Model-based or scheduled property**: operation sequences or
   interleavings.
5. **Proof**: a load-bearing property over every input in a pure kernel.

Mutation testing sits beside the hierarchy. Rendering, integration,
accessibility, timing, and package consumers leave it for specialist tests.

## When to reach for the TypeScript 7 skill

`typescript-7-transition` is version-pinned and review-dated. Load it when a
project upgrades, when `tsc` rejects an option the previous compiler accepted,
or when a tool that imports `typescript` as a library breaks. It names the new
defaults, the removed options, the npm-alias recipes for running both
compilers, and the estate's three transition states. Everyday type questions on
a project already on 7 go to the evergreen skills.

## Imported deep dives

Some skills were written elsewhere and imported with their content intact:

- `zod4-typescript` for Zod 4 schemas, migration from Zod 3, and JSON Schema
  output. Reached from `typescript-boundaries-and-validation`.
- `effect-v4` for Effect 4.x services, layers, schemas, and the v3 to v4
  renames. Reached from `typescript-errors-and-outcomes`. It carries two helper
  scripts, `has_export.py` and `check_v3_patterns.py`, that check an installed
  Effect against the skill's rename tables.
- `fast-check` and `lemmascript`, the verification deep dives, reached from
  `typescript-verification`. This catalogue is their canonical home
  ([ADR 0001](adr/0001-verification-skill-ownership.md)).
- `biome-typescript` for Biome configuration, migration, and rule semantics,
  reached from `typescript-quality-tools`.

They keep their original voice and spelling; see
[ADR 0003](adr/0003-imported-skill-provenance.md).

## Common pitfalls

- Loading two language skills in one turn. Pick the one whose decision
  surface dominates and keep the other in reserve.
- Reading a type annotation as a guarantee about data that arrived through
  `JSON.parse`, `postMessage`, or `process.env`. The boundary skill owns that.
- Treating a logical orchestration "worker" as evidence that a thread is
  needed. The async skill's vocabulary reference keeps the terms apart.
- Flipping a whole `tsconfig` to strict on an inherited codebase. The ratchet
  is per directory and measured.

## Extending the catalogue

Keep new material under `skills/`. Match the shape of the existing skills: YAML
frontmatter with a `globs` hint, a working stance, a decision surface, red
flags, pairing, and references for longer detail. Name the skill in the router,
the routing matrix, and the catalogue status; the contract suite will tell you
if you miss one. Record structural rationale in
[the design principles](design-principles.md) or an ADR.
