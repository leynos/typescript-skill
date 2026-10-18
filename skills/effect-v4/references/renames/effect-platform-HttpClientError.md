<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpClientError` v3 → v4

- `HttpClientError.HttpClientError` -> `HttpClientError.HttpClientError`:
  Changed from a union to a tagged wrapper class containing a concrete failure
  in reason.
- `HttpClientError.RequestError` -> `HttpClientError.RequestError`: Now a
  type-only reason union; construct a concrete reason and wrap it in
  HttpClientError.
- `HttpClientError.TypeId` -> `HttpClientError.isHttpClientError`: The brand
  key is private in v4; use the public runtime refinement.
