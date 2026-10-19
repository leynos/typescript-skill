<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/EntityAddress` v3 → v4

- `EntityAddress.EntityAddressFromSelf` ->
  `effect/cluster/EntityAddress#EntityAddress`: The separate self schema was
  removed; the v4 Schema.Class is itself the EntityAddress schema.
- `EntityAddress.TypeId` -> `none`: The marker is private in v4. Use the
  exported EntityAddress class and schema.
