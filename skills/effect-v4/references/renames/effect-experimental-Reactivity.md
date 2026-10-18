<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/Reactivity` v3 → v4

- `Reactivity.Reactivity` -> `effect/reactivity/Reactivity#Reactivity`: Use the
  Reactivity interface for implementations and the Reactivity Context.Service
  value as the service key. Implementations require the TypeId brand; prefer
  Reactivity.make. Unsafe methods were renamed with an Unsafe suffix.
- `Reactivity.Reactivity.Service` -> `effect/reactivity/Reactivity#Reactivity`:
  The named namespace member was removed; use the branded Reactivity interface
  directly. Prefer Reactivity.make, or include [Reactivity.TypeId]:
  Reactivity.TypeId in a custom implementation.
- `Reactivity.make` -> `effect/reactivity/Reactivity#make`: Import make from
  the v4 unstable Reactivity module.
- `Reactivity.query`: TODO: needs guidance
