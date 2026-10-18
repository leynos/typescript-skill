<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpBody` v3 → v4

- `HttpBody.Empty` -> `HttpBody.Empty`: Retained with the same tag, but v4
  exports a class rather than an interface.
- `HttpBody.ErrorReason` -> `HttpBody.ErrorReason`: Retained but reshaped;
  original causes now live on HttpBodyError.cause.
- `HttpBody.ErrorTypeId` -> `HttpBody.HttpBodyError`: The error type-id is
  private in v4; identify the exported error class instead.
- `HttpBody.HttpBodyError` -> `HttpBody.HttpBodyError`: Changed from a
  factory/interface to a class constructed with reason and optional cause.
- `HttpBody.Raw` -> `HttpBody.Raw`: Retained with the same tag and payload, but
  v4 exports a class.
- `HttpBody.Stream` -> `HttpBody.Stream`: Retained with the same tag and byte
  stream, but v4 exports a class.
- `HttpBody.TypeId` -> `HttpBody.isHttpBody`: The body brand is private in v4;
  use the public refinement instead.
- `HttpBody.Uint8Array` -> `HttpBody.Uint8Array`: Retained with the same fields
  and tag, but v4 exports a class.
- `HttpBody.file` -> `HttpBody.file`: Retained; bufferSize was replaced by
  numeric chunkSize. Offset and bytesToRead accept ByteSize.Input. Invalid
  ranges and a final EOF-clamped content length above Number.MAX\_SAFE\_INTEGER
  fail with PlatformError / BadArgument.
- `HttpBody.fileInfo` -> `HttpBody.fileFromInfo`: Renamed; it uses supplied
  File.Info with ByteSize size metadata and requires FileSystem. Offset and
  bytesToRead accept ByteSize.Input, while chunkSize is numeric. Invalid ranges
  and a final EOF-clamped content length above Number.MAX\_SAFE\_INTEGER fail
  with PlatformError / BadArgument.
- `HttpBody.unsafeJson` -> `HttpBody.jsonUnsafe`: Renamed to put Unsafe last;
  serialization failures still throw.
- `HttpBody.urlParams` -> `HttpBody.urlParams`: Retained and widened to accept
  UrlParams.Input.
