<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/RateLimiter/Redis` v3 → v4

- `Redis.layerStore` -> `effect/persistence/RateLimiter#layerStoreRedis`: The
  Redis adapter was merged into RateLimiter and now requires the generic
  Redis.Redis service.
- `Redis.layerStoreConfig` ->
  `effect/persistence/RateLimiter#layerStoreRedisConfig`: Use the merged Redis
  store config layer; connection configuration belongs to a separate Redis
  provider.
- `Redis.make` -> `effect/persistence/RateLimiter#makeStoreRedis`: The Redis
  adapter was merged into RateLimiter and now requires the generic Redis.Redis
  service.
