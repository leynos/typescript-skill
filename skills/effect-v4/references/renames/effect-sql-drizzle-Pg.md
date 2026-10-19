<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql-drizzle/Pg` v3 → v4

- `Pg.PgDrizzle` -> `drizzle-orm/effect-postgres#EffectPgDatabase`: The service
  tag was removed; use the database type and define an application Context.Tag
  if service access is required.
- `Pg.layer` -> `Layer.effect(AppDb, PgDrizzle.makeWithDefaults())`: The
  package was removed; import PgDrizzle from drizzle-orm/effect-postgres,
  define an application service tag, and compose with PgClient.layer.
- `Pg.layerWithConfig` ->
  `Layer.effect(AppDb, PgDrizzle.makeWithDefaults(config))`: The package was
  removed; use drizzle-orm/effect-postgres, port config to
  EffectDrizzlePgConfig, and define an application service tag.
- `Pg.make` -> `drizzle-orm/effect-postgres#makeWithDefaults`: Use Drizzle's
  Effect 4 integration; it returns EffectPgDatabase and requires PgClient.
- `Pg.makeWithConfig` -> `drizzle-orm/effect-postgres#makeWithDefaults`: The
  constructor split was removed; use makeWithDefaults(config), or make(config)
  when explicitly providing logger and cache services.
