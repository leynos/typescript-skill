---
name: typescript-7-transition
description: "Use for the TypeScript 6 to 7 transition as of TypeScript 7.0.2: the native compiler's new defaults, the options TypeScript 6.0 deprecated and 7.0 removed, the retired native-preview package, side-by-side installation through npm aliases, compiler-output comparison, the missing programmatic API and the tools it blocks, and the estate's current transition states. Load when upgrading, when tsc rejects an option, or when a tool still needs TypeScript 6."
metadata:
  globs: "**/tsconfig*.json, **/package.json, **/*.ts, **/*.tsx, **/*.mts, **/*.cts"
---

# TypeScript 7 transition

Reviewed 2026-10-16 against TypeScript 7.0.2 and the 6.0 and 7.0 release
announcements. TypeScript 7.0 shipped on 2026-07-08 as the native compiler,
written in Go, installed as the ordinary `typescript` package with the ordinary
`tsc` command. It is 8 to 12 times faster on full builds and it has no
programmatic API yet. Everything in this skill is version-specific and will be
wrong eventually; check `npx tsc --version` before advising, and prefer this
page over recollection.

## Working stance

- Two-step route: adopt TypeScript 6.0 first, clear every deprecation it
  reports, then move to 7.0. TypeScript 6 is the bridge release and reports
  exactly what 7 removes.
- Code that compiles cleanly under 6.0 with `stableTypeOrdering` on and no
  `ignoreDeprecations` is expected to compile identically under 7.0. Treat a
  difference as a bug to report, after ruling out the known semantic changes.
- The programmatic API is the fault line. `tsc` works; anything that imports
  `typescript` as a library needs 6.0 beside 7.0 until 7.1 ships its new API.
- Run both compilers side by side during the transition and diff their output
  on the same tree; do not switch the gate until the diff is empty or explained.
- The native-preview package is retired. Nightlies live under
  `typescript@next`. A project pinned to a dated development build is on an
  unsupported snapshot.

## What changed

- **Defaults.** `strict: true`, `module: esnext`, `target` tracks the latest
  stable ECMAScript, `types: []`, `rootDir: ./`, `noUncheckedSideEffectImports`
  on, `libReplacement` off, `stableTypeOrdering` on and fixed. A project that
  relied on `types` pulling every `@types` package now sets `"types": ["node"]`
  or `["*"]`.
- **Removed options** (deprecated in 6.0, hard errors in 7.0): `target: es5`,
  `downlevelIteration`, `moduleResolution: node`, `node10`, and `classic`,
  `module: amd`, `umd`, `systemjs`, and `none`, `baseUrl`, `outFile`,
  `esModuleInterop: false`, `allowSyntheticDefaultImports: false`,
  `alwaysStrict: false`, the `module` keyword for namespaces, `asserts` on
  imports, and `/// <reference no-default-lib />`. The full table with fixes is
  in
  [defaults-and-removed-options.md](references/defaults-and-removed-options.md).
- **Command line.** `tsc <files>` with a `tsconfig.json` in the directory is an
  error (TS5112); pass `--ignoreConfig` to bypass. New `--checkers`,
  `--builders`, and `--singleThreaded` flags control parallelism.
- **Semantics.** Template literal inference treats code points as units
  (surrogate pairs no longer split); JavaScript analysis matches `.ts` rules
  (values are not types, `@enum` and `@class` lose their special meaning,
  Closure-style function types are gone).
- **Programmatic API.** 7.0 ships none. `@typescript/typescript6` provides the
  6.0 API and a `tsc6` binary. 7.0.2 exposes `typescript/unstable/*` subpaths
  (sync, async, ast); they are unstable and not a replacement for the 6.0 API.
  See [programmatic-api-gap.md](references/programmatic-api-gap.md).

## Decision surface

- **Which tools block the move.** Embedded language services (Vue, Svelte,
  Astro, MDX), Angular template checking, `typescript-eslint`, declaration
  bundlers and API extractors, `ts-morph`, `typescript-json-schema`, anything
  that `import`s `typescript`. Each needs 6.0 beside 7.0 or a release built on
  the 7.1 API.
- **Side by side.** Install `typescript@^7` as `typescript` and
  `@typescript/typescript6` as an alias, or the reverse, so `tsc` is 7 and
  library consumers resolve 6. Recipes and the compare script are in
  [side-by-side-and-aliases.md](references/side-by-side-and-aliases.md).
- **Editors.** VS Code enables TypeScript 7 through the native-preview
  extension by default; embedded-language projects should stay on 6.0 for
  editor support while using 7.0 `tsc` for project-wide checks.
- **Estate states.** Two repositories on 5.9 with `--skipLibCheck` in the
  script; two on 6.0 with `ignoreDeprecations: "6.0"` and `bundler` resolution;
  one on a January native-preview build plus 5.4 for library consumers, with
  `module: commonjs` and `moduleResolution: node` in its Electron main
  configuration. Each has a different first step; see
  [estate-transition-states.md](references/estate-transition-states.md).

## Red flags

- `ignoreDeprecations: "6.0"` left in place as the way to "upgrade" to 7.
- `@typescript/native-preview` in `devDependencies`, especially a dated
  development build.
- `moduleResolution: node` or `module: commonjs` with `baseUrl` in an Electron
  main or a CLI configuration nobody has touched.
- A library consumer of `typescript` (schema generator, boundary checker)
  resolving a 7.0 install and failing to import.
- A `tsconfig` that relied on the old `types` default and now cannot see
  `@types/node`.
- Switching the gate to 7.0 without a compare run against 6.0 output.
- Advice that cites `tsgo` as the command; the binary is `tsc`.

## Pairing

- Pair with `typescript-types-and-apis` for the strictness ratchet, because
  7.0's `strict: true` default meets brownfield directories head on.
- Pair with `typescript-modules-and-packaging` for `module` and
  `moduleResolution` replacements.
- Pair with `typescript-quality-tools` when a lint tool needs the 6.0 API.
