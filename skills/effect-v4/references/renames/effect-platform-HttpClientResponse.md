<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpClientResponse` v3 → v4

- `HttpClientResponse.HttpClientResponse` ->
  `HttpClientResponse.HttpClientResponse`: Custom implementations must supply
  the required url string. It represents the resolved URL including query
  parameters and excluding the hash, uses the final URL after redirects, and is
  empty when unknown.
- `HttpClientResponse.TypeId` -> `typeof HttpClientResponse.TypeId`: TypeId
  remains public but is now a string constant; use typeof in type position.
- `HttpClientResponse.filterStatus` -> `HttpClientResponse.filterStatus`:
  Retained; rejected status now fails with an HttpClientError wrapper.
- `HttpClientResponse.filterStatusOk` -> `HttpClientResponse.filterStatusOk`:
  Retained; non-2xx status now fails with an HttpClientError wrapper.
- `HttpClientResponse.schemaBodyJson` -> `HttpClientResponse.schemaBodyJson`:
  Retained with v4 Schema constraints and SchemaError failures.
- `HttpClientResponse.schemaBodyUrlParams` ->
  `HttpClientResponse.schemaBodyUrlParams`: Retained with ConstraintCodec input
  and SchemaError failures.
- `HttpClientResponse.schemaHeaders` -> `HttpClientResponse.schemaHeaders`:
  Retained with ConstraintCodec input and SchemaError failures.
- `HttpClientResponse.schemaJson` -> `HttpClientResponse.schemaJson`: Retained
  with ConstraintCodec input and v4 error types.
- `HttpClientResponse.schemaNoBody` -> `HttpClientResponse.schemaNoBody`:
  Retained with Schema.Codec input and SchemaError failures.
- `HttpClientResponse.stream` -> `HttpClientResponse.stream`: Retained; body
  failures now use the broader HttpClientError wrapper.
