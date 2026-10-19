<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpIncomingMessage` v3 → v4

- `HttpIncomingMessage.MaxBodySize` -> `HttpIncomingMessage.MaxBodySize`:
  Changed from a Reference subclass holding Option\<Size\> to
  Context.Reference\<ByteSize.ByteSize | undefined\>.
- `HttpIncomingMessage.TypeId` -> `typeof HttpIncomingMessage.TypeId`: TypeId
  remains public but is now a string constant; use typeof in type position.
- `HttpIncomingMessage.withMaxBodySize` ->
  `Effect.provideService(HttpIncomingMessage.MaxBodySize, size)`: The helper
  was removed; provide a ByteSize value or undefined directly.
