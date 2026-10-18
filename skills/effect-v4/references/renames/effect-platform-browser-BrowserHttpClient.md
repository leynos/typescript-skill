<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-browser/BrowserHttpClient` v3 → v4

- `BrowserHttpClient.currentXHRResponseType` ->
  `BrowserHttpClient.CurrentXHRResponseType`: The FiberRef became a defaulted
  Context.Reference; use withXHRArrayBuffer or provide the reference as a
  service.
