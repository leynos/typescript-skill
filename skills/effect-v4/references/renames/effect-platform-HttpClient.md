<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpClient` v3 → v4

- `HttpClient.SpanNameGenerator` -> `HttpClient.SpanNameGenerator`: The
  interface became a Context.Reference containing the generator function.
- `HttpClient.TypeId` -> `HttpClient.isHttpClient`: The brand key is private in
  v4; use the public runtime refinement.
- `HttpClient.catchAll` -> `HttpClient.catch`: Renamed to catch; the recovery
  callback still returns a response effect.
- `HttpClient.catchTag` -> `HttpClient.catchTag`: Retained and widened to
  accept one or more error tags.
- `HttpClient.currentTracerDisabledWhen` -> `HttpClient.TracerDisabledWhen`:
  Renamed and changed from FiberRef to Context.Reference.
- `HttpClient.currentTracerPropagation` ->
  `HttpClient.TracerPropagationEnabled`: Renamed and changed from FiberRef to
  Context.Reference\<boolean\>.
- `HttpClient.filterOrFail` -> `HttpClient.filterOrFail`: Retained; v4 also
  provides refinement overloads.
- `HttpClient.filterStatus` -> `HttpClient.filterStatus`: Retained; rejection
  now fails with the HttpClientError wrapper.
- `HttpClient.filterStatusOk` -> `HttpClient.filterStatusOk`: Retained; non-2xx
  responses now fail with the HttpClientError wrapper.
- `HttpClient.make` -> `HttpClient.make`: Retained; the runner receives
  Fiber.Fiber and failures use the v4 error wrapper.
- `HttpClient.makeWith` -> `HttpClient.makeWith`: Retained with the preprocess
  and postprocess constructor pattern.
- `HttpClient.retry` -> `HttpClient.retry`: Retained; the Schedule error
  channel is included in the resulting client error type.
- `HttpClient.tap` -> `effect/http/HttpClient#tap`: Moved to the v4 HTTP module
  with the same response-effect callback and client error/service widening.
- `HttpClient.transform` -> `effect/http/HttpClient#transform`: Moved to the v4
  HTTP module with the same request-aware transformation shape.
- `HttpClient.withSpanNameGenerator` ->
  `HttpClient.transformResponse(Effect.provideService(HttpClient.SpanNameGenerator, f))`:
  The convenience combinator was removed; provide the reference around
  response effects.
- `HttpClient.withTracerDisabledWhen` ->
  `HttpClient.transformResponse(Effect.provideService(HttpClient.TracerDisabledWhen, predicate))`:
  The convenience combinator was removed; provide the reference around
  response effects.
- `HttpClient.withTracerPropagation` ->
  `HttpClient.transformResponse(Effect.provideService(HttpClient.TracerPropagationEnabled, enabled))`:
  Provide the renamed propagation reference around response effects.
