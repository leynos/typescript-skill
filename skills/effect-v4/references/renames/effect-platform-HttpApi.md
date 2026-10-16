<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApi` v3 → v4

- `HttpApi.Api` -> `none`: The Context tag carrying the API was removed. Pass
  the HttpApi value explicitly to builders and clients.
- `HttpApi.HttpApi.Any` -> `effect/http-api/HttpApi#Constraint`: Use the erased
  marker constraint when only HttpApi identity is needed.
- `HttpApi.HttpApi.AnyWithProps` -> `effect/http-api/HttpApi#Top`: Use the
  widened HttpApi type that retains runtime properties.
- `HttpApi.TypeId` -> `none`: The marker is private in v4; use
  HttpApi.isHttpApi for runtime narrowing and Constraint or Top for types.
- `HttpApi.make` -> `effect/http-api/HttpApi#make`: The constructor remains,
  but API-wide error and service parameters were removed; declare errors on
  endpoints and attach middleware.
