<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlError` v3 → v4

- `SqlError.SqlErrorTypeId` -> `effect/sql/SqlError#isSqlError`: The type id is
  private; use isSqlError for runtime narrowing or isSqlErrorReason for
  structured reason values.
