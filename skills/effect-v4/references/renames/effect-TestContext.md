<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TestContext` v3 → v4

- `TestContext.LiveContext` -> `@effect/vitest#live`: Default runtime
  references are live in v4. Use it.live for a whole live test; no LiveContext
  layer is required.
- `TestContext.TestContext` ->
  `Layer.mergeAll(TestConsole.layer, TestClock.layer())`: This is the v4 test
  layer used by @effect/vitest. Prefer it.effect, which provides it
  automatically.
