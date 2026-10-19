<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node-shared/NodeSocket` v3 → v4

- `NodeSocket.NetSocket` -> `NodeSocket.NetSocket`: The identifier remains, but
  the old interface/tag pair is now one Context.Service; use
  NodeSocket.NetSocket["Service"] for the node:net.Socket value type.
