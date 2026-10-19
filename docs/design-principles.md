# Design principles

- **Status:** Living document, describing the implemented catalogue.
- **Scope:** Why the catalogue has the shape it has, what it inherits from the
  Rust, Python, and ReScript catalogues, and what it deliberately does
  differently.
- **Precedence:** [AGENTS.md](../AGENTS.md) holds the binding rules for
  changes; [the source inventory](source-inventory.md) is the record of what
  the estate actually contains. This document explains the reasoning.

## 1. Problem

Coding agents write TypeScript from memory, and most of what they remember is
either generic tutorial material or advice tuned to one framework. Neither
answers the questions that are actually hard in a working estate: where does
this code execute, which boundary owns validation and cancellation, how strict
can an inherited codebase honestly be, what evidence does a claim need, and
which tool should enforce a rule. A single omnibus "TypeScript skill" would
either be too long to load or too shallow to help.

The catalogue therefore routes. One small router asks four questions and loads
one skill plus, usually, one companion. Each skill carries judgement; its
references carry recipes; executable tools carry policy.

## 2. Inheritance

| Source                | What this catalogue takes from it                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rust-skill`          | A small router, focused language skills, separately routed runtime and architecture skills, and verification specialists behind a selector.                                                   |
| `python-skill`        | Executable catalogue-contract tests in pytest, an explicit catalogue status document, and version-pinned skills for volatile tooling (`ruff-016` is the model for `typescript-7-transition`). |
| `rescript-skill`      | A line budget for `SKILL.md`, every reference linked from its skill, and executable examples compiled by the gate.                                                                            |
| The TypeScript estate | Browser, Node and Bun, published packages, and Electron treated as distinct execution environments rather than varieties of React.                                                            |

_Table 1: The three model catalogues and the estate, and what each contributed._

## 3. Governing principles

### 3.1. Route by pressure, not by brand

The router asks what is difficult: type modelling, untrusted input,
asynchronous ownership, packaging, frame responsiveness, IPC privilege,
evidence, or lint policy. "This project uses React" is context. The React skill
exists, but it is reached because state ownership or accessible interaction is
the pressure, not because `react` appears in `package.json`.

### 3.2. Model runtime and static semantics separately

Types disappear at runtime. The router's globs include `.js`, `.jsx`, `.mjs`,
and `.cjs` because event-loop, browser, packaging, and process guidance applies
to every JavaScript file. Type-system material triggers on TypeScript and
checked JavaScript only. A skill that conflates the two will tell someone that
a type annotation protects them from a `postMessage` payload.

### 3.3. Load the smallest useful pair

The normal route is one language skill plus at most one runtime, domain,
architecture, or assurance skill. The router states this cap and the contract
tests check that it still does. Loading half the catalogue at once drowns the
work in guidance.

### 3.4. Skills encode judgement; references encode recipes; tools encode policy

`df12-lints` remains the executable source of truth for house lint rules. The
catalogue explains why a rule exists, its exceptions, and when static analysis
is insufficient. `typescript-quality-tools` assigns an owner to each static
concern rather than restating rule lists.

### 3.5. Support greenfield and brownfield operation

The estate has both. Two mockups and two simulators run the sharpest strictness
switches; the Electron terminal relaxes most of them for its inherited
directories and runs its gate through the relaxed configuration.
`typescript-types-and-apis` therefore carries a strictness ratchet, and the
routing scenarios include "introduce exact optional properties into an old
codebase" with the expectation that the answer is a per-directory plan, not a
replacement `tsconfig`.

### 3.6. Treat execution environments as distinct

Browser main thread, Web Worker, Node or Bun process, worker thread, Electron
main, renderer, and preload, and durable external workers each have a skill or
a section that owns them. The vocabulary reference in the async skill keeps an
event-loop task, an application scheduler, a logical orchestration worker, a
Web Worker, a worker thread, a process, and a durable job apart, because the
estate already has a design that calls an orchestration loop a "worker" and
nothing about it needs a thread.

### 3.7. Version-specific claims live in versioned material

TypeScript 7 shipped as the native compiler without a stable programmatic API,
while the estate still runs TypeScript 5.4, 5.9, 6.0, and a January native
preview. That fault line belongs in `typescript-7-transition`, which names the
release it describes and the date it was checked. A contract test fails if a
compiler-version claim appears in an evergreen skill.

### 3.8. Evidence over recollection

Every behavioural claim about the compiler is backed by a fixture under
`examples/` that the gate compiles under the pinned TypeScript release.
Diagnostics fixtures use `@ts-expect-error`, so a marker with no error beneath
it fails the build. Claims about the estate point at files in
[the source inventory](source-inventory.md). Claims about third-party libraries
name the version checked.

## 4. Catalogue architecture

### 4.1. Groups

- **Router:** `typescript-router`.
- **Language spine:** types and APIs, data and state, boundaries and
  validation, errors and outcomes, async and concurrency, modules and packaging.
- **Runtime and architecture:** browser main-thread performance, React and
  accessible UI, Node and Bun processes, Electron and IPC, package design.
- **Assurance and tools:** testing, verification, quality tools, and the
  TypeScript 7 transition.
- **Imported deep dives:** `fast-check`, `lemmascript`, `zod4-typescript`,
  `biome-typescript`, and `effect-v4`, each with one owning skill inside the
  catalogue.

[The catalogue status](skill-catalogue-status.md) lists them with their
references.

### 4.2. Why data and state is separate from types and APIs

Deterministic transition models, entity and command vocabularies, React state,
and a shared IPC protocol all involve runtime state semantics: absence,
identity, immutability, serialization, and transitions. Those are decisions
about values, not about typings, and an agent asked about them should not be
handed a generics tutorial.

### 4.3. Why Electron has its own skill

The estate's terminal has a main process, a renderer, a shared protocol
package, typed IPC contracts validated with zod on one side, native modules,
PTY batching, frame timing, and no context isolation yet. That is enough
distinct material, and enough live risk, for a skill rather than a section of
the browser or Node skill.

### 4.4. Why the deep dives are imported rather than rewritten

`fast-check` and `lemmascript` were written for the TypeScript verification
work and merged elsewhere before this catalogue existed. Rewriting them would
create two divergent copies. They are moved here with their names kept, and
[ADR 0001](adr/0001-verification-skill-ownership.md) records that this
catalogue is now their canonical home. The same applies to the Zod, Biome, and
Effect skills; [ADR 0003](adr/0003-imported-skill-provenance.md) records their
provenance.

## 5. Evidence model

For screen readers: the diagram shows a claim in a skill backed by one of three
kinds of evidence, each re-checked by a gate.

```plaintext
claim in SKILL.md or a reference
  ├── TypeScript fixture (examples/positive, examples/diagnostics) ── make examples
  ├── estate fact (docs/source-inventory.md, file path named) ──────── review
  └── routing decision (router, matrix, scenarios) ──────────────────── make test
