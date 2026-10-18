<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MutableRef` v3 → v4

- `MutableRef.MutableRef` -> `MutableRef.MutableRef`: The MutableRef model
  remains; use its public operations rather than depending on internal
  representation fields.
- `MutableRef.TypeId` -> `none`: The public MutableRef.TypeId was removed; the
  v4 marker is private.
