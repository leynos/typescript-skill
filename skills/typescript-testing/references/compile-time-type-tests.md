# Compile-time type tests

A compile-time test proves that a type accepts the shapes it should and rejects
the shapes it must not. It runs when the project type-checks; no runner is
involved.

## Shape

```ts
// tests/capabilities.test-d.ts
import type { Capability, ManifestEntry } from "../src/capabilities.js";

// Accepts the vocabulary.
const supported: Capability = "handler";

// Rejects a value outside it. The marker fails to compile if the error ever
// disappears, so a widened type is caught.
// @ts-expect-error "mocked" is not a Capability
const invalid: Capability = "mocked";

// Checks a shape without widening it.
const entry = {
  operation: "createDroplet",
  behaviour: "worker",
  status: 501,
} satisfies ManifestEntry;

export { supported, invalid, entry };
```

The [type-contract.ts](../../../examples/diagnostics/type-contract.ts) fixture
shows the same shape compiled by this repository's gate.

## Rules

- Every `@ts-expect-error` carries a reason on the same line naming the
  rejection it asserts.
- Export or otherwise use the declared values so `noUnusedLocals` does not
  flag them, or disable that check for the type-test directory.
- Include the files in a `tsconfig` that the gate compiles. A `.test-d.ts`
  nothing compiles is a comment.
- Prefer `satisfies` over an annotation when the inferred literal type matters
  downstream.
- For assignability in both directions, write a small helper:

```ts
type Equal<A, B> = (<T>() => T extends A ? 1 : 2) extends <T>() => T extends B ? 1 : 2 ? true : false;
type Expect<T extends true> = T;

export type Checks = [
  Expect<Equal<keyof Commands, "shell:run" | "config:read">>,
  Expect<Equal<Request<"config:read">, Record<string, never>>>,
];
```

A tuple of `Expect<…>` entries fails to compile when any equality breaks, and
the error points at the entry.

## What to pin

| Contract                                  | Assertion                                                  |
| ----------------------------------------- | ---------------------------------------------------------- |
| A literal union is closed                 | `@ts-expect-error` on a value outside it                   |
| A command shape rejects an extra field    | `@ts-expect-error` on an object literal with the field     |
| A registry's keys are exactly a set       | `Expect<Equal<keyof R, …>>`                                |
| An exported function's return type        | `Expect<Equal<ReturnType<typeof f>, …>>`                   |
| A generic infers as intended              | `satisfies` on a call result                               |
| A type is not `any`                       | `Expect<Equal<0 extends 1 & T ? true : false, false>>`     |
| A consumer can import the package's types | A `consumer/` fixture compiled against the packed artefact |

_Table 1: Type-level contracts and the assertion that pins each._

## Tooling

- The compiler alone is sufficient and has no version drift relative to the
  project.
- `expect-type` (used by Vitest's `expectTypeOf`) and `tsd` offer fluent
  assertions; they add a dependency and a second vocabulary. Use them when the
  project already does, otherwise stay with the compiler.
- A type-test file that must also run under the unit runner can hold both
  compile-time checks and runtime `test` calls; keep the compile-time part at
  the top so a failure is visible without running anything.
