<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ExecutionPlan` v3 → v4

- `ExecutionPlan.ExecutionPlan` -> `ExecutionPlan.ExecutionPlan`: The plan type
  remains; withRequirements was renamed to captureRequirements. Step schedules
  use Schedule\<Output, Input, Error, Requirements\>; captureRequirements
  supplies captured services to schedule initialization and execution.
- `ExecutionPlan.TypesBase` -> `ExecutionPlan.ConfigBase`: The base type for
  execution-plan step configuration was renamed.
- `ExecutionPlan.make` -> `ExecutionPlan.make`: The constructor remains
  variadic. Its inferred error channel includes failures from step layers,
  predicates, and schedules; requirements include services needed by all three
  across every step.
