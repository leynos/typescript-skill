<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/Permissions` v3 → v4

- `Permissions.ErrorTypeId` -> `none`: The error marker is private in v4;
  discriminate PermissionsError and its tagged reason.
- `Permissions.Permissions` -> `Permissions.Permissions`: The query service
  remains, now as a Context.Service with a private brand.
- `Permissions.PermissionsError` -> `Permissions.PermissionsError`: The class
  remains, but reason is now PermissionsInvalidStateError or
  PermissionsTypeError, with the cause stored on that tagged reason.
- `Permissions.TypeId` -> `none`: The service marker is private in v4; use the
  Permissions Context.Service value.
