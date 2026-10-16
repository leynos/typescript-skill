<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/PersistedQueue/Redis` v3 → v4

- `Redis.layerStore` -> `effect/persistence/PersistedQueue#layerStoreRedis`:
  The Redis adapter was merged into PersistedQueue and now requires the generic
  Redis.Redis service.
- `Redis.layerStoreConfig` -> `none`: Configure a Redis provider such as
  NodeRedis.layerConfig separately, then compose it with
  PersistedQueue.layerStoreRedis.
- `Redis.make` -> `effect/persistence/PersistedQueue#makeStoreRedis`: The Redis
  adapter was merged into PersistedQueue and now requires the generic
  Redis.Redis service.
