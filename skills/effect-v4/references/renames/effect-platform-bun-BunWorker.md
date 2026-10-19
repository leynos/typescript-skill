<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunWorker` v3 → v4

- `BunWorker.layerManager` -> `BunWorker.layerPlatform`: WorkerManager was
  removed. Provide WorkerPlatform directly, or use BunWorker.layer(spawn) when
  a Worker.Spawner is also required.
- `BunWorker.layerWorker` -> `BunWorker.layerPlatform`: PlatformWorker became
  Worker.WorkerPlatform; BunWorker.layer(spawn) combines the platform and
  spawner layers.
