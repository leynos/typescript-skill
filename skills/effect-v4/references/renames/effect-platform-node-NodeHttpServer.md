<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeHttpServer` v3 → v4

- `NodeHttpServer.layerContext` -> `NodeHttpServer.layerHttpServices`: Direct
  rename; it provides NodeServices, HttpPlatform, and Etag.Generator, without
  the removed WorkerManager.
