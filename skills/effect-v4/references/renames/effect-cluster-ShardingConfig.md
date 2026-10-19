<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/ShardingConfig` v3 → v4

- `ShardingConfig.config` -> `effect/cluster/ShardingConfig#config`: Moved into
  core Effect; its Context service value type now uses the Service property
  instead of Type.
- `ShardingConfig.defaults` -> `effect/cluster/ShardingConfig#defaults`: Moved
  into core Effect; service type projections now use Service instead of Type.
  V4 also defaults maxResidentEntities to 10,000 and
  unprocessedMessageBatchSize to 1,024.
- `ShardingConfig.layer` -> `effect/cluster/ShardingConfig#layer`: Moved into
  core Effect with the same shallow default merge; service type projections now
  use Service instead of Type.
