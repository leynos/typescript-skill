<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/HttpApiError` v3 → v4

- `HttpApiError.Forbidden` ->
  `effect/http-api/HttpApiError#ForbiddenNoContent`: Use ForbiddenNoContent to
  preserve the empty 403 wire schema; Forbidden now has a JSON-tagged body.
- `HttpApiError.HttpApiDecodeError` ->
  `effect/http-api/HttpApiError#HttpApiSchemaError`: Validation now stores kind
  and a SchemaError cause and is a defect unless transformed by schema-error
  middleware.
- `HttpApiError.Issue` -> `effect/SchemaIssue#Issue`: Structured failures now
  live at HttpApiSchemaError.cause.issue; format them explicitly when a flat
  external list is needed.
- `HttpApiError.TypeId` ->
  `effect/http-api/HttpApiError#HttpApiSchemaErrorTypeId`: The old module
  symbol is gone; prefer HttpApiSchemaError.is for runtime narrowing.
