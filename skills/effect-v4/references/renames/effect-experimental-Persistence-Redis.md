<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/Persistence/Redis` v3 → v4

- `Redis.layer` -> `effect/persistence/Persistence#layerBackingRedis`: The
  Redis backing adapter was merged into Persistence and now requires the
  generic Redis.Redis service.
- `Redis.layerConfig` -> `none`: Compose Persistence.layerBackingRedis with a
  config-driven provider such as NodeRedis.layerConfig.
- `Redis.layerResult` -> `effect/persistence/Persistence#layerRedis`: The
  combined Redis persistence layer was merged into Persistence and now requires
  Redis.Redis.
- `Redis.layerResultConfig` -> `none`: Compose Persistence.layerRedis with a
  config-driven provider such as NodeRedis.layerConfig.
- `Redis.make` -> `none`: V4 exposes Redis-backed layers over the Redis.Redis
  service, not a constructor that creates an ioredis client directly.
