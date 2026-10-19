<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MutableHashSet` v3 → v4

- `MutableHashSet.MutableHashSet` -> `MutableHashSet.MutableHashSet`: The
  MutableHashSet model remains; use its public operations rather than depending
  on internal representation fields.
- `MutableHashSet.TypeId` -> `none`: The public MutableHashSet.TypeId was
  removed; the v4 marker is private.
