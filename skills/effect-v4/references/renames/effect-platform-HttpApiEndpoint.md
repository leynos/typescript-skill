<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiEndpoint` v3 → v4

- `HttpApiEndpoint.HttpApiEndpoint` ->
  `effect/http-api/HttpApiEndpoint#HttpApiEndpoint`: The model remains, but its
  generics now carry path literals, schemas, middleware, and middleware
  services.
- `HttpApiEndpoint.HttpApiEndpoint.AddContext` ->
  `effect/http-api/HttpApiEndpoint#AddMiddleware`: Use AddMiddleware to add a
  middleware identifier and compute its service transformation.
- `HttpApiEndpoint.HttpApiEndpoint.AddError` -> `none`: Declare error schemas
  in the endpoint constructor options; the type helper and fluent addError
  method were removed.
- `HttpApiEndpoint.HttpApiEndpoint.Constructor` -> `none`: The tagged-template
  constructor type was removed; use HttpApiEndpoint.make(method)(identifier,
  path, options?).
- `HttpApiEndpoint.HttpApiEndpoint.Context` ->
  `effect/http-api/HttpApiEndpoint#ServerServices`: Use ServerServices for
  handler requirements; middleware IDs and extra requirements have separate
  extractors.
- `HttpApiEndpoint.HttpApiEndpoint.ContextWithName` ->
  `effect/http-api/HttpApiEndpoint#ServerServicesWithIdentifier`: Name became
  Identifier; combine with middleware extractors when the complete handler
  requirement union is needed.
- `HttpApiEndpoint.HttpApiEndpoint.Error` ->
  `effect/http-api/HttpApiEndpoint#Errors`: Use Errors for the decoded endpoint
  and middleware error union; v4 Error extracts the schema.
- `HttpApiEndpoint.HttpApiEndpoint.ErrorContext` ->
  `effect/http-api/HttpApiEndpoint#ErrorServicesEncode / ErrorServicesDecode`:
  The single schema context split into server encoding and client decoding
  services.
- `HttpApiEndpoint.HttpApiEndpoint.ErrorContextWithName` ->
  `effect/http-api/HttpApiEndpoint#ErrorServicesEncode / ErrorServicesDecode`:
  Select the endpoint with WithIdentifier, then apply the encode or decode
  service extractor.
- `HttpApiEndpoint.HttpApiEndpoint.ErrorWithName` ->
  `effect/http-api/HttpApiEndpoint#ErrorsWithIdentifier`: Renamed for
  identifier and returns the decoded endpoint plus middleware error union.
- `HttpApiEndpoint.HttpApiEndpoint.ExcludeName` ->
  `effect/http-api/HttpApiEndpoint#ExcludeIdentifier`: Direct rename from name
  to identifier.
- `HttpApiEndpoint.HttpApiEndpoint.ExtractPath` -> `none`: Tagged-template path
  extraction was removed. Put a params schema or field record in constructor
  option params.
- `HttpApiEndpoint.HttpApiEndpoint.HandlerRawWithName` ->
  `effect/http-api/HttpApiEndpoint#HandlerRawWithIdentifier`: Direct rename;
  raw request fields are now params and query.
- `HttpApiEndpoint.HttpApiEndpoint.HandlerWithName` ->
  `effect/http-api/HttpApiEndpoint#HandlerWithIdentifier`: Direct rename from
  name to identifier.
- `HttpApiEndpoint.HttpApiEndpoint.OptionalTypePropertySignature` -> `none`:
  Removed with the tagged-template path implementation.
- `HttpApiEndpoint.HttpApiEndpoint.PathEntries` -> `none`: Removed with
  tagged-template path extraction; declare endpoint params explicitly.
- `HttpApiEndpoint.HttpApiEndpoint.PathParsed` ->
  `effect/http-api/HttpApiEndpoint#Params`: Path data became params; Params
  extracts the schema, so use Params\<Endpoint\>["Type"] for decoded data.
- `HttpApiEndpoint.HttpApiEndpoint.Payload` ->
  `effect/http-api/HttpApiEndpoint#Payload`: The name remains but now extracts
  the schema; use Payload\<Endpoint\>["Type"] for buffered decoded data.
- `HttpApiEndpoint.HttpApiEndpoint.Success` ->
  `effect/http-api/HttpApiEndpoint#SuccessWithIdentifier`: Use
  SuccessWithIdentifier for the decoded, stream-aware result; v4 Success
  extracts the schema.
- `HttpApiEndpoint.HttpApiEndpoint.SuccessWithName` ->
  `effect/http-api/HttpApiEndpoint#SuccessWithIdentifier`: Direct rename from
  name to identifier; the result remains decoded and stream-aware.
- `HttpApiEndpoint.HttpApiEndpoint.UrlParams` ->
  `effect/http-api/HttpApiEndpoint#Query`: urlParams became query; Query
  extracts the schema, so use Query\<Endpoint\>["Type"] for decoded data.
- `HttpApiEndpoint.HttpApiEndpoint.ValidateHeaders` ->
  `effect/http-api/HttpApiEndpoint#HeadersConstraint`: Validation moved from an
  intersection helper to a constructor generic constraint.
- `HttpApiEndpoint.HttpApiEndpoint.ValidateParams` -> `none`: Tagged-template
  interpolation validation was removed; params are declared explicitly in
  options.params.
- `HttpApiEndpoint.HttpApiEndpoint.ValidatePath` ->
  `effect/http-api/HttpApiEndpoint#ParamsConstraint`: path became params and
  validation is now a constructor constraint.
- `HttpApiEndpoint.HttpApiEndpoint.ValidatePayload` ->
  `effect/http-api/HttpApiEndpoint#PayloadConstraint`: Payload validation is
  now a method-sensitive constructor constraint.
- `HttpApiEndpoint.HttpApiEndpoint.ValidateUrlParams` ->
  `effect/http-api/HttpApiEndpoint#QueryConstraint`: urlParams became query and
  validation is now a constructor constraint.
- `HttpApiEndpoint.PathSegment` -> `effect/http/HttpRouter#PathInput`: Path
  input moved to the shared router and is generalized to slash-prefixed paths
  or wildcard.
- `HttpApiEndpoint.TypeId` -> `none`: The endpoint type ID is private; use
  HttpApiEndpoint.isHttpApiEndpoint for runtime narrowing.
- `HttpApiEndpoint.get` -> `effect/http-api/HttpApiEndpoint#get`: Use
  get(identifier, path, options?); tagged templates and fluent schema setters
  were removed.
- `HttpApiEndpoint.head` -> `effect/http-api/HttpApiEndpoint#head`: Use
  head(identifier, path, options?); tagged templates and fluent schema setters
  were removed.
- `HttpApiEndpoint.make` -> `effect/http-api/HttpApiEndpoint#make`: The factory
  remains but now requires identifier, path, and options and applies codecs
  unless disabled.
- `HttpApiEndpoint.options` -> `effect/http-api/HttpApiEndpoint#options`: Same
  HTTP method constructor with the new identifier, path, and options signature.
- `HttpApiEndpoint.patch` -> `effect/http-api/HttpApiEndpoint#patch`: Same HTTP
  method constructor with the new identifier, path, and options signature.
- `HttpApiEndpoint.post` -> `effect/http-api/HttpApiEndpoint#post`: Same HTTP
  method constructor with the new identifier, path, and options signature.
- `HttpApiEndpoint.put` -> `effect/http-api/HttpApiEndpoint#put`: Same HTTP
  method constructor with the new identifier, path, and options signature.
