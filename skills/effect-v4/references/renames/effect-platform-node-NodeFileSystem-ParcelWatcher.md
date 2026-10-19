<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeFileSystem/ParcelWatcher` v3 → v4

- `ParcelWatcher.layer` -> `NodeFileSystem.layer`: The Parcel watcher adapter
  was removed. Native node:fs.watch support is built in;
  FileSystem.WatchBackend is the extension point.
