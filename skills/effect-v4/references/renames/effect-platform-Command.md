<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Command` v3 → v4

- `Command.Command` -> `ChildProcess.Command`: Commands moved to
  effect/process/ChildProcess and are now directly Effectable to spawn a
  ChildProcessHandle.
- `Command.Command.Input` -> `ChildProcess.CommandInput`: The standard-input
  configuration type was flattened out of the Command namespace.
- `Command.Command.Proto` ->
  `ChildProcess.StandardCommand | ChildProcess.PipedCommand`: The public
  command prototype was removed; narrow the Command union to its
  StandardCommand or PipedCommand interfaces.
- `Command.CommandTypeId` -> `none`: The command type-id alias is internal in
  v4; use ChildProcess.Command or ChildProcess.isCommand instead.
- `Command.env` -> `ChildProcess.setEnv`: Use the renamed command combinator.
- `Command.exitCode` -> `ChildProcessSpawner.ChildProcessSpawner.exitCode`:
  Obtain the ChildProcessSpawner service and call exitCode, or spawn the
  Effectable command and read the handle exitCode.
- `Command.feed` -> `ChildProcess.CommandOptions["stdin"]`: The feed combinator
  was removed; pass a Stream as stdin when constructing the command.
- `Command.flatten` -> `none`: No flatten helper remains; inspect
  StandardCommand and PipedCommand recursively when command structure is
  required.
- `Command.lines` -> `ChildProcessSpawner.ChildProcessSpawner.lines`: Output
  collection moved onto the ChildProcessSpawner service.
- `Command.runInShell` -> `ChildProcess.CommandOptions["shell"]`: Set shell
  when calling ChildProcess.make; there is no post-construction shell
  combinator.
- `Command.start` -> `ChildProcessSpawner.ChildProcessSpawner.spawn`: Use the
  spawner service, or yield the Effectable ChildProcess.Command directly, to
  obtain a ChildProcessHandle.
- `Command.stderr` -> `ChildProcess.CommandOptions["stderr"]`: Configure stderr
  in ChildProcess.make options; the standalone combinator was removed.
- `Command.stdin` -> `ChildProcess.CommandOptions["stdin"]`: Configure stdin in
  ChildProcess.make options; the standalone combinator was removed.
- `Command.stdout` -> `ChildProcess.CommandOptions["stdout"]`: Configure stdout
  in ChildProcess.make options; the standalone combinator was removed.
- `Command.stream` ->
  `ChildProcessSpawner.ChildProcessSpawner.spawn + ChildProcessHandle.stdout`:
  Spawn within a scope and consume the returned handle's stdout stream.
- `Command.streamLines` ->
  `ChildProcessSpawner.ChildProcessSpawner.streamLines`: Text-line streaming
  moved onto the ChildProcessSpawner service.
- `Command.string` -> `ChildProcessSpawner.ChildProcessSpawner.string`: Output
  collection moved onto the ChildProcessSpawner service.
- `Command.workingDirectory` -> `ChildProcess.setCwd`: Use the renamed command
  combinator.
