<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/SocketServer` v3 → v4

- `SocketServer.Address` -> `effect/net/NetAddress#SocketAddress`: Replaced by
  the shared concrete internet-or-Unix socket address union.
- `SocketServer.ErrorTypeId` -> `SocketServer.ErrorTypeId`: The API moved to
  effect/socket/SocketServer and retains this name.
- `SocketServer.TcpAddress` -> `effect/net/NetAddress#InetAddress`: Replaced by
  the shared resolved internet-address model; use address and port instead of
  hostname and port.
- `SocketServer.UnixAddress` -> `effect/net/NetAddress#UnixPathAddress`:
  Replaced by the shared Unix filesystem-path address model.
