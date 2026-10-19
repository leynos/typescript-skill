<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Headers` v3 → v4

- `Headers.Headers` -> `Headers.Headers`: Import Headers from effect/http; the
  immutable string-record interface is retained with its v4 TypeId brand.
- `Headers.HeadersTypeId` -> `Headers.TypeId`: The public Headers type-id
  symbol was renamed from HeadersTypeId to TypeId.
- `Headers.currentRedactedNames` -> `Headers.CurrentRedactedNames`: Renamed and
  changed from FiberRef to Context.Reference; override it with service
  provisioning.
- `Headers.remove` -> `Headers.remove / Headers.removeMany`: Use remove for one
  name or removeMany for an iterable; RegExp removal requires enumerating
  matching names.
- `Headers.schema` -> `Schema.Headers`: The encoded-record and self schemas
  were consolidated and moved to effect/Schema as Schema.Headers.
- `Headers.schemaFromSelf` -> `Schema.Headers`: The encoded-record and self
  schemas were consolidated and moved to effect/Schema as Schema.Headers.
- `Headers.unsafeFromRecord` -> `Headers.fromRecordUnsafe`: Renamed to put
  Unsafe last; it still skips name normalization.
