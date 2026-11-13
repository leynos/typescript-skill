# ADR 0002: a version-pinned TypeScript 7 transition skill

Date: 2026-10-16

Status: accepted

## Context

TypeScript 7.0 shipped on 2026-07-08 as the native compiler. It changes the
defaults (`strict`, `module: esnext`, `types: []`, `rootDir: ./`), turns the
options TypeScript 6.0 deprecated into hard errors, and ships without a
programmatic API; a new API is expected in 7.1. Tools that embed TypeScript
(Vue, Svelte, Astro, MDX language services, `typescript-eslint`, declaration
bundlers) therefore still need TypeScript 6 alongside 7, and the release notes
recommend npm aliases to run both.

The estate is spread across the fault line: two repositories pin
`typescript ^5.6.3` (resolving to 5.9.3), two pin `^6.0.x` with
`ignoreDeprecations: "6.0"`, and one runs every type check through a January
development build of the retired `@typescript/native-preview` package while
keeping `typescript ^5.4.5` for library consumers.

Every one of these facts will be wrong within a year. Evergreen skills that
mention them would rot silently.

## Decision

The catalogue gains `typescript-7-transition`, a version-pinned skill modelled
on the Python catalogue's `ruff-016`. It names the release it describes (7.0.2
at the time of writing) and carries a review date. It owns: the 6.0 deprecation
list and its 7.0 removal, the new defaults, side-by-side installation through
npm aliases, compiler-output comparison, the programmatic API gap and which
tools it affects, and the retirement of the native-preview package.

Evergreen skills do not mention compiler versions, `tsgo`, the native-preview
package, or the TypeScript 6 compatibility package. A contract test
(`tests/test_versioned_claims.py`) fails when such a claim appears outside the
versioned skill, the router (which must name the trigger), and the two imported
skills that pin their own TypeScript floor.

The example gate compiles its fixtures under TypeScript 7.0.2 only. TypeScript
6 fixtures are not compiled, because the estate's TypeScript 6 projects already
pass their own gates and a second compiler in this repository would be a second
thing to keep current for no new evidence.

## Consequences

- When TypeScript 7.1 ships its API, the skill needs a new review date, a
  revised tool-gap table, and possibly a new name if the material no longer
  describes a transition.
- The router's trigger for the skill is pinned by
  `tests/test_router_contract.py`.
- The catalogue status carries a maintenance note listing what to re-derive at
  each TypeScript minor release.
- The imported `biome-typescript` and `effect-v4` skills are allowed to name
  TypeScript versions because they pin their own floors; a reviewer should
  check those floors when the transition skill is revised.
