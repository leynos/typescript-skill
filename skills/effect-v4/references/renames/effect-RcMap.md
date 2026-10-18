<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/RcMap` v3 → v4

- `RcMap.RcMap` -> `RcMap.RcMap`: The model remains as a Pipeable
  reference-counted resource map; use RcMap.get explicitly inside a Scope.
- `RcMap.RcMap.Variance` -> `none`: The public variance marker was removed; use
  RcMap.RcMap directly.
- `RcMap.TypeId` -> `none`: The RcMap type id is internal in v4; do not inspect
  or construct the brand directly.
