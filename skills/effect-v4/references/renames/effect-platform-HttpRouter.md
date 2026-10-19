<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpRouter` v3 → v4

- `HttpRouter.Default` -> `HttpRouter.HttpRouter + HttpRouter.layer`:
  Custom/default router tags were removed; v4 provides one router service.
- `HttpRouter.HttpRouter` -> `HttpRouter.HttpRouter`: The name remains, but now
  denotes the mutable layer-oriented registration service.
- `HttpRouter.HttpRouter.DefaultServices` -> `none`: The custom tagged-router
  default-service bundle was removed.
- `HttpRouter.HttpRouter.Service` -> `HttpRouter.HttpRouter`: Use the
  consolidated router service interface.
- `HttpRouter.Route.Middleware` -> `Effect.Effect`: Spell the route response
  Effect directly, or use HttpRouter.middleware for transforms.
- `HttpRouter.RouteContextTypeId` -> `none`: The nominal id is internal in v4;
  access HttpRouter.RouteContext as a service.
- `HttpRouter.RouteTypeId` -> `none`: The nominal id is internal in v4;
  construct routes with HttpRouter.route.
- `HttpRouter.Tag` -> `none`: Custom router tags were removed; use the
  singleton router service and registration layers.
- `HttpRouter.TypeId` -> `none`: The router nominal service id is internal in
  v4; use HttpRouter.HttpRouter.
- `HttpRouter.all` -> `HttpRouter.add("*", path, handler, options)`: v4
  registers a route layer instead of returning an immutable router.
- `HttpRouter.append` -> `HttpRouter.addAll([route])`: Register the route and
  merge its layer with other route layers.
- `HttpRouter.catchAll` -> `HttpRouter.middleware + Effect.catch`: Apply
  typed-error recovery in route middleware provided to route layers.
- `HttpRouter.catchAllCause` -> `HttpRouter.middleware + Effect.catchCause`:
  Apply cause recovery in route middleware provided to route layers.
- `HttpRouter.catchTag` -> `HttpRouter.middleware + Effect.catchTag`: Apply
  tagged-error recovery in route middleware provided to route layers.
- `HttpRouter.concat` -> `Layer.merge`: Routers are now route-registration
  layers; merge the two layers.
- `HttpRouter.concatAll` -> `Layer.mergeAll`: Routers are now
  route-registration layers; merge all layers.
- `HttpRouter.currentRouterConfig` -> `HttpRouter.RouterConfig`: The FiberRef
  became a Context.Reference containing Partial\<FindMyWay.RouterConfig\>.
- `HttpRouter.empty` -> `Layer.empty`: There is no immutable empty router; use
  an empty registration layer.
- `HttpRouter.fromIterable` -> `HttpRouter.addAll(Array.from(routes))`:
  Materialize and register the route descriptors as a layer.
- `HttpRouter.get` -> `HttpRouter.add("GET", path, handler, options)`: Register
  a route layer; handlers must produce HttpServerResponse.
- `HttpRouter.head` ->
  `HttpRouter.addAll([HttpRouter.route("HEAD", path, handler, options)])`: Use
  route plus addAll because add does not expose HEAD.
- `HttpRouter.makeRoute` -> `HttpRouter.route`: Renamed to route; v4 route
  options no longer expose the old prefix field.
- `HttpRouter.mount` -> `HttpRouter.addAll(routes, { prefix: path })`: Register
  child routes with a prefix, or use router.prefixed(path).
- `HttpRouter.mountApp` ->
  `HttpRouter.use((router) => router.prefixed(path).add("*", "/*", app))`:
  Register the app on the prefixed router service; no direct mount API remains.
- `HttpRouter.options` -> `HttpRouter.add("OPTIONS", path, handler, options)`:
  Register a route layer; handlers must produce HttpServerResponse.
- `HttpRouter.patch` -> `HttpRouter.add("PATCH", path, handler, options)`:
  Register a route layer; handlers must produce HttpServerResponse.
- `HttpRouter.post` -> `HttpRouter.add("POST", path, handler, options)`:
  Register a route layer; handlers must produce HttpServerResponse.
- `HttpRouter.prefixAll` -> `HttpRouter.addAll(routes, { prefix })`: Apply the
  prefix while registering route descriptors.
- `HttpRouter.put` -> `HttpRouter.add("PUT", path, handler, options)`: Register
  a route layer; handlers must produce HttpServerResponse.
- `HttpRouter.setRouterConfig` ->
  `Layer.succeed(HttpRouter.RouterConfig)(config)`: Provide the RouterConfig
  Context.Reference as a layer.
- `HttpRouter.toHttpApp` -> `HttpRouter.toHttpEffect`: Pass the
  route-registration layer to build the server handler effect.
- `HttpRouter.transform` -> `HttpRouter.middleware`: Express the route-wide
  response Effect transform as router middleware.
- `HttpRouter.withRouterConfig` ->
  `Effect.provideService(effect, HttpRouter.RouterConfig, config)`: Provide the
  RouterConfig Context.Reference locally instead of setting a FiberRef.
