# State machines

## Shape

- Each state is one member of a discriminated union, carrying only the fields
  that exist in that state.
- Each event is one member of another union.
- The transition is a pure function `(state, event) => state` (or
  `=> { state, effects }` when effects are outputs).
- Illegal transitions return the input state unchanged, or an explicit
  `rejected` outcome, but never throw for ordinary protocol violations.

The [exhaustive-state.ts](../../../examples/positive/exhaustive-state.ts)
example shows the shape with `assertNever` closing every `switch`.

## Effects as outputs

```ts
type Effect =
  | { readonly type: "dial"; readonly host: string }
  | { readonly type: "log"; readonly message: string };

interface Step {
  readonly state: Connection;
  readonly effects: readonly Effect[];
}

export function step(state: Connection, event: Event): Step {
  // compute next state, append effects, return both
}
```

The runtime loop interprets effects. The transition is now testable as a table
with no mocks, and the same function drives a replay from a journal.

## Determinism

A transition that reads the wall clock, a random source, or a global counter is
not replayable. Pass them in:

```ts
interface Deps {
  readonly now: () => number;        // virtual or wall clock
  readonly nextId: () => string;     // seeded allocator
  readonly random: () => number;     // seeded PRNG
}
```

A logical worker that owns these dependencies, drains a queue of pending
transitions in virtual-time order, and writes a journal of
`(virtualTime, event, state)` is an orchestration owner. It runs on whatever
thread calls it. Nothing about it requires a Web Worker or a worker thread;
route that question to `typescript-async-and-concurrency` only when the drain
is too slow for the thread that hosts it.

Two gates make determinism a property rather than a hope:

- the same seed and the same event sequence produce byte-identical journals,
- advancing the virtual clock past a scheduled transition applies it, and
  advancing short of it does not.

Both are natural model-based properties; route to `typescript-verification`.

## Testing a transition table

| From         | Event      | To               |
| ------------ | ---------- | ---------------- |
| `idle`       | `dial`     | `connecting(1)`  |
| `connecting` | `opened`   | `open`           |
| `connecting` | `failed`×3 | `closed`         |
| `open`       | `dial`     | `open` (ignored) |
| `closed`     | any        | `closed`         |

_Table 1: A transition table doubles as the named-example test list._

Write the table as a parameterized test with one row per cell, including the
ignored and rejected rows. When the table keeps growing to sample one
invariant, such as "attempts never exceed three", move that invariant to a
property test.

## Runtime libraries

A hand-written union and `switch` is enough for most machines. Reach for a
statechart library when the machine has nested or parallel states, delayed
transitions, or needs visual inspection by non-engineers. The cost is a second
vocabulary; the benefit is tooling. Either way, keep the transition pure and
the effects explicit, or the library cannot help with determinism.
