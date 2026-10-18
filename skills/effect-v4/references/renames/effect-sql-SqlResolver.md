<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlResolver` v3 → v4

- `SqlResolver.SqlResolver` ->
  `RequestResolver.RequestResolver<SqlResolver.SqlRequest<...>>`: The wrapper
  interface was removed; constructors return RequestResolvers. Execute them
  with effect/sql/SqlResolver#request.
- `SqlResolver.void` -> `effect/sql/SqlResolver#void`: Moved, but remove the
  leading tag and withContext arguments; it now returns a RequestResolver
  synchronously and runs through SqlResolver.request.
