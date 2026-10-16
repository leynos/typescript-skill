<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-bun/BunHttpPlatform` v3 → v4

- `BunHttpPlatform.make` -> `BunHttpPlatform.layer`: The Bun-specific
  constructor is private; provide the public layer and consume
  HttpPlatform.HttpPlatform.
