<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/MachineId` v3 → v4

- `MachineId.make` -> `effect/cluster/MachineId#make`: Moved into core Effect.
  The v4 helper is an unchecked cast; validate external input with the
  MachineId schema when needed.
