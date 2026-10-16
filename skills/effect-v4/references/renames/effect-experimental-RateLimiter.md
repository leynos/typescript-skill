<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/RateLimiter` v3 → v4

- `RateLimiter.ErrorTypeId` -> `effect/persistence/RateLimiter#ErrorTypeId`:
  Retained as a string brand; the runtime marker now uses the persistence
  module path.
- `RateLimiter.RateLimiterError` ->
  `effect/persistence/RateLimiter#RateLimiterError`: The retained name is now a
  wrapper error class whose reason is RateLimitExceeded or RateLimitStoreError.
- `RateLimiter.RateLimiterStore` -> `RateLimiter.RateLimiterStore`: Use the
  Context.Service class from effect/persistence/RateLimiter. Custom tokenBucket
  implementations must return [remaining, elapsedMillis] instead of a number,
  preserving fractional counts and elapsed refill time.
- `RateLimiter.TypeId` -> `effect/persistence/RateLimiter#TypeId`: Import
  TypeId from the v4 unstable RateLimiter module; it is now a string brand.
- `RateLimiter.makeSleep` -> `effect/persistence/RateLimiter#sleep`: The
  accessor Effect was replaced by sleep; obtain the RateLimiter service and
  pass it to sleep directly or with its curried overload.
