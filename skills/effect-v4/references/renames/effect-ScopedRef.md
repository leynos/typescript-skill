<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ScopedRef` v3 → v4

- `ScopedRef.ScopedRef` -> `ScopedRef.ScopedRef`: The type remains but no
  longer extends Effect; use ScopedRef.get or ScopedRef.getUnsafe.
- `ScopedRef.ScopedRef.Variance` -> `none`: The exported variance artifact was
  removed.
- `ScopedRef.ScopedRefTypeId` -> `none`: The marker is private in v4 and no
  public guard exists.
- `ScopedRef.ScopedRefUnify` -> `none`: ScopedRef no longer extends Effect; use
  ScopedRef.get explicitly.
- `ScopedRef.ScopedRefUnifyIgnore` -> `none`: The Effect-unification
  implementation detail was removed.
