<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiGroup` v3 → v4

- `HttpApiGroup.ApiGroup` -> `effect/http-api/HttpApiGroup#Service`: Renamed;
  the service field and type parameter are now identifier rather than name.
- `HttpApiGroup.HttpApiGroup.AddContext` -> `none`: Groups no longer carry
  arbitrary context. Use AddMiddleware for middleware service transformations.
- `HttpApiGroup.HttpApiGroup.Any` -> `effect/http-api/HttpApiGroup#Constraint`:
  Renamed widened structural constraint.
- `HttpApiGroup.HttpApiGroup.AnyWithProps` ->
  `effect/http-api/HttpApiGroup#Top`: Renamed widened runtime-property type.
- `HttpApiGroup.HttpApiGroup.ClientContext` ->
  `effect/http-api/HttpApiGroup#ClientServices / ErrorServicesDecode / MiddlewareClient`:
  Client schema services and required client middleware are separate
  extractors in v4.
- `HttpApiGroup.HttpApiGroup.Context` -> `none`: Group error and context
  generics were removed; derive server requirements from the group's endpoints.
- `HttpApiGroup.HttpApiGroup.ContextWithName` -> `none`: Select with
  WithIdentifier and derive endpoint server requirements; groups no longer have
  a context generic.
- `HttpApiGroup.HttpApiGroup.EndpointsWithName` ->
  `effect/http-api/HttpApiGroup#EndpointsWithIdentifier`: Direct rename from
  name to identifier.
- `HttpApiGroup.HttpApiGroup.Error` -> `none`: Group-level errors were removed.
  Declare shared errors on each endpoint or through middleware.
- `HttpApiGroup.HttpApiGroup.ErrorContext` ->
  `effect/http-api/HttpApiGroup#ErrorServicesEncode / ErrorServicesDecode`: The
  closest endpoint-error aggregate splits server encoding from client decoding
  services.
- `HttpApiGroup.HttpApiGroup.ErrorWithName` -> `none`: Group-level errors were
  removed; select with WithIdentifier and inspect Errors over the selected
  endpoints.
- `HttpApiGroup.HttpApiGroup.Middleware` ->
  `effect/http-api/HttpApiEndpoint#Middleware`: Middleware is attached to the
  endpoints present when group.middleware is called; extract it from group
  endpoints.
- `HttpApiGroup.HttpApiGroup.MiddlewareWithName` ->
  `effect/http-api/HttpApiEndpoint#Middleware`: Select the group with
  WithIdentifier, get its endpoints, then apply the endpoint Middleware
  extractor.
- `HttpApiGroup.HttpApiGroup.Provides` ->
  `effect/http-api/HttpApiGroup#MiddlewareProvides`: Renamed; derives provided
  services from endpoint middleware.
- `HttpApiGroup.HttpApiGroup.ToService` ->
  `effect/http-api/HttpApiGroup#ToService`: Same role and now produces
  Service\<ApiId, Identifier\>.
- `HttpApiGroup.HttpApiGroup.WithName` ->
  `effect/http-api/HttpApiGroup#WithIdentifier`: Direct rename from name to
  identifier.
- `HttpApiGroup.TypeId` -> `none`: The group type ID is private; use
  HttpApiGroup.isHttpApiGroup for runtime narrowing.
- `HttpApiGroup.make` -> `effect/http-api/HttpApiGroup#make`: The constructor
  remains; group error and context generics are gone and add is variadic.
