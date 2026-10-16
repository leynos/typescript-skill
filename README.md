# 🧭 typescript-skill

*A technical lead in a box for JavaScript that happens to be written in
TypeScript.*

A skill catalogue for coding agents. One small router asks where the code runs,
what it is, which number is unhealthy, and who owns the lifecycle, then loads
one focused skill and, usually, one companion. The catalogue is about choosing
the right execution context, boundary, evidence, and enforcement mechanism, not
about how to spell a generic.

______________________________________________________________________

## Why typescript-skill?

Agents write TypeScript from memory, and memory is either tutorial material or
advice tuned to one framework. Neither answers the questions that are hard in a
real estate:

- **Route by pressure, not by brand.** "This project uses React" is context.
  The diagnosis is type modelling, untrusted input, asynchronous ownership,
  packaging, frame budgets, IPC privilege, evidence, or lint policy.
- **Runtime and static semantics kept apart.** Types disappear at runtime. The
  catalogue triggers on `.js` and `.mjs` wherever event-loop, browser, or
  packaging guidance applies, and keeps type material for TypeScript.
- **Smallest useful pair.** One language skill plus at most one companion,
  never a wagon train of vaguely relevant Markdown.
- **Greenfield and brownfield.** A strictness ratchet for inherited code,
  rather than a replacement `tsconfig` fired from orbit.
- **Evidence over recollection.** Compiler claims are backed by fixtures the
  gate compiles under the pinned TypeScript release; estate claims point at
  files; volatile facts carry a review date.

______________________________________________________________________

## Quick start

### Installation

```bash
mkdir -p ~/.codex/skills
cp -a skills/* ~/.codex/skills/
```

The same layout works for `~/.claude/skills`.

### Basic usage

Ask the router first:

```text
Use $typescript-router to route this task, then help me bound the
concurrency of this import job and make it cancellable.
```

When the pressure point is already known, call the skill directly:

```text
Use $typescript-modules-and-packaging to make this package's exports map
pass publint and attw for both ESM and CJS consumers.
```

______________________________________________________________________

## Features

- A router with four opening questions, a routing matrix, and a testing
  hierarchy from the type system to proof.
- A language spine: types and APIs, data and state, boundaries and validation,
  errors and outcomes, async and concurrency, modules and packaging.
- Runtime and architecture skills for the browser main thread, React and
  accessible UI, Node and Bun processes, Electron and IPC, and package design.
- An assurance layer: a testing skill, a question-first verification selector,
  and the `fast-check` and `lemmascript` deep dives it owns.
- Quality tooling with one owner per static concern, and a version-pinned
  TypeScript 7 transition skill that says when it was last checked.
- Imported deep dives for Zod 4, Biome, and Effect 4, content intact.
- A contract suite that keeps the router, the routing matrix, the status
  document, the fixtures, and the tree in agreement.

______________________________________________________________________

## Learn more

- [Users' guide](docs/users-guide.md) — installation, invocation, and
  routing.
- [Developers' guide](docs/developers-guide.md) — the gates, the contract
  suite, and the example gate.
- [Skill catalogue status](docs/skill-catalogue-status.md) — what is active,
  what is imported, and what to maintain.
- [Design principles](docs/design-principles.md) — why the catalogue has this
  shape, and what it rejected.
- [Routing scenarios](docs/routing-scenarios.md) — the router's evaluation
  set, drawn from the estate.
- [Source inventory](docs/source-inventory.md) — what the six estate
  repositories actually contain.
- [TypeScript router](skills/typescript-router/SKILL.md) — the entry point.

______________________________________________________________________

## Development

The catalogue is Markdown with a pytest contract suite and a Bun-driven
TypeScript example gate. `make check` is the default goal and the full commit
gate; `make fmt` rewrites files and is deliberately not part of it. `uv`, `bun`,
`markdownlint-cli2`, `nixie`, and `mdtablefix` 0.6.1 or later must be on
`PATH`. The [developers' guide](docs/developers-guide.md) covers each target
and what the tests enforce.

______________________________________________________________________

## Acknowledgements

Modelled on the [`rust-skill`](https://github.com/leynos/rust-skill),
[`python-skill`](https://github.com/leynos/python-skill), and `rescript-skill`
catalogues. The verification deep dives (`fast-check`, `lemmascript`) and the
Zod and Biome skills were written in `agent-helper-scripts` and moved here. The
Effect skill was built from the Effect team's own agent guidance and migration
material under the MIT licence. The browser performance skill takes its
decision sequence from Lee Sun-Hyoup's essay on the expensive main thread and
from Chrome's scheduling guidance.

______________________________________________________________________

## Licence

ISC — see [LICENSE](LICENSE) for details.

______________________________________________________________________

## Contributing

Contributions are welcome. Read [AGENTS.md](AGENTS.md) before changing tracked
files: it lists the commit gates and the rules for changes under `skills/`.
Keep new material short and judgement-shaped, push recipes into `references/`,
name every new skill in the router and the catalogue status, and let
`make check` tell you what you missed.
