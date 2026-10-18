<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/Command` v3 → v4

- `Command.Command.Config`: TODO: needs guidance
- `Command.Command.Context` -> `Command.CommandContext`: Renamed to
  CommandContext.
- `Command.Command.ParseConfig` -> `Command.Command.Config.Infer`: Use the v4
  command-config inference helper.
- `Command.Command.ParseConfigValue` -> `Command.Command.Config.InferValue`:
  Use the v4 command-config value inference helper.
- `Command.Command.ParsedConfig` -> `none`: The parsed config representation is
  internal in v4.
- `Command.Command.ParsedConfigNode` -> `none`: The parsed config node
  representation is internal in v4.
- `Command.Command.ParsedConfigTree` -> `none`: The parsed config tree
  representation is internal in v4.
- `Command.Command.Transform` -> `none`: The handler transformation type and
  machinery are internal in v4.
- `Command.TypeId` -> `Command.isCommand`: The type id is internal in v4; use
  the public runtime guard.
- `Command.fromDescriptor` -> `Command.make`: The descriptor layer was folded
  into Command; define config and handler directly on Command.make.
- `Command.getBashCompletions` -> `Completions.generate`: Generation now
  returns one script string; normally use GlobalFlag.Completions through the
  runner.
- `Command.getFishCompletions` -> `Completions.generate`: Generation now
  returns one script string; normally use GlobalFlag.Completions through the
  runner.
- `Command.getHelp` -> `none`: Help generation for a command path is internal;
  use GlobalFlag.Help through Command.run or runWith.
- `Command.getNames` -> `Command.Command.name / Command.Command.alias`: Read
  the public name and optional alias fields; no HashSet accessor remains.
- `Command.getSubcommands` -> `Command.Command.subcommands`: Read the public
  grouped subcommands field; its shape is no longer a name map.
- `Command.getUsage` -> `none`: Usage is generated internally as part of
  structured HelpDoc.
- `Command.getZshCompletions` -> `Completions.generate`: Generation now returns
  one script string; normally use GlobalFlag.Completions through the runner.
- `Command.make` -> `Command.make`: Use the redesigned constructor with one
  nested config object of Argument and Flag values.
- `Command.run` -> `Command.runWith`: Use runWith for the v3-style function
  that accepts an argv array; use run to read arguments from Stdio.
- `Command.transformHandler` -> `none`: Transform in the handler or use the
  specific provide combinators; the generic handler transform is internal.
- `Command.withDescription` -> `Command.withDescription`: Use the retained
  combinator; v4 descriptions are strings rather than the old HelpDoc ADT.
