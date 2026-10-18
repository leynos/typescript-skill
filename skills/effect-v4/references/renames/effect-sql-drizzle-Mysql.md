<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-drizzle/Mysql` v3 → v4

- `Mysql.MysqlDrizzle` -> `drizzle-orm/effect-mysql2#EffectMysql2Database`: The
  service tag was removed; use the database type and define an application
  Context.Tag if service access is required.
- `Mysql.layer` -> `Layer.effect(AppDb, MysqlDrizzle.makeWithDefaults())`: The
  package was removed; import MysqlDrizzle from drizzle-orm/effect-mysql2,
  define an application service tag, and compose with MysqlClient.layer.
- `Mysql.layerWithConfig` ->
  `Layer.effect(AppDb, MysqlDrizzle.makeWithDefaults(config))`: The package was
  removed; use drizzle-orm/effect-mysql2, port config to
  EffectDrizzleMySqlConfig, and define an application service tag.
- `Mysql.make` -> `drizzle-orm/effect-mysql2#makeWithDefaults`: Use Drizzle's
  Effect 4 integration; it returns EffectMysql2Database and requires
  MysqlClient.
- `Mysql.makeWithConfig` -> `drizzle-orm/effect-mysql2#makeWithDefaults`: The
  constructor split was removed; use makeWithDefaults(config), or make(config)
  when explicitly providing logger and cache services.
