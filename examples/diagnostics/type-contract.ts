/**
 * @file Compile-time type-test fixture in the shape of a `.test-d.ts` file:
 * `@ts-expect-error` markers prove the public vocabulary rejects a shape and
 * `Expect<Equal<…>>` proves two types are identical. Compiled by
 * `make examples`; never executed.
 */
// Linked from skills/typescript-testing/SKILL.md.
//
// A compile-time type test in the shape of a `.test-d.ts` file. The gate
// compiles it, so each `@ts-expect-error` proves the public vocabulary rejects
// the shape beneath it, and the `Expect<Equal<…>>` tuple proves two types are
// identical. Nothing here runs.

export type Capability = "handler" | "worker" | "fixture" | "not-implemented";

export interface ManifestEntry {
  readonly operation: string;
  readonly behaviour: Capability;
  readonly status: 200 | 501;
}

type Equal<A, B> =
  (<T>() => T extends A ? 1 : 2) extends <T>() => T extends B ? 1 : 2 ? true : false;
type Expect<T extends true> = T;

// Accepts the vocabulary.
export const supported: Capability = "handler";

// @ts-expect-error "mocked" is not a Capability
export const invalid: Capability = "mocked";

// Checks a shape without widening the inferred literal types.
export const entry = {
  operation: "createDroplet",
  behaviour: "worker",
  status: 501,
} satisfies ManifestEntry;

// An unknown field is rejected on a fresh object literal. The marker sits on
// the offending property, which is where the compiler reports it.
export const extraField: ManifestEntry = {
  operation: "listDroplets",
  behaviour: "handler",
  status: 200,
  // @ts-expect-error `cached` is not a property of ManifestEntry
  cached: true,
};

// Pins the vocabulary and the inferred literal type of `entry.behaviour`.
export type Checks = [
  Expect<Equal<Capability, "handler" | "worker" | "fixture" | "not-implemented">>,
  Expect<Equal<(typeof entry)["behaviour"], "worker">>,
];
