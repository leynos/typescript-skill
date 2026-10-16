<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/FetchHttpClient` v3 → v4

- `FetchHttpClient.Fetch` -> `FetchHttpClient.Fetch`: Retained as a
  Context.Reference that defaults to globalThis.fetch.
- `FetchHttpClient.layer` -> `FetchHttpClient.layer`: Retained as the
  HttpClient layer backed by the configured Fetch reference.
