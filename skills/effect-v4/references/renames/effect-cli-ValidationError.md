<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/ValidationError` v3 → v4

- `ValidationError.CommandMismatch` -> `none`: The root-command mismatch error
  was removed.
- `ValidationError.CorrectedFlag` -> `CliError.UnrecognizedOption`: Use the
  unrecognized-option class and its suggestions field.
- `ValidationError.HelpRequested` -> `CliError.ShowHelp`: Renamed and
  redesigned as ShowHelp.
- `ValidationError.InvalidArgument` ->
  `CliError.InvalidValue | CliError.UnexpectedArgument`: Argument decoding and
  leftover operands are separate v4 errors.
- `ValidationError.InvalidValue` -> `CliError.InvalidValue`: Use the
  schema-backed v4 error class.
- `ValidationError.MissingFlag` -> `CliError.MissingOption`: Renamed to
  MissingOption.
- `ValidationError.MissingSubcommand` -> `none`: The dedicated
  missing-subcommand error was removed.
- `ValidationError.MissingValue` -> `CliError.InvalidValue`: The dedicated tag
  was folded into InvalidValue.
- `ValidationError.MultipleValuesDetected` -> `CliError.InvalidValue`: Count
  violations are summarized as InvalidValue without preserving the old values
  array.
- `ValidationError.NoBuiltInMatch` -> `none`: The intermediate built-in
  matching error was removed.
- `ValidationError.UnclusteredFlag` -> `none`: The public cluster error was
  removed.
- `ValidationError.ValidationError` -> `CliError.CliError`: The validation
  union was redesigned and renamed to CliError.
- `ValidationError.ValidationError.Proto` -> `none`: V4 errors are
  schema-backed classes and expose no shared public prototype type.
- `ValidationError.ValidationErrorTypeId` -> `none`: The CliError type id is
  private; use CliError.isCliError.
- `ValidationError.commandMismatch` -> `none`: V4 runners receive arguments
  after the root name; unknown child commands use CliError.UnknownSubcommand.
- `ValidationError.correctedFlag` ->
  `new CliError.UnrecognizedOption({ option, command, suggestions })`:
  Suggestions are carried by UnrecognizedOption; there is no separate
  corrected-flag case.
- `ValidationError.helpRequested` ->
  `new CliError.ShowHelp({ commandPath, errors: [] })`: Help requests now carry
  a command path and optional underlying errors.
- `ValidationError.invalidArgument` ->
  `new CliError.InvalidValue({ option, value, expected, kind: "argument" })`:
  Use InvalidValue for undecodable arguments and UnexpectedArgument for
  leftover operands.
- `ValidationError.invalidValue` ->
  `new CliError.InvalidValue({ option, value, expected, kind })`: Replace the
  HelpDoc payload with structured option, value, expected, and kind fields.
- `ValidationError.isCommandMismatch` -> `none`: The root-command mismatch
  error was removed.
- `ValidationError.isCorrectedFlag` ->
  `error._tag === "UnrecognizedOption" && error.suggestions.length > 0`: Check
  the v4 tag and suggestions array.
- `ValidationError.isHelpRequested` -> `error._tag === "ShowHelp"`: Narrow the
  CliError union by its tag.
- `ValidationError.isInvalidArgument` ->
  `(error._tag === "InvalidValue" && error.kind === "argument") || error._tag === "UnexpectedArgument"`:
  Check both v4 argument error forms.
- `ValidationError.isInvalidValue` -> `error._tag === "InvalidValue"`: Narrow
  the CliError union by its tag.
- `ValidationError.isMissingFlag` -> `error._tag === "MissingOption"`:
  MissingFlag was renamed to MissingOption.
- `ValidationError.isMissingSubcommand` -> `none`: Missing subcommands now
  cause ShowHelp rather than a dedicated error.
- `ValidationError.isMissingValue` ->
  `error._tag === "InvalidValue" && error.value === ""`: Missing values are
  represented as InvalidValue with an empty value.
- `ValidationError.isMultipleValuesDetected` -> `none`: Count violations are
  summarized as InvalidValue without a stable subtype.
- `ValidationError.isNoBuiltInMatch` -> `none`: Built-ins are GlobalFlag
  definitions and the intermediate failure was removed.
- `ValidationError.isUnclusteredFlag` -> `none`: Cluster expansion is internal
  and has no public intermediate error.
- `ValidationError.isValidationError` -> `CliError.isCliError`: Use the renamed
  union guard.
- `ValidationError.keyValuesDetected` ->
  `new CliError.InvalidValue({ option, value, expected, kind: "flag" })`:
  Represent count violations with structured InvalidValue fields.
- `ValidationError.missingFlag` -> `new CliError.MissingOption({ option })`:
  MissingFlag was renamed to MissingOption.
- `ValidationError.missingSubcommand` -> `none`: A parent without a selected
  subcommand now shows help rather than emitting a dedicated error.
- `ValidationError.missingValue` ->
  `new CliError.InvalidValue({ option, value: "", expected, kind })`: Missing
  values are represented as InvalidValue with an empty value.
- `ValidationError.noBuiltInMatch` -> `none`: Built-ins are GlobalFlag
  definitions and the intermediate failure was removed.
- `ValidationError.unclusteredFlag` -> `none`: Flag cluster expansion is
  internal in v4.
