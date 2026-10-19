<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/vitest/utils` v3 → v4

- `utils.assertFailure` -> `assertExitFailure`: For v3 Exit values, rename to
  assertExitFailure. In v4, assertFailure instead asserts Result.Failure.
- `utils.assertLeft` -> `assertFailure`: Either became Result in v4: migrate
  Left to Result.Failure, then use assertFailure; narrowed payload access
  changes from .left to .failure.
- `utils.assertMatch` -> `assertMatch`: Unchanged positional helper and
  behavior; only the parameter spelling changed, so call sites need no change.
- `utils.assertRight` -> `assertSuccess`: Either became Result in v4: migrate
  Right to Result.Success, then use assertSuccess; narrowed payload access
  changes from .right to .success.
- `utils.assertSuccess` -> `assertExitSuccess`: For v3 Exit values, rename to
  assertExitSuccess. In v4, assertSuccess instead asserts Result.Success.
