<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Etag` v3 → v4

- `Etag.GeneratorTypeId` -> `Etag.Generator`: The standalone generator brand
  was removed; Generator is now a Context.Service class.
- `Etag.layer` -> `Etag.layer`: Retained; it still provides the strong
  metadata-based ETag Generator service.
