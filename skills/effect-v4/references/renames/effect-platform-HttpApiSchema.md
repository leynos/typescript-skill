<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiSchema` v3 → v4

- `HttpApiSchema.AnnotationEmptyDecodeable` ->
  `effect/http-api/HttpApiSchema#asNoContent`: The public marker was removed;
  represent no-content decoding structurally with asNoContent({ decode }).
- `HttpApiSchema.AnnotationEncoding` ->
  `effect/http-api/HttpApiSchema#asJson / asFormUrlEncoded / asText / asUint8Array`:
  The key is internal; select encoding with a public combinator.
- `HttpApiSchema.AnnotationMultipart` ->
  `effect/http-api/HttpApiSchema#asMultipart`: The symbol annotation became a
  brand plus internal encoding metadata; apply the schema combinator.
- `HttpApiSchema.AnnotationMultipartStream` ->
  `effect/http-api/HttpApiSchema#asMultipartStream`: The symbol annotation
  became a brand plus internal encoding metadata; apply the schema combinator.
- `HttpApiSchema.AnnotationParam` -> `effect/http-api/HttpApiEndpoint#params`:
  Path names now live in the router path and schemas in endpoint option params,
  not schema annotations.
- `HttpApiSchema.AnnotationStatus` -> `effect/http-api/HttpApiSchema#status`:
  The public symbol was removed; apply status(code), which uses the
  httpApiStatus schema annotation.
- `HttpApiSchema.Empty` -> `effect/http-api/HttpApiSchema#Empty`: The API
  remains and returns Schema.Void annotated with the supplied status.
- `HttpApiSchema.EmptyError` -> `effect/Schema#Error`: Define a normal schema
  error with httpApiStatus, then derive its no-content wire schema with
  asNoContent.
- `HttpApiSchema.EmptyErrorClass` -> `effect/Schema#Error`: The class and
  no-content codec are separate in v4; combine Schema.Error with
  HttpApiSchema.asNoContent.
- `HttpApiSchema.EmptyErrorUnify` -> `none`: Removed with EmptyError;
  Schema.Error instances already support yieldable-error behavior.
- `HttpApiSchema.EmptyErrorUnifyIgnore` -> `none`: Removed with EmptyError; do
  not recreate the old Unify marker.
- `HttpApiSchema.Encoding` -> `effect/http-api/HttpApiSchema#Encoding`: The
  name remains but is now a discriminated PayloadEncoding or ResponseEncoding
  union; prefer public as\* combinators.
- `HttpApiSchema.Multipart` -> `effect/http-api/HttpApiSchema#asMultipart`: The
  type and constructor became a curried schema combinator:
  schema.pipe(asMultipart(options)).
- `HttpApiSchema.MultipartStream` ->
  `effect/http-api/HttpApiSchema#asMultipartStream`: The type and constructor
  became a curried schema combinator.
- `HttpApiSchema.Text` -> `effect/http-api/HttpApiSchema#asText`: Apply the
  encoding combinator to Schema.String instead of using a dedicated constructor.
- `HttpApiSchema.Uint8Array` -> `effect/http-api/HttpApiSchema#asUint8Array`:
  Apply the encoding combinator to Schema.Uint8Array instead of using a
  dedicated constructor.
- `HttpApiSchema.UnionUnify` -> `effect/Schema#Union`: Use Schema.Union([self,
  that]); for endpoint alternatives, pass the schema array directly to preserve
  metadata.
- `HttpApiSchema.annotations` -> `effect/Schema#annotate`: Schema annotations
  became annotate; set httpApiStatus directly or prefer HttpApiSchema.status
  for status only.
- `HttpApiSchema.asEmpty` -> `effect/http-api/HttpApiSchema#asNoContent`: Use
  schema.pipe(asNoContent({ decode }), status(code)); status is now a separate
  combinator.
- `HttpApiSchema.deunionize` -> `none`: Pass schema arrays to endpoint success,
  error, and body alternatives so each member retains status and content type.
- `HttpApiSchema.extractAnnotations` -> `none`: The internal symbol-copy helper
  was removed; HTTP metadata is schema-native and resolved through AST
  traversal.
- `HttpApiSchema.getEmptyDecodeable` ->
  `effect/http-api/HttpApiSchema#isNoContent`: Use isNoContent only to test
  bodylessness; decodeability is structural and has no exact query replacement.
- `HttpApiSchema.getEncoding` ->
  `effect/http-api/HttpApiSchema#getPayloadEncoding / getResponseEncoding`:
  Encoding lookup split by direction; application code should normally use
  public as\* combinators.
- `HttpApiSchema.getMultipart` ->
  `effect/http-api/HttpApiSchema#getPayloadEncoding`: Narrow the payload
  encoding to Multipart with buffered mode; multipart limits are on the
  encoding value.
- `HttpApiSchema.getMultipartStream` ->
  `effect/http-api/HttpApiSchema#getPayloadEncoding`: Narrow the payload
  encoding to Multipart with stream mode; multipart limits are on the encoding
  value.
- `HttpApiSchema.getParam` -> `none`: Param identity moved out of schema
  metadata; read endpoint.path and endpoint.params.
- `HttpApiSchema.getStatus` -> `effect/SchemaAST#resolveAt`: Resolve the
  httpApiStatus annotation directly, or prefer getStatusSuccess and
  getStatusError for response logic.
- `HttpApiSchema.getStatusError` ->
  `effect/http-api/HttpApiSchema#getStatusError`: The helper remains but
  accepts an AST and defaults to 500.
- `HttpApiSchema.getStatusErrorAST` ->
  `effect/http-api/HttpApiSchema#getStatusError`: The AST suffix collapsed into
  the sole helper, which defaults to 500.
- `HttpApiSchema.getStatusSuccess` ->
  `effect/http-api/HttpApiSchema#getStatusSuccess`: The helper remains but
  accepts an AST; bare Schema.Void now defaults to 200, so use Empty(204) for
  204.
- `HttpApiSchema.getStatusSuccessAST` ->
  `effect/http-api/HttpApiSchema#getStatusSuccess`: The AST suffix collapsed
  into the sole helper; bare Schema.Void no longer implies 204.
- `HttpApiSchema.param` -> `effect/http-api/HttpApiEndpoint#params`: Use a
  literal /:name path and the matching field in endpoint constructor option
  params.
- `HttpApiSchema.withEncoding` ->
  `effect/http-api/HttpApiSchema#asJson / asFormUrlEncoded / asUint8Array / asText`:
  Replace the generic kind with the matching public curried encoding
  combinator.
