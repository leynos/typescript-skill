<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Multipart` v3 → v4

- `Multipart.ErrorTypeId` -> `Multipart.MultipartError`: The public error
  type-id alias was removed; use the MultipartError class.
- `Multipart.FieldMimeTypes` -> `Multipart.FieldMimeTypes`: The setting remains
  but is now a Context.Reference rather than a service class.
- `Multipart.FileSchema` -> `Multipart.PersistedFileSchema`: The schema for
  persisted multipart files was renamed.
- `Multipart.MaxFieldSize` -> `Multipart.MaxFieldSize`: Now a
  Context.Reference\<ByteSize.ByteSize\>; provide a value such as
  ByteSize.bytes(100).
- `Multipart.MaxFileSize` -> `Multipart.MaxFileSize`: Now a
  Context.Reference\<ByteSize.ByteSize | undefined\>; provide
  ByteSize.bytes(100), for example, or undefined for no limit.
- `Multipart.MaxParts` -> `Multipart.MaxParts`: The setting remains as a
  Context.Reference; use undefined rather than Option.none for no limit.
- `Multipart.TypeId` -> `typeof Multipart.TypeId`: The runtime marker remains
  exported, but the separate type alias was removed.
- `Multipart.makeChannel` -> `effect/http/Multipart#makeChannel`: The channel
  constructor moved and no longer accepts bufferSize; input and output chunks
  use non-empty readonly arrays.
- `Multipart.schemaJson` -> `Multipart.schemaJson`: The JSON-field decoder
  remains in effect/http/Multipart and uses v4 Schema constraints.
- `Multipart.withFieldMimeTypes` ->
  `Effect.provideService(Multipart.FieldMimeTypes, mimeTypes)`: Provide the v4
  Context.Reference around the effect.
- `Multipart.withLimits` ->
  `Effect.provideContext(effect, Multipart.limitsServices(options))`: Build the
  multipart limit context and provide it to the effect; Option-valued limits
  became optional plain values.
- `Multipart.withLimits.Options` -> `Multipart.withLimits.Options`: Limit
  fields now use optional plain numbers or ByteSize inputs; convert Option.none
  to undefined and Option.some(value) to value.
- `Multipart.withLimitsStream` ->
  `Stream.provideContext(stream, Multipart.limitsServices(options))`: Build the
  multipart limit context and provide it to the stream; Option-valued limits
  became optional plain values.
- `Multipart.withMaxFieldSize` ->
  `Effect.provideService(Multipart.MaxFieldSize, size)`: Provide a ByteSize
  value, such as ByteSize.bytes(100). To normalize ByteSize.Input options, use
  Multipart.limitsServices.
- `Multipart.withMaxFileSize` ->
  `Effect.provideService(Multipart.MaxFileSize, size)`: Replace Option.none
  with undefined and Option.some(value) with a normalized ByteSize value. To
  normalize ByteSize.Input options, use Multipart.limitsServices.
- `Multipart.withMaxParts` ->
  `Effect.provideService(Multipart.MaxParts, count)`: Provide the v4
  Context.Reference around the effect, converting Option.none to undefined.
