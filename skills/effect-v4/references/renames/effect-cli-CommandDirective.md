<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/CommandDirective` v3 → v4

- `CommandDirective.BuiltIn` -> `GlobalFlag.Action`: Use the global action
  definition type; it is processed directly by the runner.
- `CommandDirective.CommandDirective` -> `none`: The intermediate parse-result
  model was removed; the runner invokes the selected handler directly.
- `CommandDirective.UserDefined` -> `none`: The user-defined intermediate
  directive was removed.
- `CommandDirective.builtIn` -> `GlobalFlag.Action`: Define a custom action
  flag; v4 runners no longer return built-in directives.
- `CommandDirective.isBuiltIn` -> `none`: Intermediate built-in directives were
  removed.
- `CommandDirective.map` -> `none`: Map parameters or transform in the handler;
  there is no intermediate directive to map.
- `CommandDirective.userDefined` -> `none`: Parsed input is delivered directly
  to the selected command handler.
