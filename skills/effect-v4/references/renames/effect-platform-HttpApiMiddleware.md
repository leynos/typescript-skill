<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiMiddleware` v3 → v4

- `HttpApiMiddleware.HttpApiMiddleware` ->
  `effect/http-api/HttpApiMiddleware#HttpApiMiddleware`: The model remains but
  now wraps the response effect and carries provided services, an error schema,
  and required services.
- `HttpApiMiddleware.HttpApiMiddleware.Any` ->
  `effect/http-api/HttpApiMiddleware#AnyService`: Renamed widened middleware
  service-key shape.
- `HttpApiMiddleware.HttpApiMiddleware.AnyId` ->
  `effect/http-api/HttpApiMiddleware#AnyId`: Same name; metadata now includes
  provided and required services, error schema, client error, and client
  requirement.
- `HttpApiMiddleware.HttpApiMiddleware.Error` ->
  `effect/http-api/HttpApiMiddleware#Error`: Same name and now derives the
  decoded type from the configured error schema.
- `HttpApiMiddleware.HttpApiMiddleware.ErrorContext` ->
  `effect/http-api/HttpApiMiddleware#ErrorServicesEncode / ErrorServicesDecode`:
  The single schema context split into server encoding and client decoding
  services.
- `HttpApiMiddleware.HttpApiMiddleware.Only` ->
  `Extract<R, HttpApiMiddleware.AnyId>`: The helper was removed because
  middleware IDs are explicit; use Extract when the direct filter is still
  needed.
- `HttpApiMiddleware.HttpApiMiddleware.Provides` ->
  `effect/http-api/HttpApiMiddleware#Provides`: Same name and reads the
  expanded v4 middleware ID metadata.
- `HttpApiMiddleware.SecurityTypeId` -> `none`: The marker is private; use
  HttpApiMiddleware.isSecurity.
- `HttpApiMiddleware.Tag` -> `effect/http-api/HttpApiMiddleware#Service`:
  Renamed and redesigned; use error, requires, provides, clientError, and
  requiredForClient configuration.
- `HttpApiMiddleware.TagClass` ->
  `effect/http-api/HttpApiMiddleware#ServiceClass`: Renamed class type with the
  new two-stage type configuration and wrapping service shape.
- `HttpApiMiddleware.TagClass.BaseSecurity` ->
  `effect/http-api/HttpApiMiddleware#ServiceClass`: Security is conditional
  metadata on ServiceClass; there is no separate public base interface.
- `HttpApiMiddleware.TagClass.Failure` ->
  `effect/http-api/HttpApiMiddleware#Error`: failure terminology became error;
  apply the extractor to the middleware ID.
- `HttpApiMiddleware.TagClass.FailureContext` ->
  `effect/http-api/HttpApiMiddleware#ErrorServicesEncode / ErrorServicesDecode`:
  Failure schema services split by server encoding and client decoding
  direction.
- `HttpApiMiddleware.TagClass.FailureSchema` ->
  `effect/http-api/HttpApiMiddleware#ErrorSchema`: Renamed and applied to the
  middleware ID rather than constructor options.
- `HttpApiMiddleware.TagClass.FailureService` ->
  `effect/http-api/HttpApiMiddleware#Error`: Use the decoded error extractor;
  optional middleware fallback was removed.
- `HttpApiMiddleware.TagClass.Optional` -> `none`: Optional declaration and
  fallback-on-failure behavior were removed; model fallback in the wrapping
  middleware.
- `HttpApiMiddleware.TagClass.Provides` ->
  `effect/http-api/HttpApiMiddleware#Provides`: Moved to the module level and
  applied to the middleware ID.
- `HttpApiMiddleware.TagClassAny` ->
  `effect/http-api/HttpApiMiddleware#AnyService`: Renamed widened service-key
  type.
- `HttpApiMiddleware.TagClassSecurityAny` ->
  `effect/http-api/HttpApiMiddleware#AnyServiceSecurity`: Renamed widened
  security service-key type.
- `HttpApiMiddleware.TypeId` -> `none`: The marker is private; use public
  guards and type extractors.
