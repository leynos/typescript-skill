<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpServerError` v3 → v4

- `HttpServerError.HttpServerError` ->
  `HttpServerError.HttpServerError | HttpServerError.ServeError`: Handler
  failures became a tagged wrapper, while ServeError remains separate.
- `HttpServerError.RequestError` ->
  `HttpServerError.RequestParseError (constructor) / HttpServerError.RequestError (type)`:
  The constructible class became RequestParseError; RequestError is now a
  broader type union.
- `HttpServerError.TypeId` -> `HttpServerError.isHttpServerError`: The brand is
  private in v4; use the public runtime refinement.
- `HttpServerError.clientAbortFiberId` ->
  `HttpServerError.ClientAbort.annotation`: Client aborts now use a Cause
  context annotation rather than a sentinel FiberId.
- `HttpServerError.isServerError` -> `HttpServerError.isHttpServerError`:
  Renamed and narrowed to wrapped handler errors; test ServeError separately if
  needed.
