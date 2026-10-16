<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpLayerRouter` v3 → v4

- `HttpLayerRouter.FindMyWay.PathInput` -> `FindMyWay.PathInput`: Import
  FindMyWay from effect/http.
- `HttpLayerRouter.FindMyWay.make` -> `FindMyWay.make`: Import FindMyWay from
  effect/http.
- `HttpLayerRouter.MiddlewareTypeId` -> `none`: The middleware type id is
  internal in v4; use HttpRouter.Middleware.
- `HttpLayerRouter.PathInput` -> `HttpRouter.PathInput`: Moved to the
  consolidated v4 router.
- `HttpLayerRouter.Request.From` -> `HttpRouter.Request.From`: Moved with the
  layer-oriented router into the consolidated HttpRouter module.
- `HttpLayerRouter.Request.Only` -> `HttpRouter.Request.Only`: Moved with the
  layer-oriented router into the consolidated HttpRouter module.
- `HttpLayerRouter.Route.Context` -> `HttpRouter.Route.Context`: Moved with the
  Route helper types into the consolidated HttpRouter module.
- `HttpLayerRouter.Route.Error` -> `HttpRouter.Route.Error`: Moved with the
  Route helper types into the consolidated HttpRouter module.
- `HttpLayerRouter.RouteContext` -> `HttpRouter.RouteContext`: Moved to the
  consolidated v4 router.
- `HttpLayerRouter.RouteTypeId` -> `none`: Route nominal ids are internal in
  v4; construct routes with HttpRouter.route.
- `HttpLayerRouter.RouterConfig` -> `HttpRouter.RouterConfig`: Now a
  Context.Reference containing Partial\<FindMyWay.RouterConfig\>.
- `HttpLayerRouter.TypeId` -> `none`: The router nominal service id is internal
  in v4; use HttpRouter.HttpRouter.
- `HttpLayerRouter.add` -> `HttpRouter.add`: Moved to the consolidated
  HttpRouter; it still returns a route-registration Layer.
- `HttpLayerRouter.addAll` -> `HttpRouter.addAll`: Moved to the consolidated
  HttpRouter; it still registers route values through a Layer and supports a
  prefix option.
- `HttpLayerRouter.addHttpApi` -> `HttpApiBuilder.layer`: HTTP API registration
  moved to effect/http-api.
- `HttpLayerRouter.cors` -> `HttpRouter.cors`: HttpLayerRouter was consolidated
  into v4 HttpRouter.
- `HttpLayerRouter.layer` -> `HttpRouter.layer`: Use the layer for the
  consolidated HttpRouter service.
- `HttpLayerRouter.make` -> `HttpRouter.make`: The layer-oriented router became
  the sole v4 HttpRouter implementation.
- `HttpLayerRouter.schemaJson` -> `HttpRouter.schemaJson`: Moved to the
  consolidated router with v4 Schema and error types.
- `HttpLayerRouter.schemaNoBody` -> `HttpRouter.schemaNoBody`: Moved to the
  consolidated router with v4 Schema types.
- `HttpLayerRouter.serve` -> `HttpRouter.serve`: Moved to the consolidated
  router; pass the route-registration layer.
- `HttpLayerRouter.toHttpEffect` -> `HttpRouter.toHttpEffect`: Moved to the
  consolidated HttpRouter; route-not-found failures now use
  HttpServerError.HttpServerError.
- `HttpLayerRouter.toWebHandler` -> `HttpRouter.toWebHandler`: Moved to the
  consolidated router for building a Fetch handler and disposer.
