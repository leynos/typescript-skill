<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpServer` v3 → v4

- `HttpServer.Address` -> `effect/net/NetAddress#SocketAddress`: Replaced by
  the shared concrete internet-or-Unix socket address union.
- `HttpServer.HttpServer` -> `HttpServer.HttpServer`: The interface and tag
  became one Context.Service class; use its Service member for implementations.
  The service-level serve method derives requirements from the
  middleware-transformed application, so services added by middleware must also
  be provided.
- `HttpServer.ServeOptions` -> `none`: The unused respond option model was
  removed with no shared v4 counterpart.
- `HttpServer.TcpAddress` -> `effect/net/NetAddress#InetAddress`: Replaced by
  the shared resolved internet-address model; use address and port instead of
  hostname and port.
- `HttpServer.TypeId` -> `none`: The public TypeId was removed; HttpServer is
  now a Context.Service class.
- `HttpServer.UnixAddress` -> `effect/net/NetAddress#UnixPathAddress`: Replaced
  by the shared Unix filesystem-path address model.
- `HttpServer.addressWith` ->
  `HttpServer.HttpServer.use(({ address }) => effect(address))`: The accessor
  was removed; read the service and pass its Address to the callback.
- `HttpServer.formatAddress` -> `HttpServer.formatAddress`: Accepts
  NetAddress.SocketAddress and delegates to NetAddress.formatUrlUnsafe. Scoped
  IPv6 addresses throw NetAddressError; Unix paths use the unix:// prefix.
- `HttpServer.layerContext` -> `HttpServer.layerServices`: Renamed; it provides
  the standard HTTP platform services.
- `HttpServer.make` -> `HttpServer.make`: Retained; it returns the
  Context.Service implementation. Supply a NetAddress.SocketAddress for
  address, using NetAddress.inetAddressUnsafe for a parsed IP and port or
  NetAddress.unixPathAddress for a Unix path. Use NetAddress.inetAddress to
  validate the port through Result instead.
- `HttpServer.serve` -> `effect/http/HttpServer#serve`: Moved to the v4 HTTP
  module; the application is now an Effect producing HttpServerResponse rather
  than the separate HttpApp model.
