<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpMiddleware` v3 → v4

- `HttpMiddleware.SpanNameGenerator` -> `HttpMiddleware.SpanNameGenerator`: The
  branded interface became a Context.Reference containing the generator.
- `HttpMiddleware.cors` -> `HttpMiddleware.cors`: Retained with the same CORS
  options and behavior.
- `HttpMiddleware.currentTracerDisabledWhen` ->
  `HttpMiddleware.TracerDisabledWhen`: The FiberRef became a Context.Reference
  containing the request predicate.
- `HttpMiddleware.loggerDisabled` -> `HttpMiddleware.withLoggerDisabled`: The
  FiberRef was removed; locally wrap an effect or use HttpRouter.disableLogger.
- `HttpMiddleware.withSpanNameGenerator` ->
  `Layer.provide(layer, Layer.succeed(HttpMiddleware.SpanNameGenerator)(f))`:
  Provide the SpanNameGenerator reference to the target layer.
- `HttpMiddleware.withTracerDisabledForUrls` ->
  `Layer.provide(layer, HttpMiddleware.layerTracerDisabledForUrls(urls))`:
  Provide the new URL-predicate layer to the target layer.
- `HttpMiddleware.withTracerDisabledWhen` ->
  `Layer.provide(layer, Layer.succeed(HttpMiddleware.TracerDisabledWhen)(predicate))`:
  Provide the TracerDisabledWhen reference to the target layer.
- `HttpMiddleware.withTracerDisabledWhenEffect` ->
  `Effect.provideService(effect, HttpMiddleware.TracerDisabledWhen, predicate)`:
  Provide the TracerDisabledWhen reference locally to the effect.
