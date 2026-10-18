<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/Model` v3 → v4

- `Model.TypeId` -> `none`: The Model brand still exists internally, but its
  TypeId is not exported and v4 has no public isModel guard. Use Model values
  created by Model.make rather than inspecting or constructing the brand.
