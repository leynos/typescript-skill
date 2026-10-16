# Users' guide

This guide covers installation, invocation, the routing rules, and when to
reach for the assurance and tooling skills.

## Installation

Copy the catalogue under the agent's skill directory:

```bash
mkdir -p ~/.codex/skills
cp -a skills/* ~/.codex/skills/
```

The same layout works for `~/.claude/skills`. The catalogue is self-contained:
each `skills/<name>/` directory carries a `SKILL.md`, a `references/`
directory, and (for every skill but the router) an `agents/openai.yaml` that
opts it out of implicit invocation. A strict loader discovers a skill by its
directory and identifies it by the manifest `name`; the two always match in a
checkout that has passed `make check`.

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

Pairing rules:

- Boundary work pairs boundaries with errors: what is accepted, then what
  happens when it is not.
- Async work at a process or worker edge pairs async with errors.
- Publishing work pairs modules and packaging with types and APIs when
  declaration shape is the problem.
- Two language skills are never both primary. Load the one that explains the
  failure.

## Strictness postures

The catalogue serves both greenfield and brownfield code. A greenfield project
takes the full switch set from the first commit; a brownfield project ratchets
one switch at a time per directory and never relaxes the base. The types skill
carries the order and the measurements. The example gate's own `tsconfig`
models the greenfield posture.

## Imported deep dives

Some skills were written elsewhere and imported with their content intact:

- `zod4-typescript` for Zod 4 schemas, migration from Zod 3, and JSON Schema
  output. Reached from `typescript-boundaries-and-validation`.
- `effect-v4` for Effect 4.x services, layers, schemas, and the v3 to v4
  renames. Reached from `typescript-errors-and-outcomes`. It carries two helper
  scripts, `has_export.py` and `check_v3_patterns.py`, that check an installed
  Effect against the skill's rename tables.

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
