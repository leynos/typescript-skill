<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/ShardId` v3 → v4

- `ShardId.ShardId` -> `effect/cluster/ShardId#ShardId`: The class became a
  merged interface and schema value. Use ShardId.make; former static parsers
  and printers are module functions.
- `ShardId.TypeId` -> `none`: The shard marker is private in v4. Use
  ShardId.isShardId for runtime refinement.
