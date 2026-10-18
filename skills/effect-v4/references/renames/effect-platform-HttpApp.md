<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApp` v3 → v4

- `HttpApp.Default` ->
  `Effect.Effect<HttpServerResponse.HttpServerResponse, E, R | HttpServerRequest.HttpServerRequest>`:
  The alias was removed; v4 HTTP applications are ordinary response-producing
  Effects.
- `HttpApp.HttpApp` ->
  `Effect.Effect<A, E, R | HttpServerRequest.HttpServerRequest>`: The alias was
  removed; use the underlying Effect type and HttpEffect boundary combinators.
- `HttpApp.currentPreResponseHandlers` ->
  `HttpEffect.appendPreResponseHandler / HttpEffect.withPreResponseHandler`:
  The FiberRef was removed; register request-local handlers through HttpEffect.
- `HttpApp.ejectDefaultScopeClose` -> `HttpEffect.scopeDisableClose`: Renamed;
  it disables automatic request-scope closure, leaving closure to the caller.
- `HttpApp.toWebHandler` -> `HttpEffect.toWebHandler`: Moved to HttpEffect for
  converting an HTTP effect to a Web handler.
- `HttpApp.toWebHandlerRuntime` -> `HttpEffect.toWebHandlerWith(context)`:
  Runtime was removed in v4; supply a Context with toWebHandlerWith instead.
- `HttpApp.unsafeEjectStreamScope` -> `HttpEffect.scopeTransferToStream`:
  Renamed; it transfers request-scope closure to a streaming response.
