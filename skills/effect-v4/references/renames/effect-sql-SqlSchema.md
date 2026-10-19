<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlSchema` v3 → v4

- `SqlSchema.single` -> `effect/sql/SqlSchema#findOne`: Renamed with the same
  first-row-or-fail behavior; empty results use Cause.NoSuchElementError and
  schema failures use Schema.SchemaError.
- `SqlSchema.void` -> `effect/sql/SqlSchema#void`: Moved with the same encode,
  execute, and discard-result pattern; schema failures now use
  Schema.SchemaError.
