<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/CommandExecutor` v3 → v4

- `CommandExecutor.CommandExecutor` ->
  `ChildProcessSpawner.ChildProcessSpawner`: The executor service moved to
  effect/process/ChildProcessSpawner and was renamed.
- `CommandExecutor.Process` -> `ChildProcessSpawner.ChildProcessHandle`:
  Running-process handles were renamed and moved to ChildProcessSpawner.
- `CommandExecutor.Process.Id` -> `ChildProcessSpawner.ProcessId`: The
  process-id brand is now exported directly.
- `CommandExecutor.ProcessTypeId` -> `none`: The ChildProcessHandle marker is
  internal in v4; use the ChildProcessHandle interface.
- `CommandExecutor.TypeId` -> `none`: The Context.Service class replaces the
  public executor type-id alias.
- `CommandExecutor.makeExecutor` -> `ChildProcessSpawner.make`: Use the renamed
  constructor; it derives output helpers from a spawn implementation.
