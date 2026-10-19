<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TestSized` v3 → v4

- `TestSized.TestSized` -> `Context.Reference<number>`: Collapse the wrapper
  service to the reference itself; yield the reference to read the current size.
- `TestSized.TestSizedTypeId` -> `none`: The wrapper's nominal type id is
  unnecessary; Context.Reference supplies stable key identity.
- `TestSized.fromFiberRef` -> `Context.Reference<number>`: FiberRef and
  TestSized were removed. Define one stable Context.Reference\<number\> instead
  of wrapping a FiberRef.
- `TestSized.make` -> `Context.Reference<number>`: Define a module-level
  reference with defaultValue; do not create a fresh key at each call site.
