<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcMessage` v3 → v4

- `RpcMessage.FromServerEncoded` -> `effect/rpc/RpcMessage#FromServerEncoded`:
  The union is retained and now also includes RequestEncoded for
  server-originated requests and notifications. Handle \_tag: "Request" when
  matching exhaustively; isNotification identifies notifications.
- `RpcMessage.RequestId` -> `effect/rpc/RpcMessage#RequestId`: Request ids are
  now branded string or number values; convert bigint ids before calling the
  retained RequestId constructor.
- `RpcMessage.RequestIdTypeId` -> `effect/rpc/RpcMessage#RequestId`: The public
  symbol marker was removed; use the branded RequestId type and RequestId
  constructor rather than inspecting its brand.
