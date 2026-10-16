<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-mssql/MssqlClient` v3 → v4

- `MssqlClient.MssqlClient` -> `@effect/sql-mssql/MssqlClient#MssqlClient`:
  Retained; the service value is now a Context.Service rather than a GenericTag.
- `MssqlClient.MssqlClientConfig` ->
  `@effect/sql-mssql/MssqlClient#MssqlClientConfig`: Retained; durations use
  Duration.Input, parameterTypes is keyed by Statement.PrimitiveKind, and v4
  adds retry and timeout options.
