<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/Options` v3 → v4

- `Options.All.OptionsAny` -> `Param.AnyFlag`: Use the shared
  any-flag-parameter type.
- `Options.All.Return` -> `Command.Command.Config.Infer`: Infer the output of a
  command config record; standalone flag collections were removed.
- `Options.Options` -> `Flag.Flag`: Options was renamed to Flag in effect/cli.
- `Options.Options.BooleanOptionsConfig` ->
  `Flag.Boolean + Flag.withAlias + Flag.map`: The config object was removed;
  aliases and value inversion are combinators, while custom negation names need
  application logic.
- `Options.Options.PathOptionsConfig` -> `{ readonly mustExist?: boolean }`:
  Path options are inline; true replaces exists=yes and omission replaces
  either. exists=no has no exact replacement.
- `Options.Options.Variance` -> `Flag.Flag`: The separate variance artifact was
  removed; Flag inherits the shared Param variance.
- `Options.OptionsTypeId` ->
  `Param.isParam(value) && value.kind === Param.flagKind`: The public Options
  type id was removed; use the Param guard and flag kind discriminator.
- `Options.all` -> `Command.make(name, config)`: Collect flags in the config
  record passed to Command.make; there is no standalone Flag.all.
- `Options.atLeast` -> `Flag.atLeast`: Use the moved combinator; v4 returns
  ReadonlyArray rather than NonEmptyArray.
- `Options.atMost` -> `Flag.atMost`: Use the moved combinator.
- `Options.between` -> `Flag.between`: Use the moved combinator; v4 validates
  bounds when constructing the parameter.
- `Options.boolean` -> `Flag.Boolean + Flag.withDefault`: Use
  Flag.Boolean(name).pipe(Flag.withDefault(false)) to preserve v3's
  omitted-flag default; bare Flag.Boolean is now required. --no-name is
  automatic and aliases are added with Flag.withAlias.
- `Options.choice` -> `Flag.Literals`: Use the moved constructor.
- `Options.choiceWithValue` -> `Flag.ChoiceWithValue`: Use the moved
  constructor.
- `Options.date` -> `Flag.Date`: Use the moved constructor.
- `Options.directory` -> `Flag.Directory`: Use mustExist=true for exists=yes
  and omit it for either; exists=no has no exact replacement.
- `Options.file` -> `Flag.File`: Use mustExist=true for exists=yes and omit it
  for either; exists=no has no exact replacement.
- `Options.fileContent` -> `Flag.File + Flag.mapEffect`: Parse a path and read
  it with FileSystem.readFile; no binary-content flag constructor remains.
- `Options.fileParse` -> `Flag.FileParse`: Pass the old format as an options
  field; v4 returns parsed content rather than a path/content tuple.
- `Options.fileSchema` -> `Flag.FileSchema`: Pass the old format as an options
  field and use a v4 Schema constraint decoder.
- `Options.fileText` -> `Flag.File + Flag.mapEffect`: Flag.FileText returns
  content only; read after Flag.File when the path/content tuple must be
  preserved.
- `Options.filterMap` -> `Flag.filterMap`: Use the moved combinator and replace
  the fixed message with an onNone function.
- `Options.float` -> `Flag.Finite`: Use the moved constructor.
- `Options.getHelp` -> `none`: Per-flag help introspection was removed; Command
  generates help internally.
- `Options.getIdentifier` -> `none`: Public flag identifier introspection was
  removed.
- `Options.getUsage` -> `none`: The public Usage tree was removed; Command
  generates a usage string internally.
- `Options.integer` -> `Flag.Int`: Use the moved constructor.
- `Options.isBool` -> `none`: No public flag-shape predicate remains;
  boolean-shape inspection is internal.
- `Options.isOptions` ->
  `Param.isParam(value) && value.kind === Param.flagKind`: Flags now use the
  shared Param representation and an explicit kind discriminator.
- `Options.keyValueMap` -> `Flag.KeyValuePair`: Renamed and now returns
  Record\<string, string\> rather than HashMap.
- `Options.map` -> `Flag.map`: Use the moved combinator.
- `Options.mapEffect` -> `Flag.mapEffect`: Use the moved combinator; mapping
  failures are CliError.
- `Options.mapTryCatch` -> `Flag.mapTryCatch`: Use the moved combinator;
  onError now returns a string rather than HelpDoc.
- `Options.none` -> `omit the config entry`: V4 Flag.Never is an always-failing
  sentinel, not v3's empty successful option set.
- `Options.optional` -> `Flag.optional`: Use the moved combinator; it still
  returns Option.
- `Options.orElse` -> `Flag.orElse(() => fallback)`: The fallback is now lazy;
  add explicit exclusivity validation if both flags must be rejected.
- `Options.orElseEither` -> `Flag.orElseResult(() => fallback)`: Either became
  Result and the fallback is lazy; v4 no longer rejects both flags being
  present.
- `Options.parse` -> `flag.parse({ flags, arguments: [] })`: Parsing is now a
  Param method over a Record and returns leftover arguments with the value;
  errors are CliError.
- `Options.processCommandLine` -> `Command.runWith`: Raw argv processing is now
  whole-command execution; no public standalone flag tokenizer remains.
- `Options.redacted` -> `Flag.Redacted`: Use the moved constructor.
- `Options.repeated` -> `Flag.variadic`: Renamed to variadic; pass optional min
  and max bounds.
- `Options.secret` -> `Flag.Redacted`: The deprecated Secret constructor was
  removed; use Redacted-backed input.
- `Options.text` -> `Flag.String`: Renamed from text to String.
- `Options.withAlias` -> `Flag.withAlias`: Use the moved combinator.
- `Options.withDefault` -> `Flag.withDefault`: Use the moved combinator; v4
  also accepts an Effect fallback.
- `Options.withDescription` -> `Flag.withDescription`: Use the moved combinator.
- `Options.withFallbackConfig` -> `Flag.withFallbackConfig`: Use the moved
  combinator; invalid configuration becomes CliError.InvalidValue.
- `Options.withFallbackPrompt` -> `Flag.withFallbackPrompt`: Use the moved
  combinator; v4 can construct the Prompt lazily in Effect.
- `Options.withPseudoName` -> `Flag.withMetavar`: Renamed to withMetavar.
- `Options.withSchema` -> `Flag.withSchema`: Use the moved combinator with a v4
  Schema constraint decoder.
