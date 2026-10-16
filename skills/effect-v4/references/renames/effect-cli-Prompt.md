<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/Prompt` v3 → v4

- `Prompt.All.PromptAny` -> `Prompt.Any`: The any-prompt alias moved out of the
  All namespace.
- `Prompt.All.Return` -> `Prompt.All.Return`: The collection result helper
  remains under Prompt.All.
- `Prompt.Prompt` -> `Prompt.Prompt`: The model moved to effect/cli; quitting
  now fails with Terminal.QuitError.
- `Prompt.Prompt.FloatOptions` -> `Prompt.NumberOptions`: Use the renamed
  public options type for Prompt.Number; it still extends the integer options
  type, now IntOptions.
- `Prompt.Prompt.IntegerOptions` -> `Prompt.IntOptions`: Use the renamed public
  options type for Prompt.Int; option fields are preserved.
- `Prompt.Prompt.Variance` -> `Prompt.Prompt`: The named variance artifact was
  removed; use Prompt\<Output\>.
- `Prompt.Prompt.VarianceStruct` -> `Prompt.Prompt`: The named variance
  structure was removed; use Prompt\<Output\>.
- `Prompt.PromptTypeId` -> `Prompt.isPrompt`: The public type-id symbol was
  removed; use the runtime guard.
- `Prompt.confirm` -> `Prompt.Confirm`: Use the renamed constructor.
- `Prompt.custom` -> `Prompt.Custom`: Use the renamed constructor; both
  overloads are preserved.
- `Prompt.date` -> `Prompt.Date`: Use the moved constructor.
- `Prompt.file` -> `Prompt.File`: Use the moved constructor; v4 also supports a
  default selected path.
- `Prompt.float` -> `Prompt.Number`: Use the moved constructor; v4 also
  supports a default value.
- `Prompt.hidden` -> `Prompt.Hidden`: Use the renamed constructor.
- `Prompt.integer` -> `Prompt.Int`: Use the moved constructor; v4 also supports
  a default value.
- `Prompt.list` -> `Prompt.List`: Use the renamed constructor.
- `Prompt.multiSelect` -> `Prompt.MultiSelect`: Use the renamed constructor.
- `Prompt.password` -> `Prompt.Password`: Use the renamed constructor.
- `Prompt.select` -> `Prompt.Select`: Use the renamed constructor.
- `Prompt.text` -> `Prompt.String`: Use the moved constructor.
- `Prompt.toggle` -> `Prompt.Toggle`: Use the renamed constructor.
