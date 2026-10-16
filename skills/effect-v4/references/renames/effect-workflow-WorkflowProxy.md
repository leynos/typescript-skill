<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/WorkflowProxy` v3 → v4

- `WorkflowProxy.ConvertHttpApi` ->
  `effect/workflow/WorkflowProxy#ConvertHttpApi`: Moved into core Effect and
  updated to v4 HttpApiEndpoint types and the consolidated HttpApi architecture.
- `WorkflowProxy.ConvertRpcs` -> `effect/workflow/WorkflowProxy#ConvertRpcs`:
  Moved into core Effect; generated execute, discard, and resume RPCs are now
  keyed from workflow \_tag.
