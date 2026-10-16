<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiClient` v3 → v4

- `HttpApiClient.Client.Method` ->
  `effect/http-api/HttpApiClient#Client.Method`: The type remains without
  GroupError. Requests use params/query and responseMode instead of
  path/urlParams and withResponse. Omitting responseMode returns the decoded
  value; a union-valued mode returns the corresponding union of decoded values,
  responses, or [value, response] tuples.
- `HttpApiClient.endpoint` -> `effect/http-api/HttpApiClient#endpoint`: The
  endpoint client remains, selected by group and endpoint identifiers and using
  v4 request and responseMode fields.
- `HttpApiClient.make` -> `effect/http-api/HttpApiClient#make`: The generated
  client remains; errors and services are now derived per endpoint and
  middleware.
- `HttpApiClient.makeWith` -> `effect/http-api/HttpApiClient#makeWith`: The
  supplied-HttpClient constructor remains and now requires endpoint
  client-middleware services.
