<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/BuiltInOptions` v3 → v4

- `BuiltInOptions.BuiltInOptions` -> `GlobalFlag.BuiltIn`: The parsed directive
  union became a union of global Action and Setting definitions.
- `BuiltInOptions.BuiltInOptions.ShellType` -> `Completions.Shell`: The shell
  union moved to Completions.
- `BuiltInOptions.SetLogLevel` -> `GlobalFlag.LogLevel`: Log level is now a
  global Setting whose parsed value is provided through context.
- `BuiltInOptions.ShowCompletions` -> `GlobalFlag.Completions`: The directive
  payload was replaced by a global completion action definition.
- `BuiltInOptions.ShowHelp` -> `GlobalFlag.Help`: The directive payload was
  replaced by a global help action definition.
- `BuiltInOptions.ShowVersion` -> `GlobalFlag.Version`: The directive value was
  replaced by a global version action definition.
- `BuiltInOptions.ShowWizard` -> `GlobalFlag.Wizard`: The directive payload was
  replaced by a global wizard action definition.
- `BuiltInOptions.builtInOptions` -> `GlobalFlag.BuiltIns`: Built-ins are
  global flag definitions consumed automatically by Command.run and
  Command.runWith.
- `BuiltInOptions.isShowCompletions` -> `none`: Parsed ShowCompletions
  directives were removed; the runner processes GlobalFlag.Completions directly.
- `BuiltInOptions.isShowHelp` -> `none`: Parsed ShowHelp directives were
  removed; the runner processes GlobalFlag.Help directly.
- `BuiltInOptions.isShowVersion` -> `none`: Parsed ShowVersion directives were
  removed; the runner processes GlobalFlag.Version directly.
- `BuiltInOptions.isShowWizard` -> `none`: Parsed ShowWizard directives were
  removed; the runner processes GlobalFlag.Wizard directly.
- `BuiltInOptions.showCompletions` -> `GlobalFlag.Completions`: Use the
  built-in completion action; the shell is parsed from --completions.
- `BuiltInOptions.showHelp` -> `GlobalFlag.Help`: Use the built-in help action;
  usage and help are derived from the active Command.
- `BuiltInOptions.showVersion` -> `GlobalFlag.Version`: Use the built-in
  version action; supply the version to Command.run or Command.runWith.
- `BuiltInOptions.showWizard` -> `GlobalFlag.Wizard`: Use the built-in wizard
  action; runner context supplies the active Command.
