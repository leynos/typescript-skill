# Declarations and dual packages

## Declaration files are format-specific

A `.d.ts` beside a `.js` takes the format of that `.js` under the nearest
`"type"`. A `.d.mts` is ESM; a `.d.cts` is CJS. A dual package therefore needs
two declaration files, one per format, or `attw` reports that the `require`
consumer is handed ESM-shaped types (or the reverse).

Build tools that emit both (`tsdown`, `tsup --dts`, rollup with the dts plugin)
write `index.d.ts` plus `index.d.cts` or `index.d.mts` and wire them into
`exports`. Check the output; do not assume.

## The dual-package hazard

When a package ships both ESM and CJS and a program loads both (one dependency
imports, another requires), there are two copies of every module-scope value:
two `Symbol`s, two class identities, two singletons. `instanceof` across the
copies fails.

Avoid it by one of:

- shipping ESM only, when every consumer can import;
- keeping no state in module scope, so two copies are harmless;
- making the CJS entry a thin wrapper that re-exports the ESM one through a
  synchronous `require` of ESM where the runtime floor allows it, or otherwise
  documenting the hazard.

Decide and record the decision in the package README.

## `isolatedDeclarations`

With `isolatedDeclarations` on, every exported symbol needs an explicit type
annotation so a single-file tool can emit declarations without the checker. It
makes declaration emit fast and parallel, and it forces the public API to be
written down. Turn it on for libraries; leave it off for applications that
never emit declarations.

## Declaration-only consumers

Some consumers only ever read the types: editors, `tsc` in a downstream
project, documentation generators. For them:

- keep `declarationMap` on so "go to definition" reaches source;
- never reference a `src/` path from a `.d.ts`;
- avoid `export *` from a `.d.ts` that would pull in an internal module's
  private names.

## Checking resolution modes

`attw` evaluates the package under four resolution modes (`node10`, `node16`
ESM, `node16` CJS, `bundler`) and reports:

| Finding                    | Meaning                                                         |
| -------------------------- | --------------------------------------------------------------- |
| No types                   | Condition resolves JS but no declaration                        |
| Masquerading as ESM or CJS | Declaration format disagrees with the JS it describes           |
| False export default       | CJS `module.exports =` described as a default export            |
| Untyped resolution         | A subpath resolves JS but `types` is missing for that condition |

_Table 1: Common attw findings and what each means._

Each finding is a consumer bug that a type check on their side will surface.
Fix the map or the emit; do not add `typesVersions` to paper over it unless
`node10` support is a stated requirement.
