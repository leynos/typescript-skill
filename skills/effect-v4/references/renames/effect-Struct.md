<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Struct` v3 → v4

- `Struct.entries` -> `Object.entries`: Use the native helper, adding a cast
  when the old precise key and value type is required.
- `Struct.getEquivalence` -> `Struct.makeEquivalence`: Direct rename; the
  fields object call shape is unchanged.
- `Struct.getOrder` -> `Struct.makeOrder`: Direct rename; the fields object
  call shape is unchanged.
