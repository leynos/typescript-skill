<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunHttpServer` v3 → v4

- `BunHttpServer.ServeOptions` -> `BunHttpServer.ServeOptions<R>`: The alias
  remains, but R is now a route-key string union and routes uses
  Bun.Serve.Routes; update old route-map generic arguments or infer R from
  routes.
- `BunHttpServer.layerContext` -> `BunHttpServer.layerHttpServices`: Direct
  rename; it provides HttpPlatform, Etag.Generator, and BunServices.
