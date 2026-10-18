<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/EntityProxyServer` v3 → v4

- `EntityProxyServer.RpcHandlers` ->
  `effect/cluster/EntityProxyServer#RpcHandlers`: Moved into core Effect and
  updated for the additional v4 Rpc requirements type parameter.
- `EntityProxyServer.layerHttpApi` ->
  `effect/cluster/EntityProxyServer#layerHttpApi`: Moved into core Effect. Use
  v4 HttpApi identifiers and provide Sharding plus both Rpc.ServicesServer and
  Rpc.ServicesClient codec requirements.
- `EntityProxyServer.layerRpcHandlers` ->
  `effect/cluster/EntityProxyServer#layerRpcHandlers`: Moved into core Effect;
  replace Rpc.Context with both Rpc.ServicesServer and Rpc.ServicesClient codec
  requirements, alongside Sharding.
