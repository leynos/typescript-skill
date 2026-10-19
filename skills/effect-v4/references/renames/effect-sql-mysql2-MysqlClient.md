<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-mysql2/MysqlClient` v3 → v4

- `MysqlClient.MysqlClientConfig` ->
  `@effect/sql-mysql2/MysqlClient#MysqlClientConfig`: Retained; connectionTTL
  uses Duration.Input and v4 adds disablePreparedStatements.
