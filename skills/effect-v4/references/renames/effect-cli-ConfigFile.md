<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/ConfigFile` v3 → v4

- `ConfigFile.ConfigErrorTypeId` -> `none`: ConfigProvider.SourceError has no
  public type-id export.
- `ConfigFile.ConfigFileError` -> `ConfigProvider.SourceError`: Use the general
  source error when implementing a custom file-backed provider.
- `ConfigFile.layer` -> `ConfigProvider.layerAdd(customProviderEffect)`: Build
  the provider explicitly and add it as fallback to preserve the v3 composition
  order.
- `ConfigFile.makeProvider` -> `none`: V4 has no API that discovers, parses,
  and composes config files; use FileSystem, a format parser, and
  ConfigProvider.fromUnknown explicitly.
