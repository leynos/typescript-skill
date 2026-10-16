<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeWorker` v3 → v4

- `NodeWorker.layerManager` -> `NodeWorker.layerPlatform`: WorkerManager was
  removed. Provide WorkerPlatform directly, or use NodeWorker.layer(spawn) when
  a Worker.Spawner is also required.
- `NodeWorker.layerWorker` -> `NodeWorker.layerPlatform`: PlatformWorker became
  Worker.WorkerPlatform; NodeWorker.layer(spawn) combines the platform and
  spawner layers.