```

_Figure 1: How a claim in the catalogue is backed and re-checked._

## 6. Rejected alternatives

| Alternative                                   | Reason rejected                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| One omnibus TypeScript skill                  | Too long to load and too shallow to help; routing is the point.                                        |
| Framework-first skills (React, Next, Express) | Routes by brand; the hard questions cut across frameworks.                                             |
| Rewriting the verification deep dives         | Two live copies would diverge; move them and record the ownership.                                     |
| Evergreen TypeScript 7 guidance               | The fault line moves; a review-dated specialist is honest about its shelf life.                        |
| A spelling gate over imported skills          | Imported material is American-spelled; rewriting it is churn, excluding it weakens the gate. Deferred. |
| Scraping every fenced example into the gate   | Many examples are deliberately broken; the gate compiles named fixtures only.                          |
| Dogfooding TypeScript for the contract tests  | The subject under test is Markdown; pytest is already the estate's structural-test tool.               |

_Table 2: Alternatives considered and why they were rejected._

## 7. Risks and evolution

- **Version drift.** `typescript-7-transition` names TypeScript 7.0.2 and the
  tool gaps as of its review date. When 7.1 ships a programmatic API, the skill
  needs a new review date and probably a new name.
- **Imported skill drift.** The deep dives pin library versions (fast-check
  4.x, LemmaScript 0.5.x, Zod 4.3.x, Biome 2.x, Effect 4.0.x). Each has a
  maintenance note in the catalogue status.
- **Policy not yet executable.** `prefer-css-state` and the Stylelint
  animation rule are described, not shipped. Until `df12-lints` carries them,
  the quality-tools skill is advice rather than enforcement.
- **Estate assumptions.** The source inventory is dated. Re-read it before
  citing an estate fact in a skill.
