<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-drizzle/Sqlite` v3 → v4

- `Sqlite.SqliteDrizzle` -> `matching drizzle-orm Effect SQLite database type`:
  The generic service tag was removed; use the backend-specific database type
  and define an application Context.Tag if needed.
- `Sqlite.layer` -> `Layer.effect(AppDb, SqliteDrizzle.makeWithDefaults())`:
  The package was removed; select the matching drizzle-orm Effect backend
  module, define an application service tag, and compose with its SQL client
  layer.
- `Sqlite.layerWithConfig` ->
  `Layer.effect(AppDb, SqliteDrizzle.makeWithDefaults(config))`: Select the
  matching drizzle-orm Effect backend, port config to
  EffectDrizzleSQLiteConfig, and define an application service tag.
- `Sqlite.make` -> `drizzle-orm/effect-sqlite-node#makeWithDefaults`: SQLite
  integration is backend-specific; use the module matching sql-sqlite-node,
  -bun, -do, -wasm, libsql, or d1.
- `Sqlite.makeWithConfig` ->
  `matching drizzle-orm Effect SQLite module#makeWithDefaults`: The generic
  constructor was removed; select the concrete backend and use
  makeWithDefaults(config), or make(config) with explicit services.
