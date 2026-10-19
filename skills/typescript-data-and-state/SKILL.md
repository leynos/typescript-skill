---
name: typescript-data-and-state
description: Use for runtime data and state in TypeScript and JavaScript, including identity, absence versus undefined versus null, immutable updates, discriminated state machines, deterministic transitions, serializable state, and the line between model types and transport types.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.js, **/*.jsx, **/*.mjs, **/*.cjs"
---

# TypeScript data and state

Use this when the question is about values at runtime: what a value means,
whether it can be absent, who may change it, how it moves between states, and
what survives serialization. Clever typings are the companion, not the point.

## Working stance

- Separate the model (what the program reasons about) from the transport (what
  crosses a wire, a file, or a process). They are different types with a
  converter between them, even when the fields look the same today.
- Absence is a value with meaning. Decide what "missing" means for each field,
  and encode it once: a missing key, `undefined`, `null`, or a variant.
- Prefer data that can be compared and serialized by structure. Identity-based
  objects, class instances with methods, `Map`, `Set`, `Date`, and `bigint` all
  need a deliberate decision at every boundary.
- State transitions are functions from state and event to state. Side effects
  are inputs or outputs of those functions, never hidden inside them.
- Determinism is a design property. If a transition needs the clock, a random
  value, or an identifier, those arrive as parameters or injected services.

## Decision surface

- **Absence.** Under `exactOptionalPropertyTypes`, `field?: T` means the key
  may be missing and may not hold `undefined`; `field: T | undefined` means the
  key is present and may be empty; `field: T | null` means the producer chose
  to say "no value". Use one convention per boundary and convert at the edge.
  See [absence-and-identity.md](references/absence-and-identity.md).
- **Identity.** Two objects with equal fields are equal by value only if the
  code says so. Use branded identifiers for entities, structural comparison for
  values, and never rely on reference equality across a boundary.
- **Immutability.** Mark model types `readonly` throughout and produce new
  values with spreads or structured updates. Freeze only at the edge where
  untrusted code could mutate. Mutation inside a function that owns a local is
  fine; mutation of a shared object is a bug waiting for a second caller.
- **State machines.** Model each state as a variant of a discriminated union
  whose fields exist only in that state, so a `connecting` state cannot carry a
  `socketId`. Write the transition as one exhaustive function and test it as a
  table. See [state-machines.md](references/state-machines.md) and the
  [exhaustive-state.ts](../../examples/positive/exhaustive-state.ts) example.
- **Deterministic transitions.** A logical worker that drains a queue of
  transitions in virtual-time order is an orchestration owner, not a thread.
  Give it a clock, an identity allocator, and a journal as injected
  dependencies, and the same seed yields the same journal.
- **Serializable state.** State that persists, replays, or crosses a process
  must round-trip through JSON. Keep `Date` as ISO strings, `Map` as arrays of
  pairs or records, `bigint` as strings, and `undefined` as a missing key. See
  [model-vs-transport.md](references/model-vs-transport.md).

## Red flags

- Two optional fields that are only meaningful together; make them one
  optional object or a variant.
- A `null` check and an `undefined` check on the same field in different
  modules.
- A function that both computes a new state and calls `fetch`, `Date.now()`,
  or `Math.random()`.
- A `class` whose instances are put into Redux, `postMessage`, or
  `localStorage` and come back as plain objects with no methods.
- `JSON.parse(JSON.stringify(x))` used as a deep clone of a value that holds
  a `Date`, `Map`, or `undefined` field.
- A reducer that mutates its argument and returns it.
- A `Date` compared with `===`, or an entity compared by object identity after
  a round trip.
- A transition table with no test row for the transition that is not allowed.

## Pairing

- Pair with `typescript-types-and-apis` when the public type vocabulary is the
  deliverable, for example a published command or event union.
- Pair with `typescript-boundaries-and-validation` when the transport type is
  parsed from untrusted input.
- Pair with `typescript-verification` when the invariant spans many states or
  sequences; model-based property tests and proofs both start from an explicit
  transition function.
- Pair with `react-and-accessible-ui` when the state in question is component
  state and the question is who owns it.
