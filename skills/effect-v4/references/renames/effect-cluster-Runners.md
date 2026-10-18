<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Runners` v3 → v4

- `Runners.make` -> `effect/cluster/Runners#make`: Moved into core Effect. Its
  options now require codecFor; pass the codec used by the remote runner
  transport, such as RpcSerialization.json.codecFor for JSON. Context service
  projections now use Service instead of Type.
- `Runners.makeNoop` -> `effect/cluster/Runners#makeNoop`: Moved into core
  Effect; it returns the Context.Service implementation through the Service
  projection instead of Type.
