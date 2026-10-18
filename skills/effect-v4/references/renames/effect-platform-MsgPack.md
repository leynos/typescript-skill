<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/MsgPack` v3 → v4

- `MsgPack.ErrorTypeId` -> `Schema.SchemaError`: MsgPackError was removed with
  MessagePack. SchemaBinary channels fail with Schema.SchemaError.
- `MsgPack.MsgPackError` -> `Schema.SchemaError`: MsgPackError was removed with
  MessagePack. SchemaBinary channels fail with Schema.SchemaError.
- `MsgPack.duplex` -> `SchemaBinary.duplex`: MessagePack was removed. Wrap a
  byte channel with SchemaBinary.duplex and explicit input and output schemas.
- `MsgPack.duplexSchema` -> `SchemaBinary.duplex`: MessagePack was removed. Use
  SchemaBinary.duplex with the v4 Schema model.
- `MsgPack.pack` -> `SchemaBinary.encode`: MessagePack was removed. Encode
  schema values to binary frames with SchemaBinary.encode.
- `MsgPack.packSchema` -> `SchemaBinary.encode`: MessagePack was removed. Use
  SchemaBinary.encode with the v4 Schema model.
- `MsgPack.schema` -> `SchemaBinary.toCodec`: MessagePack was removed. Derive a
  binary codec from a Schema with SchemaBinary.toCodec.
- `MsgPack.unpack` -> `SchemaBinary.decode`: MessagePack was removed. Decode
  binary frames with SchemaBinary.decode.
- `MsgPack.unpackSchema` -> `SchemaBinary.decode`: MessagePack was removed. Use
  SchemaBinary.decode with the v4 Schema model.
