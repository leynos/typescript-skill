<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TPriorityQueue` v3 → v4

- `TPriorityQueue.TPriorityQueue` -> `TxPriorityQueue.TxPriorityQueue`: Rename
  the type and import from "effect/TxPriorityQueue". V4 Tx operations return
  ordinary Effects; compose multiple operations under one outer Effect.tx to
  keep them atomic.
- `TPriorityQueue.TPriorityQueue.Variance` -> `none`: TxPriorityQueue exposes
  no public variance marker.
- `TPriorityQueue.TPriorityQueueTypeId` -> `TxPriorityQueue.isTxPriorityQueue`:
  The type id is internal in v4; use the public runtime guard.
- `TPriorityQueue.empty` -> `TxPriorityQueue.empty`: Import TxPriorityQueue
  from "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.fromIterable` -> `TxPriorityQueue.fromIterable`: Import
  TxPriorityQueue from "effect/TxPriorityQueue"; the operation keeps its name.
  V4 Tx operations return ordinary Effects; compose multiple operations under
  one outer Effect.tx to keep them atomic.
- `TPriorityQueue.isEmpty` -> `TxPriorityQueue.isEmpty`: Import TxPriorityQueue
  from "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.isNonEmpty` -> `TxPriorityQueue.isNonEmpty`: Import
  TxPriorityQueue from "effect/TxPriorityQueue"; the operation keeps its name.
  V4 Tx operations return ordinary Effects; compose multiple operations under
  one outer Effect.tx to keep them atomic.
- `TPriorityQueue.make` -> `TxPriorityQueue.make`: Import TxPriorityQueue from
  "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.peek` -> `TxPriorityQueue.peek`: Import TxPriorityQueue from
  "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.size` -> `TxPriorityQueue.size`: Import TxPriorityQueue from
  "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.take` -> `TxPriorityQueue.take`: Import TxPriorityQueue from
  "effect/TxPriorityQueue"; the operation now returns an ordinary Effect, so
  compose multiple operations under one outer Effect.tx to keep them atomic.
- `TPriorityQueue.takeAll` -> `TxPriorityQueue.takeAll`: Import TxPriorityQueue
  from "effect/TxPriorityQueue"; it returns an ordinary Effect containing the
  priority-ordered Array.
- `TPriorityQueue.toArray` -> `TxPriorityQueue.toArray`: Import TxPriorityQueue
  from "effect/TxPriorityQueue"; the operation keeps its name. V4 Tx operations
  return ordinary Effects; compose multiple operations under one outer
  Effect.tx to keep them atomic.
- `TPriorityQueue.toChunk` ->
  `Effect.map(TxPriorityQueue.toArray(self), Chunk.fromIterable)`: The direct
  Chunk conversion was removed; convert the retained Array snapshot explicitly.
