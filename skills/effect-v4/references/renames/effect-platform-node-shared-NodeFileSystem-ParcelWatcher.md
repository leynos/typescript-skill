<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node-shared/NodeFileSystem/ParcelWatcher` v3 → v4

- `ParcelWatcher.layer` -> `NodeFileSystem.layer`: The Parcel watcher adapter
  was removed. NodeFileSystem.layer uses node:fs.watch; provide a custom
  FileSystem.WatchBackend for specialized behavior.
