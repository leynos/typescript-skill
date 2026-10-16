<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/WorkflowEngine` v3 → v4

- `WorkflowEngine.makeUnsafe` -> `effect/workflow/WorkflowEngine#makeUnsafe`:
  Moved into core Effect. Context service projections now use Service instead
  of Type, and absent encoded results use Option.
