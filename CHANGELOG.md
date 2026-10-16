# Changelog

All notable changes to this project are documented in this file. The format
follows [Common Changelog](https://common-changelog.org/).

## Unreleased

### Added

- The catalogue spine: `typescript-router` with its routing matrix, the
  contract test suite, the TypeScript example gate under `examples/`, and the
  catalogue documents (`docs/skill-catalogue-status.md`,
  `docs/design-principles.md`, `docs/source-inventory.md`).
- The language core: `typescript-types-and-apis`, `typescript-data-and-state`,
  `typescript-boundaries-and-validation`, `typescript-errors-and-outcomes`,
  `typescript-async-and-concurrency`, and `typescript-modules-and-packaging`.
- The runtime and architecture skills: `browser-main-thread-performance`,
  `react-and-accessible-ui`, `node-bun-and-processes`, `electron-and-ipc`, and
  `arch-typescript-package-design`, with fixtures for a yielding scheduler and
  a typed IPC registry.
- The assurance layer: `typescript-testing` with the testing hierarchy and a
  compile-time type-test fixture, and `typescript-verification` as the
  question-first selector.
- Imported verification deep dives `fast-check` and `lemmascript`, now owned
  by `typescript-verification`
  ([ADR 0001](docs/adr/0001-verification-skill-ownership.md)).
- `typescript-quality-tools`, assigning one owner per static concern and
  specifying the `prefer-css-state` rule and browser preset for `df12-lints`,
  and `typescript-7-transition`, version-pinned to TypeScript 7.0.2
  ([ADR 0002](docs/adr/0002-typescript-7-versioned-boundary.md)).
- Imported deep dive `biome-typescript`, owned by `typescript-quality-tools`.
- Imported deep dives `zod4-typescript` and `effect-v4`, with manifests
  adapted to the catalogue's contract
  ([ADR 0003](docs/adr/0003-imported-skill-provenance.md)).
- `docs/routing-scenarios.md`, the router's evaluation set, with its contract
  test pinning the six design scenarios.
- Architecture decision records for verification ownership, the TypeScript 7
  versioned boundary, and imported-skill provenance.
