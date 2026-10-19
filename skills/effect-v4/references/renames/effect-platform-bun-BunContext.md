<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunContext` v3 → v4

- `BunContext.BunContext` -> `BunServices.BunServices`: The aggregate was
  renamed and now provides ChildProcessSpawner, Crypto, FileSystem, Path,
  Stdio, and Terminal; add BunWorker separately when needed.
- `BunContext.layer` -> `BunServices.layer`: Use the renamed aggregate layer;
  worker services are no longer included.
