<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/FiberSet` v3 → v4

- `FiberSet.FiberSet` -> `FiberSet.FiberSet`: Retained; contained runtime
  fibers now use the unified Fiber type.
- `FiberSet.TypeId` -> `FiberSet.isFiberSet`: The type-id symbol is private in
  v4; use the public guard.
- `FiberSet.unsafeAdd` -> `FiberSet.addUnsafe`: Renamed to put the Unsafe
  suffix last; the interruptAs option was removed because IDs are now numeric
  runtime details.
