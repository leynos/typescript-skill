# typescript-skill

*A TypeScript skill catalogue for coding agents, about choosing the right
execution context, boundary, evidence, and enforcement mechanism for JavaScript
that happens to be engineered with TypeScript.*

This repository carries a router, a language spine, runtime and architecture
skills for the browser, React, Node and Bun, Electron, and published packages,
an assurance layer with a question-first verification selector, and
version-pinned specialists for volatile tooling. It is modelled on the
[`rust-skill`](https://github.com/leynos/rust-skill),
[`python-skill`](https://github.com/leynos/python-skill), and `rescript-skill`
catalogues.

______________________________________________________________________

## Why typescript-skill?

- **Route by pressure, not by brand.** The router asks where code executes,
  what role it plays, which quality is unhealthy, and which boundary owns
  lifecycle. "This project uses React" is context, not a diagnosis.
- **Runtime and static semantics kept apart.** Types disappear at runtime; the
  catalogue triggers on `.js` and `.mjs` wherever event-loop, browser, or
  packaging guidance applies, and keeps type material for TypeScript.
- **Smallest useful pair.** One language skill plus at most one companion.
- **Greenfield and brownfield.** A strictness ratchet for inherited code, not a
  replacement `tsconfig` from orbit.
- **Evidence.** Compiler claims are backed by fixtures the gate compiles under
  the pinned TypeScript release; estate claims point at files.

______________________________________________________________________

## Quick start

### Installation

```bash
mkdir -p ~/.codex/skills
cp -a skills/* ~/.codex/skills/
```

### Basic usage

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

## Learn more

- [Users' guide](docs/users-guide.md): installation, invocation, routing.
- [Developers' guide](docs/developers-guide.md): the gates and the contract
  suite.
- [Skill catalogue status](docs/skill-catalogue-status.md): what is active,
  what is imported, and what to maintain.
- [Design principles](docs/design-principles.md): why the catalogue has this
  shape.
- [Source inventory](docs/source-inventory.md): what the six estate
  repositories actually contain.
- [TypeScript router](skills/typescript-router/SKILL.md): the entry point.

______________________________________________________________________

## Development

Run the gates through the `Makefile`:

| Target           | What it does                       |
| ---------------- | ---------------------------------- |
| `make fmt`       | Format Python and Markdown         |
| `make check-fmt` | Formatting gate                    |
| `make lint`      | Markdown, Mermaid, manifests, Ruff |
| `make typecheck` | Strict mypy over the tests         |
| `make examples`  | Compile the TypeScript fixtures    |
| `make test`      | Run the pytest contract suite      |
| `make check`     | Default goal; the full commit gate |

`uv`, `bun`, `markdownlint-cli2`, `nixie`, and `mdtablefix` 0.6.1 or later must
be on `PATH`. Read [AGENTS.md](AGENTS.md) before changing tracked files.

______________________________________________________________________

## Acknowledgements

The verification deep dives (`fast-check`, `lemmascript`) and the Zod and Biome
skills were written in `agent-helper-scripts` and moved here; the Effect skill
was built from the Effect team's own agent guidance and migration material
under the MIT licence. The browser performance skill takes its decision
sequence from Lee Sun-Hyoup's essay on the expensive main thread and from
Chrome's scheduling guidance.

______________________________________________________________________

## Licence

ISC. See [LICENSE](LICENSE).
