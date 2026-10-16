<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Scheduler` v3 → v4

- `Scheduler.ControlledScheduler` -> `none`: No public step-controlled
  scheduler remains; implement Scheduler and SchedulerDispatcher for exact
  controlled stepping.
- `Scheduler.MixedScheduler` -> `Scheduler.MixedScheduler`: The class remains
  with a redesigned constructor and makeDispatcher-based task API. On
  Cloudflare Workers, request-owned scheduler timers can leave shared fibers
  suspended; provide new Scheduler.MixedScheduler("sync") to both layers and
  requests and build handlers at module scope (see HttpRouter.toWebHandler).
  Sync mode does not yield to the event loop and does not fix request-owned
  Effect.sleep timers or request-bound async contexts.
- `Scheduler.PriorityBuckets` -> `none`: Priority buckets are now an internal
  Scheduler implementation detail.
- `Scheduler.Scheduler` -> `Scheduler.Scheduler`: The interface remains but
  dispatch moved to SchedulerDispatcher returned by makeDispatcher.
- `Scheduler.SchedulerRunner` -> `Scheduler.SchedulerDispatcher`: Task
  scheduling and flushing moved to the dispatcher returned by
  Scheduler.makeDispatcher.
- `Scheduler.SyncScheduler` -> `new Scheduler.MixedScheduler("sync")`: Use a
  synchronous MixedScheduler and its dispatcher; call flush when directly
  driving queued tasks.
- `Scheduler.Task` -> `() => void`: The named alias was removed; dispatcher
  APIs inline the task callback type.
- `Scheduler.defaultScheduler` -> `Scheduler.Scheduler`: The default scheduler
  is now a Context.Reference; yield it to read or provide it to override the
  current scheduler.
- `Scheduler.defaultShouldYield` -> `Scheduler.MixedScheduler#shouldYield`: The
  standalone function was removed; yielding is implemented by each Scheduler
  instance.
- `Scheduler.make` -> `none`: Implement the redesigned Scheduler interface and
  return task dispatch through makeDispatcher.
- `Scheduler.makeBatched` -> `new Scheduler.MixedScheduler("async", schedule)`:
  Pass a cancellable scheduling function; the dispatcher performs priority
  batching.
- `Scheduler.makeMatrix` -> `none`: Matrix routing was removed; implement
  routing in a custom Scheduler and SchedulerDispatcher if still required.
- `Scheduler.timer` -> `Effect.delay`: Use Effect delay or sleep for effect
  timing; implement a custom dispatcher for exact per-task scheduler timing.
- `Scheduler.timerBatched` ->
  `new Scheduler.MixedScheduler("async", scheduleWithTimer)`: Use a
  setTimeout-based cancellable scheduling function; the dispatcher batches
  queued tasks.
