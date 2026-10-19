<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcMiddleware` v3 → v4

- `RpcMiddleware.RpcMiddlewareWrap` ->
  `effect/rpc/RpcMiddleware#RpcMiddleware`: The wrap and non-wrap shapes were
  unified; implement a function receiving the handler effect and request
  options.
- `RpcMiddleware.Tag` -> `effect/rpc/RpcMiddleware#Service`: Renamed and
  redesigned with explicit requires, provides, clientError, error, and
  requiredForClient configuration.
- `RpcMiddleware.TagClass` -> `effect/rpc/RpcMiddleware#ServiceClass`: Renamed
  class type for the v4 Context.Service-based middleware declaration.
- `RpcMiddleware.TagClass.Failure` -> `effect/rpc/RpcMiddleware#Error`: Failure
  terminology became error; apply the extractor to the middleware ID.
- `RpcMiddleware.TagClass.FailureContext` ->
  `effect/rpc/RpcMiddleware#ErrorServicesEncode / ErrorServicesDecode`: The
  single schema context split into server encoding and client decoding services.
- `RpcMiddleware.TagClass.FailureSchema` ->
  `effect/rpc/RpcMiddleware#ErrorSchema`: Renamed and applied to the middleware
  ID rather than constructor options.
- `RpcMiddleware.TagClass.FailureService` -> `effect/rpc/RpcMiddleware#Error`:
  Use the decoded error extractor; optional middleware fallback was removed.
- `RpcMiddleware.TagClass.Optional` -> `none`: Optional declaration and
  fallback-on-failure behavior were removed; model fallback inside the
  middleware effect.
- `RpcMiddleware.TagClass.Provides` -> `effect/rpc/RpcMiddleware#Provides`:
  Moved to the module level and applied to the middleware ID metadata.
- `RpcMiddleware.TagClass.RequiredForClient` ->
  `RpcMiddleware.ServiceClass["requiredForClient"]`: The standalone options
  extractor was removed; the boolean is exposed directly by the resulting
  service class.
- `RpcMiddleware.TagClassAny` -> `effect/rpc/RpcMiddleware#AnyService`: Renamed
  widened middleware service-key shape.
- `RpcMiddleware.TagClassAnyWithProps` ->
  `effect/rpc/RpcMiddleware#AnyServiceWithProps`: Renamed erased service key
  whose value has the unified server middleware function shape.
- `RpcMiddleware.TypeId` -> `effect/rpc/RpcMiddleware#TypeId`: Retained as the
  public middleware metadata marker and now has a string-literal type.
- `RpcMiddleware.layerClient` -> `effect/rpc/RpcMiddleware#layerClient`:
  Retained; the client function can now modify the typed Request passed to next
  and carry a client-only error type.
