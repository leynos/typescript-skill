<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/OpenApi` v3 → v4

- `OpenApi.AdditionalPropertiesStrategy` -> `none`: OpenApi.fromApi no longer
  accepts generation options; standalone JSON Schema generation has a separate
  additionalProperties option.
- `OpenApi.Exclude` -> `effect/http-api/OpenApi#Exclude`: Same annotation key
  and default; it is now a Context.Reference value.
- `OpenApi.OpenApiSpecContentType` -> `string`: The closed media-type union was
  removed so custom and streaming media types are supported.
- `OpenApi.fromApi` -> `effect/http-api/OpenApi#fromApi`: The operation remains
  and returns OpenAPI 3.1, but the signature is now only fromApi(api).
