# The programmatic API gap

Reviewed 2026-10-16 against TypeScript 7.0.2's published package.

## What 7.0 ships

- `tsc`, the compiler command, as `bin/tsc` (a Node launcher that runs the
  native binary from a platform-specific optional dependency such as
  `@typescript/typescript-linux-x64`).
- A language server, LSP-native and multithreaded.
- `typescript/unstable/sync`, `typescript/unstable/async`,
  `typescript/unstable/fs`, `typescript/unstable/proto`, and
  `typescript/unstable/ast` with `ast/is`, `ast/factory`, `ast/utils`,
  `ast/scanner`, `ast/visitor`, and `ast/clone` subpaths. These are the seeds
  of the 7.1 API, explicitly unstable, and not shaped like the 6.0 API.
- The main entry (`import ts from "typescript"`) resolves to a version module,
  not the compiler API.

## What it does not ship

The 6.0 programmatic API: `ts.createProgram`, `ts.transpileModule`, the
`TypeChecker`, transformers, `ts.sys`, the language service factory. Every tool
built on it fails to import or fails at runtime under 7.0.

## Tools affected

| Tool class                              | Examples                                        | Posture                                                                      |
| --------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- |
| Embedded language services              | Vue (Volar), Svelte, Astro, MDX                 | Stay on 6.0 for the editor; 7.0 `tsc` for project checks                     |
| Framework template checking             | Angular                                         | Angular uses 7.0 `tsc` for whole-project checks and 6.0 in the editor        |
| Type-aware lint                         | `typescript-eslint`                             | Needs 6.0 as its `typescript` peer                                           |
| Declaration bundlers and API extractors | tsup `--dts`, rollup dts plugins, API Extractor | Need 6.0; or use `tsc --declaration` from 7.0 and bundle separately          |
| AST manipulation                        | `ts-morph`, codemods                            | Need 6.0, or port to `typescript/unstable/ast` with the instability accepted |
| Schema and documentation generators     | `typescript-json-schema`, TypeDoc               | Need 6.0 until they release against 7.1                                      |
| Build tools that transpile only         | esbuild, swc, Bun, Vite                         | Unaffected; they never used the API                                          |
| Test runners                            | Vitest, `bun test`, Jest with a transpiler      | Unaffected unless type-checking through the API                              |

_Table 1: Tool classes and how each is affected by the missing API._

## Decision

- If no dependency imports `typescript`, move the whole project to 7.0.
- If one does, keep 6.0 beside 7.0 by alias, run the gate on 7.0 `tsc`, and
  track each blocked tool's 7.1 release.
- Do not port a project tool to `typescript/unstable/*` for a one-off script;
  the API may change in a patch. Port when the tool's maintenance life is long
  enough to absorb that, and pin the exact TypeScript version.
- Expect 7.1 to ship the new API; when it does, this page and the tool table
  need a new review date.

## In the estate

One repository runs a package-boundary checker that imports `typescript` and a
schema generator that depends on it; both need 6.0 while its `tsc` moves to
7.0. The two front ends use Vite and need no API. The two simulators use
graphql-codegen and tsdown with `dts`; tsdown's declaration path should be
checked against 7.0 before switching.
