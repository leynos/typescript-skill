<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/CliApp` v3 → v4

- `CliApp.CliApp` -> `Command.Command`: The separate application wrapper was
  folded into the runnable v4 Command tree.
- `CliApp.CliApp.ConstructorArgs` -> `none`: Build the command with
  Command.make and withDescription, then pass version to Command.run; the old
  app constructor shape was removed.
- `CliApp.make` -> `Command.make`: Build the executable Command directly; there
  is no separate CliApp wrapper.
- `CliApp.run` -> `Command.run`: The CliApp wrapper was removed. Attach the
  execute function with Command.withHandler, then run the Command with its
  version; v4 reads arguments through the CLI environment instead of accepting
  args and execute at this call.
