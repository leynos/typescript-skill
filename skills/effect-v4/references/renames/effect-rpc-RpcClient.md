<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcClient` v3 → v4

- `RpcClient.Protocol` -> `effect/rpc/RpcClient#Protocol`: Retained as a
  Context.Service; custom transports now route multiple client ids through run
  and send.
- `RpcClient.RpcClient.From` -> `effect/rpc/RpcClient#RpcClient.From`:
  Generated clients now preserve full RPC tags as property names, remove the
  Prefix type parameter, and expose streaming results through the asQueue
  option instead of asMailbox.
- `RpcClient.RpcClient.NonPrefixed` -> `none`: The prefix-partition helper was
  removed; v4 clients map every RPC tag directly to an object property.
- `RpcClient.RpcClient.Prefixes` -> `none`: Nested prefix client objects were
  removed; v4 preserves the full RPC tag as the generated client property.
- `RpcClient.currentHeaders` -> `effect/rpc/RpcClient#CurrentHeaders`: Renamed
  and changed from FiberRef to Context.Reference; prefer RpcClient.withHeaders
  for scoped overrides.
- `RpcClient.makeProtocolHttp` -> `effect/rpc/RpcClient#makeProtocolHttp`:
  Retained; it creates the Protocol service implementation from an HttpClient.
- `RpcClient.withHeadersEffect` ->
  `Effect.flatMap(headers, (value) => RpcClient.withHeaders(effect, value))`:
  withHeaders now accepts Headers.Input synchronously; evaluate effectful
  headers first and then scope the client effect.
