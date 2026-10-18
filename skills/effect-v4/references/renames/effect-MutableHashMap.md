<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MutableHashMap` v3 → v4

- `MutableHashMap.MutableHashMap` -> `MutableHashMap.MutableHashMap`: The
  MutableHashMap model remains; use its public operations rather than depending
  on internal representation fields.
- `MutableHashMap.TypeId` -> `none`: The public MutableHashMap.TypeId was
  removed; the v4 marker is private.
