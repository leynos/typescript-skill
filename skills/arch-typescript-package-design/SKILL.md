---
name: arch-typescript-package-design
description: Use for TypeScript package architecture, including public surface design, dependency direction, package layering in a monorepo, generated-code ownership, plugin and extension protocols, compatibility and versioning, and which types may cross package boundaries.
metadata:
  globs: "**/package.json, **/tsconfig*.json, **/src/index.ts, **/src/index.mts, **/*.d.ts"
---

# TypeScript package design

Use this when the question is what a package should expose, what it may depend
on, and how it may change. `typescript-modules-and-packaging` owns how a
package is built and served; this skill owns what it is.

## Working stance

- The public surface is the smallest set of names that lets a consumer do the
  job. Everything else is internal and is not exported from the entry point.
- Dependencies point inward: adapters depend on the core, the core depends on
  nothing runtime-specific. A package that imports its own consumer has no
  boundary.
- Types that cross a package boundary are part of the contract and are
  versioned with it. A model type that leaks out becomes a transport type
  whether or not anyone meant it to.
- Generated code has one owner package. Other packages import its output, never
  its generator.
- An extension protocol is a boundary with untrusted code on the other side.
  Design it like IPC: validated, versioned, and small.
- Compatibility is a promise with a cost. Make it explicit (semantic
  versioning, a stability tag per export) and keep the promised surface small.

## Decision surface

- **What to export.** Functions and types a consumer needs to call the
  package; error classes or codes a consumer needs to handle; schemas a
  consumer needs to validate against. Not: internal helpers, test utilities, or
  the implementation's data structures. See
  [public-surface.md](references/public-surface.md).
- **Layering.** Core (pure logic, model types), ports (interfaces the core
  needs), adapters (runtime, database, HTTP, Electron main), and composition
  (wiring at the entry point). Enforce the direction with a boundary check
  script or a lint rule, not with a diagram. See
  [dependency-direction-and-layering.md](references/dependency-direction-and-layering.md).
- **Shared protocol packages.** A `shared/` package carries channel names,
  schemas, and the types derived from them. It has no runtime dependency on
  either side and no side effects on import.
- **Plugins.** A plugin API exposes capabilities, not internals: a typed
  registration function, a small set of hooks with validated arguments, and a
  version the host checks. Plugins never receive the host's model objects by
  reference. See
  [plugins-and-extension-protocols.md](references/plugins-and-extension-protocols.md).
- **Compatibility.** Mark each export stable, unstable, or internal (a JSDoc
  tag or a subpath). Breaking changes to stable exports bump the major and ship
  a migration note; unstable exports may break in minors and say so.
  Dual-module hazards and declaration shape are packaging questions; route
  them. See [compatibility.md](references/compatibility.md).
- **Monorepo packages.** One package per deployable or per published unit,
  not per directory. Internal packages that are never published still get an
  `exports` map so their surface is explicit.

## Red flags

- `export * from "./internal/…"` in an entry point.
- A core package importing `electron`, `node:fs`, or a database driver.
- A model type with `Date` or a branded identifier appearing in a wire schema
  because the type was reused across the boundary.
- A plugin receiving the host's store, event emitter, or DOM.
- A `shared` package with a runtime dependency on the renderer or main.
- Two packages that import each other.
- A breaking change to an exported type with no major bump because "nobody
  uses that field".
- Generated types imported from a sibling package's `__generated__` directory
  rather than from its public entry.

## Pairing

- Pair with `typescript-modules-and-packaging` for `exports`, declarations,
  and consumer checks.
- Pair with `typescript-boundaries-and-validation` when the protocol package
  carries schemas.
- Pair with `electron-and-ipc` when the layers are Electron processes.
- Pair with `typescript-types-and-apis` when the public type vocabulary is
  the deliverable.
