<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/EventLogRemote` v3 → v4

- `EventLogRemote.Ack` -> `none`: A write acknowledgement is now the void
  success of EventLogMessage.WriteSingleRpc or WriteChunkedRpc.
- `EventLogRemote.Changes` -> `effect/eventlog/EventLogMessage#ChangesRpc`:
  ChangesRpc replaces the separate request and response models with one
  streaming RPC.
- `EventLogRemote.EventLogRemote` ->
  `effect/eventlog/EventLogRemote#EventLogRemote`: Use the v4 Context.Service;
  methods now take storeId-aware options.
- `EventLogRemote.Hello` -> `effect/eventlog/EventLogMessage#HelloResponse`:
  HelloResponse replaces Hello and includes the v4 authentication challenge;
  HelloRpc defines the endpoint.
- `EventLogRemote.Pong` -> `none`: The event-log Pong model was removed;
  heartbeats belong to the generic RPC socket protocol.
- `EventLogRemote.ProtocolRequest` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: EventLogRemoteRpcs and
  generic RPC serialization replace the old protocol request union.
- `EventLogRemote.ProtocolRequestMsgPack` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: Use the generic SchemaBinary
  RPC serialization layer instead of a request-specific schema.
- `EventLogRemote.ProtocolResponse` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: EventLogRemoteRpcs and
  generic RPC serialization replace the old protocol response union.
- `EventLogRemote.ProtocolResponseMsgPack` ->
  `effect/rpc/RpcSerialization#layerSchemaBinary`: Use the generic SchemaBinary
  RPC serialization layer instead of a response-specific schema.
- `EventLogRemote.RemoteAdditions` -> `none`: This unused protocol model has no
  v4 counterpart.
- `EventLogRemote.RequestChanges` ->
  `effect/eventlog/EventLogMessage#ChangesRpc`: ChangesRpc replaces the
  separate request model with one streaming RPC.
- `EventLogRemote.StopChanges` -> `none`: Interrupt the ChangesRpc stream
  instead of sending a StopChanges message.
- `EventLogRemote.decodeRequest` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: Generic RPC framing and
  RpcSerialization.layerSchemaBinary replace the module-specific request
  decoder.
- `EventLogRemote.decodeResponse` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: Generic RPC framing and
  RpcSerialization.layerSchemaBinary replace the module-specific response
  decoder.
- `EventLogRemote.encodeRequest` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: Generic RPC framing and
  RpcSerialization.layerSchemaBinary replace the module-specific request
  encoder.
- `EventLogRemote.encodeResponse` ->
  `effect/eventlog/EventLogMessage#EventLogRemoteRpcs`: Generic RPC framing and
  RpcSerialization.layerSchemaBinary replace the module-specific response
  encoder.
- `EventLogRemote.fromSocket` ->
  `effect/eventlog/EventLogRemote#makeEncrypted + effect/rpc/RpcClient#makeProtocolSocket`:
  Construct the encrypted remote separately from its generic RPC socket
  protocol.
- `EventLogRemote.layerWebSocket` ->
  `effect/eventlog/EventLogRemote#layerEncrypted + effect/rpc/RpcClient#layerProtocolSocket`:
  Compose the encrypted remote with the generic socket protocol, SchemaBinary
  serialization, and a Socket provider.
- `EventLogRemote.layerWebSocketBrowser` ->
  `effect/eventlog/EventLogRemote#layerEncrypted + effect/rpc/RpcClient#layerProtocolSocket + @effect/platform-browser/BrowserSocket#layerWebSocket`:
  Compose the encrypted remote and generic RPC socket protocol with the
  browser WebSocket layer.
