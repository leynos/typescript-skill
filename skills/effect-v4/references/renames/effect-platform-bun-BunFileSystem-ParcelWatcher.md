<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunFileSystem/ParcelWatcher` v3 → v4

- `ParcelWatcher.layer` -> `BunFileSystem.layer`: The Parcel watcher adapter
  was removed. BunFileSystem.layer uses the built-in node:fs-compatible
  watcher; provide a custom FileSystem.WatchBackend for specialized behavior.
