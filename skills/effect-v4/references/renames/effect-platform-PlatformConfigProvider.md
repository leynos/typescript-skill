<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/PlatformConfigProvider` v3 → v4

- `PlatformConfigProvider.fromFileTree` -> `ConfigProvider.fromDir`: The
  provider moved into effect/ConfigProvider and was renamed; rootDirectory is
  now rootPath.
- `PlatformConfigProvider.layerDotEnv` ->
  `ConfigProvider.layer(ConfigProvider.fromDotEnv({ path }))`: Use the v4
  dotenv provider effect and install it with ConfigProvider.layer.
- `PlatformConfigProvider.layerDotEnvAdd` ->
  `ConfigProvider.layerAdd(ConfigProvider.fromDotEnv({ path }))`: Use the v4
  dotenv provider effect and compose it with ConfigProvider.layerAdd.
- `PlatformConfigProvider.layerFileTree` ->
  `ConfigProvider.layer(ConfigProvider.fromDir({ rootPath }))`: Use the renamed
  directory-tree provider and install it with ConfigProvider.layer.
- `PlatformConfigProvider.layerFileTreeAdd` ->
  `ConfigProvider.layerAdd(ConfigProvider.fromDir({ rootPath }))`: Use the
  renamed directory-tree provider and compose it with ConfigProvider.layerAdd.
