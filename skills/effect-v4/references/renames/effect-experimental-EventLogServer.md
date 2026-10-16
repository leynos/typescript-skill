<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/EventLogServer` v3 → v4

- `EventLogServer.Storage` ->
  `effect/eventlog/EventLogServerEncrypted#Storage`: Use the encrypted server
  Storage service, which is storeId- and session-aware.
- `EventLogServer.layerStorageMemory` ->
  `effect/eventlog/EventLogServerEncrypted#layerStorageMemory`: Use the
  encrypted server memory storage layer; storage is now storeId- and
  session-aware.
- `EventLogServer.makeHandler` ->
  `effect/eventlog/EventLogServerEncrypted#layer + effect/rpc/RpcServer#layerProtocolSocketServer`:
  Compose the encrypted server layer with the generic RPC socket server; there
  is no per-socket handler factory.
- `EventLogServer.makeHandlerHttp` ->
  `effect/eventlog/EventLogServerEncrypted#layer + effect/rpc/RpcServer#makeProtocolWithHttpEffectWebsocket`:
  Use the returned httpEffect for upgrades and provide its protocol to the
  encrypted server layer.
- `EventLogServer.makeStorageMemory` ->
  `effect/eventlog/EventLogServerEncrypted#makeStorageMemory`: Use the
  encrypted server memory storage constructor.
