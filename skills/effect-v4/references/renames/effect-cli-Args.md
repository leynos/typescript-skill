<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/Args` v3 → v4

- `Args.All.ArgsAny` -> `Param.AnyArgument`: Use the shared
  any-positional-parameter type.
- `Args.All.Return` -> `Command.Command.Config.Infer`: Infer the output of a
  command config record; standalone argument collections were removed.
- `Args.Args` -> `Argument.Argument`: Args was renamed to Argument in
  effect/cli.
- `Args.Args.BaseArgsConfig` -> `name: string`: Argument constructors now take
  the name as a required first parameter.
- `Args.Args.FormatArgsConfig` -> `Primitive.FileParseOptions`: Pass the name
  separately and use the format option with Argument.FileParse or
  Argument.FileSchema.
- `Args.Args.PathArgsConfig` -> `Argument.Path(name, { pathType, mustExist })`:
  Path options are inline; map exists=yes to mustExist=true and either to
  omission. exists=no has no exact replacement.
- `Args.Args.Variance` -> `Argument.Argument`: The separate variance artifact
  was removed; Argument inherits the shared Param variance.
- `Args.ArgsTypeId` ->
  `Param.isParam(value) && value.kind === Param.argumentKind`: The public Args
  type id was removed; use the Param guard and argument kind discriminator.
- `Args.all` -> `Command.make(name, config)`: Collect arguments in the config
  record passed to Command.make; there is no standalone Argument.all.
- `Args.atLeast` -> `Argument.atLeast`: Use the moved combinator; v4 returns
  ReadonlyArray and does not encode non-emptiness in the type.
- `Args.atMost` -> `Argument.atMost`: Use the moved combinator.
- `Args.between` -> `Argument.between`: Use the moved combinator; v4 validates
  bounds when constructing the parameter.
- `Args.boolean` -> `Flag.Boolean / Argument.ChoiceWithValue`: Positional
  booleans were removed as ambiguous; prefer a boolean flag or explicit
  true/false positional choices.
- `Args.choice` -> `Argument.Literals`: Use the renamed constructor and pass
  the argument name explicitly.
- `Args.date` -> `Argument.Date`: Use the renamed constructor and pass the
  argument name explicitly.
- `Args.directory` -> `Argument.Directory`: Use mustExist=true for exists=yes
  and omit it for either; exists=no has no exact replacement.
- `Args.file` -> `Argument.File`: Use mustExist=true for exists=yes and omit it
  for either; exists=no has no exact replacement.
- `Args.fileContent` -> `Argument.File + Argument.mapEffect`: Parse a path and
  read it with FileSystem.readFile; no binary-content argument constructor
  remains.
- `Args.fileParse` -> `Argument.FileParse`: Pass the old format as an options
  field; v4 returns parsed content rather than a path/content tuple.
- `Args.fileSchema` -> `Argument.FileSchema`: Pass the old format as an options
  field and use a v4 Schema constraint decoder.
- `Args.fileText` -> `Argument.FileText`: Use the renamed constructor; it
  returns content only.
- `Args.float` -> `Argument.Finite`: Use the renamed constructor; it rejects
  non-finite numbers.
- `Args.getHelp` -> `none`: Per-argument help introspection was removed;
  Command generates help internally.
- `Args.getIdentifier` -> `none`: Public argument identifier introspection was
  removed.
- `Args.getMaxSize` -> `none`: Public arity introspection was removed; command
  parsing enforces variadic bounds internally.
- `Args.getMinSize` -> `none`: Public arity introspection was removed; command
  parsing enforces variadic bounds internally.
- `Args.getUsage` -> `none`: The public Usage tree was removed; Command
  generates a usage string internally.
- `Args.integer` -> `Argument.Int`: Use the renamed constructor and pass the
  argument name explicitly.
- `Args.isArgs` -> `Param.isParam(value) && value.kind === Param.argumentKind`:
  Arguments now use the shared Param representation and an explicit kind
  discriminator.
- `Args.map` -> `Argument.map`: Use the moved combinator.
- `Args.mapEffect`: TODO: needs guidance
- `Args.none` -> `omit the config entry`: V4 Argument.Never is an
  always-failing sentinel, not v3's empty successful argument set.
- `Args.optional` -> `Argument.optional`: Use the moved combinator; it still
  returns Option.
- `Args.path` -> `Argument.Path`: Path options are inline; map exists=yes to
  mustExist=true and either to omission. exists=no has no exact replacement.
- `Args.redacted` -> `Argument.Redacted`: Use the renamed constructor and pass
  the argument name explicitly.
- `Args.repeated` -> `Argument.variadic`: Renamed to variadic; pass optional
  min and max bounds.
- `Args.secret` -> `Argument.Redacted`: Use Redacted-backed positional input.
- `Args.text` -> `Argument.String`: Renamed to String; pass the argument name
  explicitly.
- `Args.validate` -> `argument.parse({ flags: {}, arguments: args })`: Parsing
  is now a Param method and returns leftover tokens with the value; errors are
  CliError.
- `Args.withDefault` -> `Argument.withDefault`: Use the moved combinator; v4
  also accepts an Effect fallback.
- `Args.withDescription` -> `Argument.withDescription`: Use the moved
  combinator.
- `Args.withFallbackConfig` -> `Argument.withFallbackConfig`: Use the moved
  combinator; invalid configuration becomes CliError.InvalidValue.
- `Args.withSchema` -> `Argument.withSchema`: Use the moved combinator with a
  v4 Schema constraint decoder.
