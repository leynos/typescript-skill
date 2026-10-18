<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Hash` v3 → v4

- `Hash.cached` -> `none`: Delete Hash.cached wrappers and return the computed
  value from Hash.symbol; Hash.hash now caches objects automatically in a
  private WeakMap without mutating them.
