<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/TestClock` v3 → v4

- `TestClock.Data` -> `TestClock.TestClock.State`: The nearest state model is
  State, with timestamp and a private latch-based sleep queue. V4 exposes no
  full state getter or setter.
- `TestClock.adjustWith` ->
  `Effect.zipWith(effect, TestClock.adjust(duration), (result) => result, { concurrent: true })`:
  V4 removed adjustWith. Run the tested effect and clock adjustment
  concurrently and retain the tested effect's result.
- `TestClock.currentTimeMillis` -> `Clock.currentTimeMillis`: Read time from
  the active Clock reference; under it.effect or TestClock.layer() this is
  virtual time.
- `TestClock.defaultTestClock` -> `TestClock.layer()`: The v4 layer creates an
  epoch-based test clock and captures the surrounding live Clock automatically;
  it no longer needs TestAnnotations or TestLive.
- `TestClock.makeData` -> `TestClock.layer() + TestClock.setTime(instant)`:
  State injection was removed. Build the layer, then set initial time; seeded
  pending sleeps cannot migrate because the queue is private.
- `TestClock.save` -> `none`: Full clock snapshots including pending sleeps are
  no longer public. For timestamp-only restoration, read
  Clock.currentTimeMillis and later call TestClock.setTime(savedMillis).
- `TestClock.sleeps` -> `none`: The pending-sleep queue is private. Test
  observable behavior by forking sleepers, adjusting time, and joining or
  asserting the fibers.
- `TestClock.testClock` -> `TestClock.testClockWith(Effect.succeed)`: V4
  exposes callback-based access to the active test clock; use testClockWith
  directly when possible.
