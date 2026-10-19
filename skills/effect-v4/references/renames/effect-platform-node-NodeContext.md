<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeContext` v3 → v4

- `NodeContext.NodeContext` -> `NodeServices.NodeServices`: Use the renamed
  service union; it replaces CommandExecutor with ChildProcessSpawner, adds
  Crypto and Stdio, and omits WorkerManager.
- `NodeContext.layer` -> `NodeServices.layer`: The aggregate was renamed and
  now provides ChildProcessSpawner, Crypto, FileSystem, Path, Stdio, and
  Terminal; add NodeWorker separately when needed.
