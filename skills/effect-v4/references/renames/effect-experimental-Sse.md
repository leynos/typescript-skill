<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/Sse` v3 → v4

- `Sse.RetryTypeId` -> `none`: The Retry identifier is private in v4; use
  effect/encoding/Sse#Retry and Retry.is instead of inspecting the brand.
