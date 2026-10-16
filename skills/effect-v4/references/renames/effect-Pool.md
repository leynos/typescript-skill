<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Pool` v3 → v4

- `Pool.Pool` -> `Pool.Pool`: The model remains but is now Pipeable rather than
  an Effect subtype; borrow resources explicitly with Pool.get.
- `Pool.Pool.Variance` -> `none`: The public Pool variance marker was removed;
  use Pool.Pool directly.
- `Pool.PoolTypeId` -> `none`: The Pool type id is internal in v4; use
  Pool.isPool for runtime refinement.
- `Pool.PoolUnify` -> `none`: Pool is no longer an Effect subtype, so its
  Effect unification helper was removed; call Pool.get explicitly.
- `Pool.PoolUnifyIgnore` -> `none`: Pool is no longer an Effect subtype, so its
  Effect unification ignore marker was removed.
