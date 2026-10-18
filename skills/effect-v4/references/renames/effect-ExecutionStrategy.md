<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ExecutionStrategy` v3 → v4

- `ExecutionStrategy.ExecutionStrategy` ->
  `Types.Concurrency | Scope.ExecutionStrategy`: The ADT was removed; use
  number | unbounded for operation concurrency, or sequential | parallel for
  Scope finalizers.
- `ExecutionStrategy.Parallel` -> `"parallel" | "unbounded"`: The tagged case
  was removed; use the consumer-specific primitive value.
- `ExecutionStrategy.ParallelN` -> `number`: The tagged case was removed;
  bounded operation concurrency is represented directly by a number.
- `ExecutionStrategy.Sequential` -> `"sequential" | 1`: The tagged case was
  removed; use the consumer-specific primitive value.
- `ExecutionStrategy.isParallel` -> `strategy === "parallel"`: Compare the
  Scope strategy directly; for concurrency options compare with unbounded.
- `ExecutionStrategy.isParallelN` -> `typeof concurrency === "number"`: Bounded
  parallelism is represented directly by a numeric concurrency value.
- `ExecutionStrategy.isSequential` -> `strategy === "sequential"`: Compare the
  Scope strategy directly; for operation concurrency use the value 1.
- `ExecutionStrategy.match` -> `switch`: Use ordinary branching over the
  consumer-specific concurrency or Scope strategy primitive.
- `ExecutionStrategy.parallel` -> `"parallel" | "unbounded"`: Use parallel for
  Scope finalizers or unbounded for operation concurrency.
- `ExecutionStrategy.parallelN` -> `number`: Pass the parallelism directly as a
  numeric concurrency option; Scope has no bounded parallel strategy.
- `ExecutionStrategy.sequential` -> `"sequential" | 1`: Use sequential for
  Scope finalizers or 1 for operation concurrency.
