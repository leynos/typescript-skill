<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-clickhouse/ClickhouseClient` v3 → v4

- `ClickhouseClient.ClickhouseClient` ->
  `@effect/sql-clickhouse/ClickhouseClient#ClickhouseClient`: Retained; the
  service value is now a Context.Service rather than a GenericTag.
- `ClickhouseClient.currentClickhouseSettings` ->
  `@effect/sql-clickhouse/ClickhouseClient#ClickhouseSettings`: Renamed and
  changed from FiberRef to Context.Reference; prefer
  client.withClickhouseSettings or provide the reference as a service.
- `ClickhouseClient.currentClientMethod` ->
  `@effect/sql-clickhouse/ClickhouseClient#ClientMethod`: Renamed and changed
  from FiberRef to Context.Reference; prefer client.asCommand or provide the
  reference as a service.
- `ClickhouseClient.currentQueryId` ->
  `@effect/sql-clickhouse/ClickhouseClient#QueryId`: Renamed and changed from
  FiberRef to Context.Reference; prefer client.withQueryId or provide the
  reference as a service.
