<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/CliConfig` v3 → v4

- `CliConfig.CliConfig` -> `CliConfig.CliConfig.Service`: The service was
  redesigned to configure built-in global flags; old parser and help switches
  were removed.
- `CliConfig.defaultConfig` -> `CliConfig.defaults`: Renamed to defaults with
  the redesigned service shape.
- `CliConfig.defaultLayer` -> `CliConfig.layer`: Call CliConfig.layer() to
  provide the defaults.
- `CliConfig.layer` -> `CliConfig.layer`: The layer constructor remains, but
  its options configure the redesigned CliConfig.Service for built-in global
  flags.
- `CliConfig.make` -> `CliConfig.make`: The constructor remains but accepts the
  redesigned service options.
- `CliConfig.normalizeCase` -> `none`: Case normalization is no longer
  configurable through CliConfig.
