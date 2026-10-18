<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/rpc/RpcSchema` v3 → v4

- `RpcSchema.Stream` -> `effect/rpc/RpcSchema#Stream`: Retained as both the
  stream schema interface and constructor; error is the second argument and
  schema services are split by direction.
- `RpcSchema.StreamSchemaId` -> `none`: The stream marker is private in v4; use
  RpcSchema.isStreamSchema and getStreamSchemas.
- `RpcSchema.getStreamSchemas` -> `effect/rpc/RpcSchema#getStreamSchemas`:
  Retained for internal-style schema inspection; pass the schema itself rather
  than its AST.
- `RpcSchema.isStreamSchema` -> `effect/rpc/RpcSchema#isStreamSchema`:
  Retained; it accepts a v4 Schema.Constraint.
- `RpcSchema.isStreamSerializable` -> `RpcSchema.isStreamSchema(schema)`: The
  separate WithResult serializability predicate was removed; v4 RPC streaming
  is identified by its explicit Stream schema.
