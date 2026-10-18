<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-sqlite-react-native/SqliteClient` v3 → v4

- `SqliteClient.asyncQuery` ->
  `@effect/sql-sqlite-react-native/SqliteClient#AsyncQuery`: Renamed and
  changed from FiberRef to Context.Reference; prefer withAsyncQuery or provide
  AsyncQuery as a service.
