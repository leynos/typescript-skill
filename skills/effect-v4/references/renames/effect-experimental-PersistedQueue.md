<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/PersistedQueue` v3 → v4

- `PersistedQueue.ErrorTypeId` ->
  `effect/persistence/PersistedQueue#ErrorTypeId`: Retained as a string brand;
  the runtime marker now uses the persistence module path.
- `PersistedQueue.TypeId` -> `effect/persistence/PersistedQueue#TypeId`: Import
  TypeId from the v4 unstable PersistedQueue module; it is now a string brand.
- `PersistedQueue.make` -> `effect/persistence/PersistedQueue#make`: Import
  make from the v4 unstable PersistedQueue module.
