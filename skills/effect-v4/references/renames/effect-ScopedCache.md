<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ScopedCache` v3 → v4

- `ScopedCache.Lookup` -> `(key: Key) => Effect.Effect<A, E, R | Scope.Scope>`:
  The named alias was removed; use an inline lookup type or
  ScopedCache.ScopedCache\<Key, A, E, R\>["lookup"].
- `ScopedCache.ScopedCache` -> `ScopedCache.ScopedCache`: The model remains as
  a Pipeable scoped cache; construct and use it inside a Scope with explicit
  ScopedCache operations.
- `ScopedCache.ScopedCache.Variance` -> `none`: The public variance marker was
  removed; use ScopedCache.ScopedCache directly.
- `ScopedCache.ScopedCacheTypeId` -> `none`: The ScopedCache type id is
  internal in v4; do not inspect or construct the brand directly.
