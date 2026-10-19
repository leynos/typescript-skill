<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/BrowserWorker` v3 → v4

- `BrowserWorker.layerManager` -> `BrowserWorker.layerPlatform`: WorkerManager
  was removed. Provide WorkerPlatform directly, or use
  BrowserWorker.layer(spawn) when a Worker.Spawner is also required.
- `BrowserWorker.layerWorker` -> `BrowserWorker.layerPlatform`: PlatformWorker
  became Worker.WorkerPlatform. The platform-only layer no longer takes a spawn
  callback; BrowserWorker.layer(spawn) combines platform and spawner layers.
