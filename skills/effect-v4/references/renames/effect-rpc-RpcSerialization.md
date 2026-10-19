<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcSerialization` v3 → v4

- `RpcSerialization.RpcSerializationError` ->
  `effect/rpc/RpcSerialization#MaxBufferSizeExceeded`: Buffer-limit failures
  now use MaxBufferSizeExceeded. MessagePack-specific decode errors have no
  counterpart.
- `RpcSerialization.layerMsgPack` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: MessagePack RPC
  serialization was removed. Use SchemaBinary, or layerNdjson when you need
  newline-delimited JSON framing.
- `RpcSerialization.layerMsgPackWith` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: MessagePack RPC
  serialization was removed. Pass maxFrameSize to layerSchemaBinary; NDJSON
  buffer limits remain on layerNdjsonWith.
- `RpcSerialization.makeMsgPack` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: MessagePack RPC
  serialization was removed. Construct SchemaBinary serialization with
  layerSchemaBinary.
- `RpcSerialization.msgPack` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: The MessagePack
  RpcSerialization service value was removed. Provide layerSchemaBinary instead.
