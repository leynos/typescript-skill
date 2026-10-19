# Estate transition states

Reviewed 2026-10-16 from
[the source inventory](../../../docs/source-inventory.md). Each state has a
different first step.

## State A: 5.9 via `^5.6.3`, strict, bundled application

Two front-end mockups and the shared lint package. `module: ESNext`,
`moduleResolution: Bundler`, `noEmit`, `--skipLibCheck` on the command line in
the mockups.

First steps:

1. Upgrade to 6.0.x. Expect `types: []` to remove `@types/node` from the
   server entry and the token build; set `"types": ["node"]` in those
   configurations.
2. `rootDir` defaults to the configuration directory; the mockups do not emit,
   so no change, but the lint package emits to `dist` and already sets
   `rootDir: src` in its build configuration.
3. Decide whether `--skipLibCheck` stays. Under 7.0 the check is fast; try
   removing the flag and fixing or pinning the offending `@types`.
4. Nothing imports `typescript` in the mockups; move them to 7.0 after the
   compare run. The lint package's tests spawn Oxlint, not the compiler; it can
   move too.

## State B: 6.0 with `ignoreDeprecations: "6.0"`, published library

Two simulators. `verbatimModuleSyntax`, `allowImportingTsExtensions`,
`moduleResolution: bundler`, `noEmit`, tsdown for dual emit with `dts`,
graphql-codegen.

First steps:

1. Find out what `ignoreDeprecations` is silencing (`tsc --showConfig` and a
   run without it). If it is nothing, delete it; if it is `moduleResolution` or
   `baseUrl`, fix the option.
2. Check tsdown's declaration path and graphql-codegen against 7.0. Both are
   likely to need 6.0 for declaration bundling until they release against the
   7.1 API; alias accordingly.
3. Run the compare script; `stableTypeOrdering` may reorder union members in
   the emitted `.d.ts`, which the packed-install test and `attw` will exercise.
4. Switch `check:types` to 7.0 `tsc`; keep 6.0 for the build's `dts` step
   until tsdown no longer needs it.

## State C: 5.4 plus a dated native preview, brownfield Electron

The terminal. `typescript ^5.4.5` for `scripts/check-package-boundaries.mjs` and
`typescript-json-schema`; `@typescript/native-preview ^7.0.0-dev.20260128.1`
running every `tsgo --project` type-check and build. The Electron main
configuration uses `module: commonjs` and `moduleResolution: node`; the root
and typecheck configurations switch `strict` and most other switches off.

First steps:

1. Replace the preview dependency with `typescript@7.0.2` and change every
   `bunx tsgo` to `bunx tsc`. The January preview predates the 7.0 release and
   several of its behaviour changes; the diff may be noisy.
2. Alias `@typescript/typescript6` for the boundary checker and the schema
   generator, which import `typescript`.
3. `moduleResolution: node` is a hard error in 7.0. The Electron main's
   CommonJS configuration needs `nodenext` with `"type"` and file extensions
   sorted out, or `bundler` if esbuild owns resolution. That is a packaging
   decision; route to `typescript-modules-and-packaging`.
4. `strict: true` is now the default, and the root configuration turns it off
   explicitly. That is permitted and unchanged, but it is the moment to start
   the per-directory ratchet rather than carrying a repository-wide relaxation;
   route to `typescript-types-and-apis`.
5. Run the compare script between the 5.4 library compiler and 7.0 `tsc` only
   as a curiosity; the honest comparison is 6.0 versus 7.0, which means passing
   through 6.0 first.

## Common to all three

- Pin exact versions in `package.json` and the lockfile during the transition.
- Record the transition state in the repository's `AGENTS.md` so an agent
  does not "fix" the alias arrangement.
- Re-read this page's review date before acting on it.
