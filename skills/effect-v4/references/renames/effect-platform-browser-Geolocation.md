<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/Geolocation` v3 → v4

- `Geolocation.ErrorTypeId` -> `none`: The error marker is private in v4;
  discriminate GeolocationError and its tagged reason.
- `Geolocation.Geolocation` -> `Geolocation.Geolocation`: The service remains,
  now as a Context.Service with a private brand.
- `Geolocation.GeolocationError` -> `Geolocation.GeolocationError`: The class
  remains, but reason is now PositionUnavailable, PermissionDenied, or Timeout,
  with the cause stored on that tagged reason.
- `Geolocation.TypeId` -> `none`: The service marker is private in v4; use the
  Geolocation Context.Service value.
