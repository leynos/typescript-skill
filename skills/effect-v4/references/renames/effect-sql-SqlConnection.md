<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlConnection` v3 → v4

- `SqlConnection.Connection` -> `effect/sql/SqlConnection#Connection`: Moved;
  Connection.Acquirer is now top-level SqlConnection.Acquirer, and custom
  connections must implement executeValuesUnprepared.
