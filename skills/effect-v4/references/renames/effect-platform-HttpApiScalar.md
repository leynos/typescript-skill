<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiScalar` v3 → v4

- `HttpApiScalar.layer` -> `effect/http-api/HttpApiScalar#layer`: Pass the
  HttpApi as the first argument; the layer now contributes directly to
  HttpRouter.
- `HttpApiScalar.layerHttpLayerRouter` ->
  `effect/http-api/HttpApiScalar#layer`: The duplicate was removed. Pass
  options.api as the first layer argument and the remaining Scalar options
  second.
- `HttpApiScalar.layerHttpLayerRouterCdn` ->
  `effect/http-api/HttpApiScalar#layerCdn`: Use the explicit-api CDN layer with
  path, version, and Scalar options.
