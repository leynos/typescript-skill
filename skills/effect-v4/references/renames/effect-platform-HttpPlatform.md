<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpPlatform` v3 → v4

- `HttpPlatform.HttpPlatform` -> `HttpPlatform.HttpPlatform`: The service is
  now a Context.Service class; use its Service member for the implementation
  type. Path-backed offset and bytesToRead accept ByteSize.Input, while
  chunkSize and all Web File range options use number.
- `HttpPlatform.TypeId` -> `none`: The public type id was removed; use the
  HttpPlatform Context.Service class.
- `HttpPlatform.layer` -> `HttpPlatform.layer`: Retained as the default
  file-response layer.
- `HttpPlatform.make` -> `HttpPlatform.make`: Retained; v4 returns the service
  implementation. The fileResponse callback receives contentLength as bigint,
  while start and end remain numbers. Web File range options use number.
