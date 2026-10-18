<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-sqlite-wasm/SqliteClient` v3 → v4

- `SqliteClient.SqliteClient` ->
  `@effect/sql-sqlite-wasm/SqliteClient#SqliteClient`: Retained with the same
  export/import surface; the service value is now a Context.Service.
- `SqliteClient.currentTransferables` ->
  `@effect/sql-sqlite-wasm/SqliteClient#Transferables`: Renamed and changed
  from FiberRef to Context.Reference; prefer withTransferables or provide
  Transferables as a service.
