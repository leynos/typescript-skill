<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcServer` v3 → v4

- `RpcServer.Protocol` -> `effect/rpc/RpcServer#Protocol`: Retained as a
  Context.Service; custom transports now expose a disconnect queue, explicit
  capability flags, and codecFor for schema-aware payload and exit encoding.
- `RpcServer.fiberIdClientInterrupt` -> `effect/rpc/RpcSchema#ClientAbort`: The
  sentinel FiberId was replaced by a Cause annotation; inspect ClientAbort in
  the interruption cause when client cancellation must be distinguished.
- `RpcServer.fiberIdTransientInterrupt` -> `none`: The internal transient
  sentinel was removed; protocol shutdown and disconnect now interrupt with the
  active parent fiber identity.
- `RpcServer.layer` -> `effect/rpc/RpcServer#layer`: Moved to core Effect;
  server requirements are now derived with Rpc.ServicesServer rather than the
  former combined Rpc.Context alias.
- `RpcServer.layerHttpRouter` -> `effect/rpc/RpcServer#layerHttp`: Renamed; it
  installs an HTTP or WebSocket RPC route into the v4 HttpRouter service.
- `RpcServer.layerProtocolHttp` -> `effect/rpc/RpcServer#layerProtocolHttp`:
  Retained; v4 has one HttpRouter service and no router tag option.
- `RpcServer.layerProtocolHttpRouter` ->
  `effect/rpc/RpcServer#layerProtocolHttp`: The separate layer-router variant
  was unified with layerProtocolHttp.
- `RpcServer.layerProtocolWebsocketRouter` ->
  `effect/rpc/RpcServer#layerProtocolWebsocket`: Renamed after the HTTP router
  services were unified.
- `RpcServer.make` -> `effect/rpc/RpcServer#make`: Retained; schema encoding
  services are now explicit server requirements.
- `RpcServer.makeProtocolHttp` -> `effect/rpc/RpcServer#makeProtocolHttp`:
  Retained; it registers a POST route in the current v4 HttpRouter.
- `RpcServer.makeProtocolHttpRouter` ->
  `effect/rpc/RpcServer#makeProtocolHttp`: The separate router constructor was
  unified with makeProtocolHttp.
- `RpcServer.makeProtocolWebsocketRouter` ->
  `effect/rpc/RpcServer#makeProtocolWebsocket`: Renamed after the HTTP router
  services were unified.
- `RpcServer.makeProtocolWithHttpApp` ->
  `effect/rpc/RpcServer#makeProtocolWithHttpEffect`: HttpApp became HttpEffect;
  the result contains protocol and httpEffect.
- `RpcServer.makeProtocolWithHttpAppWebsocket` ->
  `effect/rpc/RpcServer#makeProtocolWithHttpEffectWebsocket`: HttpApp became
  HttpEffect; the result contains the WebSocket protocol and upgrade effect.
- `RpcServer.toHttpApp` -> `effect/rpc/RpcServer#toHttpEffect`: Renamed for the
  v4 HTTP effect model; it starts the RPC server and returns the request effect.
- `RpcServer.toHttpAppWebsocket` ->
  `effect/rpc/RpcServer#toHttpEffectWebsocket`: Renamed for the v4 HTTP effect
  model; it returns the WebSocket upgrade effect.
- `RpcServer.toWebHandler` ->
  `HttpRouter.toWebHandler(RpcServer.layerHttp(options).pipe(Layer.provide(options.layer)))`:
  The RPC convenience wrapper was removed; build the RPC route layer and
  convert it with the generic v4 HttpRouter web-handler adapter.
