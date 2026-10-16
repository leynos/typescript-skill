<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TestConfig` v3 → v4

- `TestConfig.TestConfig` -> `none`: There is no v4 TestConfig service. Move
  runner settings to Vitest and native Arbitrary check options, or define an
  application-specific Context.Reference if runtime access is needed.
- `TestConfig.make` -> `{ repeats, retries, samples, shrinks }`: The v3
  constructor only returned its parameter object. The TestConfig service was
  removed; keep a plain object only for application-owned configuration.
