<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiBuilder` v3 → v4

- `HttpApiBuilder.Handlers` -> `effect/http-api/HttpApiBuilder#Handlers`:
  Handlers now tracks an endpoint map and handled identifiers. Prefer
  Handlers.FromGroup\<Group\>.
- `HttpApiBuilder.Handlers.Error` ->
  `effect/http-api/HttpApiBuilder#Handlers.Error`: The helper remains and
  extracts the error channel of an effectful group-builder return.
- `HttpApiBuilder.Handlers.Middleware` -> `none`: The handler-internal HttpApp
  middleware alias was removed. Use HttpRouter.middleware inference or
  HttpRouter.middleware.Fn.
- `HttpApiBuilder.Handlers.ValidateReturn` ->
  `effect/http-api/HttpApiBuilder#Handlers.ValidateReturn`: The validator
  remains and now checks the endpoint map against handled identifiers.
- `HttpApiBuilder.HandlersTypeId` -> `none`: The exported symbol was removed;
  do not inspect or construct the private Handlers marker.
- `HttpApiBuilder.Middleware` -> `none`: The API-specific middleware service
  tag was removed. Declared HttpApiMiddleware services are applied while routes
  are built; use HttpRouter.middleware for additional global middleware.
- `HttpApiBuilder.MiddlewareFn` -> `effect/http/HttpRouter#middleware.Fn`: HTTP
  apps are Effects in v4; use the router middleware function type or infer it
  through HttpRouter.middleware.
- `HttpApiBuilder.Router` -> `effect/http/HttpRouter#HttpRouter`: The
  API-specific router tag was removed; API and group layers register with the
  shared HttpRouter service.
- `HttpApiBuilder.api` -> `effect/http-api/HttpApiBuilder#layer`: Use
  layer(api) and provide the group layers; it registers the completed API with
  HttpRouter.
- `HttpApiBuilder.buildMiddleware` -> `none`: API-wide middleware assembly was
  removed. Declared HttpApiMiddleware services are applied while routes are
  built; use HttpRouter.middleware for additional middleware.
- `HttpApiBuilder.group` -> `effect/http-api/HttpApiBuilder#group`: The group
  layer remains; names are now identifiers and API/group global error channels
  are gone.
- `HttpApiBuilder.handler` -> `effect/http-api/HttpApiBuilder#handler`: The
  typed callback helper remains; names are now identifiers and API/group global
  error channels are gone. Pass the returned callback to handlers.handle.
- `HttpApiBuilder.httpApp` -> `effect/http/HttpRouter#toHttpEffect`: Build the
  application from the assembled API route layer; HTTP apps are Effects in v4.
- `HttpApiBuilder.middleware` -> `effect/http/HttpRouter#middleware`: Use
  router effect middleware and provide its layer to the API route layer; global
  middleware can target all router routes.
- `HttpApiBuilder.middlewareCors` -> `effect/http/HttpRouter#cors`: Use the
  router CORS layer, or provide route-scoped HttpMiddleware.cors through
  HttpRouter.middleware.
- `HttpApiBuilder.middlewareOpenApi` -> `effect/http-api/HttpApiBuilder#layer`:
  Set openapiPath in layer(api, options). The additionalPropertiesStrategy
  option was removed.
- `HttpApiBuilder.toWebHandler` -> `effect/http/HttpRouter#toWebHandler`: Pass
  the assembled API route layer to HttpRouter.toWebHandler; the handler and
  dispose lifecycle is retained.
