---
name: typescript-modules-and-packaging
description: Use for modules and packaging in TypeScript and JavaScript, including ESM and CJS, module resolution, package exports maps, declaration emit, source and development conditions, .ts import behaviour, dual packages, packed-artifact testing, code generation, publint, and attw.
metadata:
  globs: "**/package.json, **/tsconfig*.json, **/tsdown.config.*, **/tsup.config.*, **/rollup.config.*, **/vite.config.*, **/*.mts, **/*.cts, **/*.mjs, **/*.cjs, **/*.d.ts"
---

# TypeScript modules and packaging

Use this when the question is how code is resolved, built, and consumed: by the
compiler, by a bundler, by Node or Bun at runtime, and by a downstream package
that installs the published artefact.

## Working stance

- The artefact a consumer installs is the product. Test that, not the source
  tree. A packed tarball installed into a scratch project is the only evidence
  that `exports`, declarations, and conditions work.
- Format decisions are made once per package and recorded in `package.json`:
  `"type"`, `exports`, and the build tool's `format` list. Everything else
  follows.
- ESM is the default for new packages. Ship CJS only when a named consumer
  requires it, and then ship both from one build with one set of tests.
- Declarations are part of the API. A missing `types` condition or a `.d.ts`
  that resolves to the wrong format breaks consumers silently until a type
  check runs on their side.
- Generated code has exactly one owner and exactly one of two states: tracked
  and never hand-edited, or ignored and regenerated in the build.

## Decision surface

- **Module settings.** Applications bundled by Vite or similar use
  `module: esnext` with `moduleResolution: bundler`. Packages and Node code use
  `module: nodenext`, which follows Node's rules for `.mjs`, `.cjs`, and
  `"type"`. `verbatimModuleSyntax` is on either way; it makes import elision
  explicit and keeps single-file transpilers correct. See
  [esm-cjs-and-exports.md](references/esm-cjs-and-exports.md).
- **`.ts` imports.** `allowImportingTsExtensions` suits `noEmit` projects
  that run under Bun or a bundler. `rewriteRelativeImportExtensions` suits
  projects that emit and want `.ts` in source rewritten to `.js` in output.
  Pick one; never ship `.ts` specifiers in a published artefact.
- **`exports` map.** List every public entry explicitly, put `types` first in
  each condition block, and include `"./package.json"`. A `development` or
  `source` condition that points at `src/` is a convenience for a monorepo;
  strip it at publish time with `publishConfig.exports` so consumers never
  resolve into source.
- **Dual packages.** One build (tsdown, tsup, or rollup) emitting `.mjs` and
  `.cjs` with matching `.d.mts` and `.d.cts`. The dual-package hazard (two
  module instances of one package) is avoided by keeping state out of module
  scope or by making the CJS entry re-export the ESM one. See
  [declarations-and-dual-packages.md](references/declarations-and-dual-packages.md).
- **Consumer checks.** `publint` for `package.json` mistakes, `attw`
  (`@arethetypeswrong/cli`) for declaration resolution under every resolution
  mode, and a packed-install smoke test that imports the package from ESM, CJS,
  and TypeScript. All three run in CI on the packed tarball. See
  [consumer-checks.md](references/consumer-checks.md).
- **Code generation.** Schema in, code out, through one script that CI runs
  and then diffs. Generated output is excluded from lint and from the
  strictness ratchet. See [generated-code.md](references/generated-code.md).
- **Monorepos.** Workspace packages resolve through `exports` like any other
  package. A `development` condition lets the workspace import source while a
  published consumer imports `dist/`; test both paths.

## Red flags

- `exports` has `import` and `require` but no `types`, and declarations are
  found only through a top-level `types` field plus `typesVersions`.
- A `.d.ts` that is ESM-shaped is served to a `require` consumer, or the
  reverse; `attw` reports it as a false export default or masquerading.
- `main` and `module` fields without `exports`, so every file is public.
- A `development` condition that survives into the published package.
- `__dirname` or `require.resolve` in ESM source; use `import.meta.dirname`
  and `import.meta.resolve`, or `createRequire` in one adapter.
- A generated file present in `.gitignore` and also tracked.
- Published `bin` that is `.cjs` while the library is ESM-only, with no
  explicit decision recorded.
- A package tested only by importing `src/` through a path alias.

## Pairing

- Pair with `arch-typescript-package-design` when the question is what the
  public surface should be rather than how it is served.
- Pair with `typescript-types-and-apis` when declaration shape or
  `isolatedDeclarations` constrains the API.
- Pair with `typescript-boundaries-and-validation` when a generated client is
  the boundary.
- Pair with `node-bun-and-processes` for Node and Bun runtime differences in
  resolution.
