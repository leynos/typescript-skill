<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpServerRequest` v3 → v4

- `HttpServerRequest.ParsedSearchParams` ->
  `HttpServerRequest.ParsedSearchParams`: The marker and tag became one
  Context.Service class.
- `HttpServerRequest.TypeId` -> `typeof HttpServerRequest.TypeId`: TypeId
  remains public but is now a string constant; use typeof in type position.
- `HttpServerRequest.fromWeb` -> `HttpServerRequest.fromWeb`: Retained for
  wrapping a Web Request.
- `HttpServerRequest.persistedMultipart` ->
  `HttpServerRequest.HttpServerRequest.use((request) => request.multipart)`:
  Use the request service's `.use` helper to return its cached multipart effect.
- `HttpServerRequest.schemaBodyJson` -> `HttpServerRequest.schemaBodyJson`:
  Retained with v4 Schema constraints and error types.
- `HttpServerRequest.schemaBodyUrlParams` ->
  `HttpServerRequest.schemaBodyUrlParams`: Retained with ConstraintCodec input
  and v4 error types.
- `HttpServerRequest.schemaHeaders` -> `HttpServerRequest.schemaHeaders`:
  Retained with ConstraintCodec input and SchemaError failures.
- `HttpServerRequest.toWeb` -> `HttpServerRequest.toWeb`: Retained and captures
  the current Context for streamed bodies.
- `HttpServerRequest.toWebEither` -> `HttpServerRequest.toWebResult`: Either
  became Result, and the optional Runtime became an optional Context.
