<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Url` v3 → v4

- `Url.fromString` -> `Url.fromString`: Retained; returns Result with
  IllegalArgumentError instead of Either with IllegalArgumentException.
- `Url.setUrlParams` -> `Url.setUrlParams`: Retained and widened to accept
  UrlParams.Input.
