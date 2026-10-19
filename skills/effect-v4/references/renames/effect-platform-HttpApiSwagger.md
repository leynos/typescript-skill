<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiSwagger` v3 → v4

- `HttpApiSwagger.layer` -> `effect/http-api/HttpApiSwagger#layer`: Pass the
  HttpApi as the first argument; the layer now contributes directly to
  HttpRouter.
- `HttpApiSwagger.layerHttpLayerRouter` ->
  `effect/http-api/HttpApiSwagger#layer`: The duplicate was removed. Pass
  options.api first and the path option second.
