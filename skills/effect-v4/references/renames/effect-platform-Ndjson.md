<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Ndjson` v3 → v4

- `Ndjson.ErrorTypeId` -> `Ndjson.NdjsonError`: The public error marker was
  removed; use the NdjsonError class.
- `Ndjson.NdjsonErrorTypeId` -> `Ndjson.NdjsonError`: The public error type-id
  alias was removed; use the NdjsonError class.
- `Ndjson.NdjsonOptions` -> `{ readonly ignoreEmptyLines?: boolean }`: The
  standalone options interface was removed; decoding and duplex APIs accept
  this inline shape.
- `Ndjson.duplex` -> `Ndjson.duplex`: The API moved to effect/encoding/Ndjson.
- `Ndjson.duplexSchema` -> `Ndjson.duplexSchema`: The API moved to
  effect/encoding/Ndjson and uses v4 Schema constraints.
- `Ndjson.pack` -> `Ndjson.encode`: The NDJSON channel constructor was renamed
  from pack to encode.
- `Ndjson.packSchema` -> `Ndjson.encodeSchema`: The schema-aware pack channel
  was renamed to encodeSchema.
- `Ndjson.packSchemaString` -> `Ndjson.encodeSchemaString`: The string schema
  pack channel was renamed to encodeSchemaString.
- `Ndjson.packString` -> `Ndjson.encodeString`: The string pack channel was
  renamed to encodeString.
- `Ndjson.unpack` -> `Ndjson.decode`: The NDJSON channel constructor was
  renamed from unpack to decode.
- `Ndjson.unpackSchema` -> `Ndjson.decodeSchema`: The schema-aware unpack
  channel was renamed to decodeSchema.
- `Ndjson.unpackSchemaString` -> `Ndjson.decodeSchemaString`: The string schema
  unpack channel was renamed to decodeSchemaString.
- `Ndjson.unpackString` -> `Ndjson.decodeString`: The string unpack channel was
  renamed to decodeString.
