<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-sqlite-do/SqliteClient` v3 → v4

- `SqliteClient.SqliteClientConfig` ->
  `@effect/sql-sqlite-do/SqliteClient#SqliteClientConfig`: Retained; db is
  optional and storage may be supplied, but one of db or storage is required at
  runtime.
