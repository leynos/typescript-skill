<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node-shared/NodeCommandExecutor` v3 → v4

- `NodeCommandExecutor.layer` -> `NodeChildProcessSpawner.layer`:
  CommandExecutor became effect/process/ChildProcessSpawner; the Node adapter
  was renamed and still requires FileSystem and Path.
