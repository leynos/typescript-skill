<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpClientRequest` v3 → v4

- `HttpClientRequest.Options.NoBody` -> `HttpClientRequest.Options.NoUrl`:
  NoBody was removed; v4 method helpers uniformly omit only url.
- `HttpClientRequest.TypeId` -> `HttpClientRequest.isHttpClientRequest`: The
  request brand is private in v4; use the public runtime refinement.
- `HttpClientRequest.bodyFileWeb` ->
  `HttpClientRequest.setBody + HttpBody.stream + Stream.fromReadableStream`: No
  one-call replacement remains; stream file.stream() and pass file.type and
  file.size to HttpBody.stream.
- `HttpClientRequest.bodyUnsafeJson` -> `HttpClientRequest.bodyJsonUnsafe`:
  Renamed to put Unsafe last; serialization remains synchronous and throwing.
- `HttpClientRequest.get` -> `HttpClientRequest.get`: Retained; options now use
  Options.NoUrl and no longer exclude body.
- `HttpClientRequest.head` -> `HttpClientRequest.head`: Retained; options now
  use Options.NoUrl and no longer exclude body.
- `HttpClientRequest.make` -> `HttpClientRequest.make`: Retained; all methods
  now accept Options.NoUrl without the GET/HEAD body restriction.
- `HttpClientRequest.setBody` -> `HttpClientRequest.setBody`: Retained and
  still synchronizes body content metadata into headers.
- `HttpClientRequest.toUrl` -> `HttpClientRequest.toUrl`: Retained and still
  returns Option\<URL\>.
