<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlPersistedQueue` v3 → v4

- `SqlPersistedQueue.layerStore` ->
  `effect/persistence/PersistedQueue#layerStoreSql`: Moved into PersistedQueue
  and renamed with the Sql suffix; options are unchanged.
- `SqlPersistedQueue.make` -> `effect/persistence/PersistedQueue#makeStoreSql`:
  Use the SQL store constructor; PersistedQueue.make creates a typed queue from
  a store factory and is not equivalent.
