<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/CommandDescriptor` v3 → v4

- `CommandDescriptor.Command.ComputeParsedType` -> `Types.Simplify`: Use the
  general simplification utility, or Command.Command.Config.Infer for command
  config.
- `CommandDescriptor.Command.GetParsedType` -> `none`: No public parsed-input
  extractor remains; v4 handlers receive inferred config directly.
- `CommandDescriptor.Command.ParsedStandardCommand` -> `none`: The
  name/options/args parsed wrapper was removed; handlers receive inferred
  config directly.
- `CommandDescriptor.Command.ParsedUserInputCommand` -> `none`: The
  descriptor-level prompt command was removed; use Prompt APIs or
  Command.wizard.
- `CommandDescriptor.Command.Subcommands` -> `none`: Compose independently
  handled commands with Command.withSubcommands instead of parsing a tuple
  union.
- `CommandDescriptor.Command.Variance` -> `Command.Command.Variance`: The
  command variance helper remains conceptually, now tracking input, error, and
  requirements.
- `CommandDescriptor.TypeId` -> `Command.isCommand`: The type id is internal in
  v4; use the public runtime guard.
- `CommandDescriptor.getBashCompletions` -> `Completions.generate`: Completion
  generation moved to one shell-parameterized function; command conversion is
  internal.
- `CommandDescriptor.getFishCompletions` -> `Completions.generate`: Completion
  generation moved to one shell-parameterized function; command conversion is
  internal.
- `CommandDescriptor.getHelp` -> `none`: Help generation is internal to the
  Command runner.
- `CommandDescriptor.getNames` ->
  `Command.Command.name / Command.Command.alias`: Read the public fields; no
  HashSet accessor remains.
- `CommandDescriptor.getSubcommands` -> `Command.Command.subcommands`: Read the
  public grouped subcommands field.
- `CommandDescriptor.getUsage` -> `none`: Usage generation is internal to
  Command help generation.
- `CommandDescriptor.getZshCompletions` -> `Completions.generate`: Completion
  generation moved to one shell-parameterized function; command conversion is
  internal.
- `CommandDescriptor.make` -> `Command.make`: The descriptor and executable
  command layers were merged into one constructor.
- `CommandDescriptor.map` -> `none`: Map individual Argument or Flag values, or
  transform inside the command handler.
- `CommandDescriptor.mapEffect` -> `none`: Use parameter mapEffect where the
  transformation belongs to an input, or perform the Effect in the handler.
- `CommandDescriptor.parse` -> `Command.runWith`: Parsing was folded into
  execution and no intermediate CommandDirective is returned.
- `CommandDescriptor.withDescription` -> `Command.withDescription`: Use the
  retained behavior; v4 descriptions are strings.
