<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ConfigProviderPathPatch` v3 → v4

- `ConfigProviderPathPatch.AndThen` -> `ConfigProvider.mapInput`: PathPatch is
  no longer public; compose path transformations as ordinary functions passed
  to mapInput.
- `ConfigProviderPathPatch.Empty` -> `none`: The PathPatch ADT was removed; an
  unchanged provider represents the identity transformation.
- `ConfigProviderPathPatch.MapName` -> `none`: The PathPatch ADT was removed;
  use a path transformation function with ConfigProvider.mapInput.
- `ConfigProviderPathPatch.Nested` -> `none`: The PathPatch ADT was removed;
  use ConfigProvider.nested on the provider.
- `ConfigProviderPathPatch.PathPatch` ->
  `(path: ConfigProvider.Path) => ConfigProvider.Path`: Path patches are
  ordinary full-path transformations in v4 and are installed with
  ConfigProvider.mapInput.
- `ConfigProviderPathPatch.Unnested` -> `none`: The PathPatch ADT was removed;
  express prefix removal as a ConfigProvider.mapInput function.
- `ConfigProviderPathPatch.empty` -> `ConfigProvider.ConfigProvider`: No
  identity patch value is needed; leave the provider untransformed.
- `ConfigProviderPathPatch.mapName` -> `ConfigProvider.mapInput`: Map the
  string segments of the full ConfigProvider.Path explicitly.
- `ConfigProviderPathPatch.nested` -> `ConfigProvider.nested`: Apply nesting
  directly to the provider instead of constructing a patch.
- `ConfigProviderPathPatch.unnested` -> `ConfigProvider.mapInput`: Strip the
  expected leading path segment in a mapInput callback; v4 has no named
  unnested helper.
