<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/FiberHandle` v3 → v4

- `FiberHandle.FiberHandle` -> `FiberHandle.FiberHandle`: Retained; contained
  runtime fibers now use the unified Fiber type.
- `FiberHandle.TypeId` -> `FiberHandle.isFiberHandle`: The type-id symbol is
  private in v4; use the public guard.
- `FiberHandle.get` -> `FiberHandle.get`: Retained, but v4 returns
  Effect\<Option\<Fiber\>\> instead of failing with NoSuchElementException when
  empty.
- `FiberHandle.unsafeGet` -> `FiberHandle.getUnsafe`: Renamed to put the Unsafe
  suffix last.
- `FiberHandle.unsafeSet` -> `FiberHandle.setUnsafe`: Renamed to put the Unsafe
  suffix last; the interruptAs option was removed because IDs are now numeric
  runtime details.
