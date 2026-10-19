<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/FiberMap` v3 → v4

- `FiberMap.FiberMap` -> `FiberMap.FiberMap`: Retained; contained runtime
  fibers now use the unified Fiber type.
- `FiberMap.TypeId` -> `FiberMap.isFiberMap`: The type-id symbol is private in
  v4; use the public guard.
- `FiberMap.unsafeGet` -> `FiberMap.getUnsafe`: Renamed to put the Unsafe
  suffix last.
- `FiberMap.unsafeHas` -> `FiberMap.hasUnsafe`: Renamed to put the Unsafe
  suffix last.
- `FiberMap.unsafeSet` -> `FiberMap.setUnsafe`: Renamed to put the Unsafe
  suffix last; the interruptAs option was removed because IDs are now numeric
  runtime details.
