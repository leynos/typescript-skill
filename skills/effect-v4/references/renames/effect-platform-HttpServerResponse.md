<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpServerResponse` v3 → v4

- `HttpServerResponse.TypeId` -> `HttpServerResponse.isHttpServerResponse`: The
  response brand is private in v4; use the public runtime refinement.
- `HttpServerResponse.expireCookie` -> `HttpServerResponse.expireCookie`: Now
  effectful and safe; use expireCookieUnsafe for synchronous throwing behavior.
- `HttpServerResponse.file` -> `HttpServerResponse.file`: Retained; offset and
  bytesToRead accept ByteSize.Input, while chunkSize uses number. Path-backed
  responses validate ranges and clamp content length to the available bytes.
- `HttpServerResponse.fileWeb` -> `HttpServerResponse.fileWeb`: Web File
  offset, bytesToRead, and chunkSize options use number, unlike path-backed
  ByteSize.Input ranges.
- `HttpServerResponse.isServerResponse` ->
  `HttpServerResponse.isHttpServerResponse`: Renamed.
- `HttpServerResponse.setCookie` -> `HttpServerResponse.setCookie`: Retained as
  the safe effectful cookie setter.
- `HttpServerResponse.stream` -> `HttpServerResponse.stream`: Retained; v4
  Stream no longer has a service type parameter.
- `HttpServerResponse.text` -> `HttpServerResponse.text`: Moved unchanged.
- `HttpServerResponse.toWeb` -> `HttpServerResponse.toWeb`: Retained, but the
  optional Runtime became an optional Context for stream execution. For a raw
  Web Response, outer headers override native headers and cookies append,
  including when the body is omitted. With withoutBody, the raw status and
  statusText are preserved unless the outer status is 204, 205, or 304, which
  takes precedence.
- `HttpServerResponse.uint8Array` -> `HttpServerResponse.uint8Array`: Moved
  unchanged.
- `HttpServerResponse.unsafeJson` -> `HttpServerResponse.jsonUnsafe`: Renamed
  to put Unsafe last; serialization failures still throw.
- `HttpServerResponse.unsafeSetCookie` -> `HttpServerResponse.setCookieUnsafe`:
  Renamed to put Unsafe last; invalid cookies still throw.
- `HttpServerResponse.unsafeSetCookies` ->
  `HttpServerResponse.setCookiesUnsafe`: Renamed to put Unsafe last; invalid
  cookies still throw.
