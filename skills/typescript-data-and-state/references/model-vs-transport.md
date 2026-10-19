# Model versus transport

A model type is what the program reasons about. A transport type is what a
boundary carries: JSON over HTTP, a `postMessage` payload, a row in storage, a
line in a journal. They differ in representation even when the fields match.

## What changes at the edge

| Model            | Transport                              | Why                                      |
| ---------------- | -------------------------------------- | ---------------------------------------- |
| `Date`           | ISO 8601 string                        | JSON has no date; `structuredClone` does |
| `Map<K, V>`      | `Array<[K, V]>` or `Record<string, V>` | JSON turns `Map` into `{}`               |
| `Set<T>`         | `T[]`                                  | Same                                     |
| `bigint`         | decimal string                         | `JSON.stringify` throws on `bigint`      |
| branded `UserId` | `string`                               | Brands are compile-time only             |
| missing key      | missing key                            | `undefined` is dropped; keep it absent   |
| `Error`          | `{ name, message, code, cause? }`      | `Error` serializes to `{}`               |
| class instance   | plain object                           | Methods and prototypes do not travel     |
| `camelCase`      | whatever the wire uses                 | Do not rename the wire to suit the model |

_Table 1: Representations that change between model and transport._

## Where the converter lives

One module per boundary owns both directions:

```ts
export function toDto(model: Order): OrderDto { /* ... */ }
export function fromDto(dto: OrderDto): Order { /* validated, branded */ }
```

`fromDto` runs after validation, so it can assume shape and only has to change
representation. Validation itself belongs to
`typescript-boundaries-and-validation`; the converter is the last step of the
parse. Nothing outside the boundary module imports a `*Dto` type.

## Persisted and replayed state

State that is written to disk, a journal, or a snapshot gains a version:

```ts
interface SnapshotV2 {
  readonly version: 2;
  readonly entries: readonly EntryDto[];
}
```

Keep the migration from each older version as a pure function and test the
chain from the oldest supported version. Deleting a migration is a decision to
drop support, not a cleanup.

## `structuredClone` and `postMessage`

Worker and IPC messages use the structured clone algorithm, which carries
`Date`, `Map`, `Set`, typed arrays, and cycles but not functions, class
prototypes, DOM nodes, or symbols. A class instance arrives as a plain object.
Treat the message as a transport type anyway: validate it and convert it, so
the day the payload moves to JSON nothing changes but the serializer.

## Generated transport types

Types generated from OpenAPI, GraphQL, or protobuf are transport types by
definition. Do not use them as model types, and do not hand-edit them; route
generation and ownership to `typescript-modules-and-packaging`.
