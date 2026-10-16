<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/AiError` v3 → v4

- `AiError.AiError` -> `AiError.AiError`: Moved to effect/ai/AiError and
  redesigned from a union of separately tagged errors into one AiError wrapper
  with a semantic reason. Construct it with AiError.make({ module, method,
  reason }) and match error.reason rather than the old top-level tags.
- `AiError.HttpRequestDetails` -> `AiError.HttpRequestDetails`: Retained in
  effect/ai/AiError and also re-exported as Response.HttpRequestDetails. Hash
  is an optional string instead of Option, headers may contain Redacted
  strings, and method includes TRACE.
- `AiError.HttpRequestError` -> `AiError.make + AiError.NetworkError`: Replace
  the old top-level request error with an AiError whose reason is NetworkError.
  NetworkError.fromRequestError converts a v4 HttpClientError.RequestError.
- `AiError.HttpResponseError` ->
  `AiError.make + AiError.reasonFromHttpStatus / AiError.InvalidOutputError`:
  There is no single v4 response-error class. Wrap a semantic reason with
  AiError.make: use reasonFromHttpStatus for status failures and
  InvalidOutputError for decode or empty-body failures.
- `AiError.MalformedInput` -> `AiError.make + AiError.InvalidUserInputError`:
  Replace the old top-level input error with an AiError whose reason is
  InvalidUserInputError. Use InvalidRequestError when the provider request
  parameters themselves are malformed.
- `AiError.MalformedOutput` -> `AiError.make + AiError.InvalidOutputError`:
  Replace the old top-level output error with an AiError whose reason is
  InvalidOutputError. The old fromParseError helper becomes
  InvalidOutputError.fromSchemaError.
- `AiError.TypeId` -> `AiError.isAiError`: The AiError brand is private in v4.
  Use isAiError for runtime narrowing, or isAiErrorReason for a reason, instead
  of inspecting or constructing the type id.
- `AiError.UnknownError` -> `AiError.make + AiError.UnknownError`: UnknownError
  is now a semantic reason rather than a top-level error. Put module and method
  on AiError.make and inspect reason.\_tag when handling the outer AiError.
