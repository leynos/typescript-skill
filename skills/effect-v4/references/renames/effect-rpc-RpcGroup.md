<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcGroup` v3 → v4

- `RpcGroup.Any` -> `effect/rpc/RpcGroup#Any`: Moved unchanged as the erased
  RpcGroup constraint.
- `RpcGroup.HandlerContext` -> `effect/rpc/RpcGroup#HandlerServices`: Renamed
  for v4 service terminology and now includes explicit RPC requirements after
  removing middleware-provided services.
- `RpcGroup.HandlersContext` -> `effect/rpc/RpcGroup#HandlersServices`:
  Renamed; it unions HandlerServices across the handler object.
- `RpcGroup.TypeId` -> `none`: The group marker is private in v4; use
  RpcGroup.Any for an erased group constraint.
