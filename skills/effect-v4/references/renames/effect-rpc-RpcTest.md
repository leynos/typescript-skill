<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcTest` v3 → v4

- `RpcTest.makeClient` -> `effect/rpc/RpcTest#makeClient`: Retained; it uses
  the v4 no-serialization client/server path and requires handlers plus any
  server and client middleware services.
