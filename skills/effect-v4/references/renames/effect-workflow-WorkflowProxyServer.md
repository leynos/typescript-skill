<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/WorkflowProxyServer` v3 → v4

- `WorkflowProxyServer.layerHttpApi` ->
  `effect/workflow/WorkflowProxyServer#layerHttpApi`: Moved into core Effect.
  Use v4 HttpApi group identifiers and Workflow.RequirementsHandler schema
  services.
- `WorkflowProxyServer.layerRpcHandlers` ->
  `effect/workflow/WorkflowProxyServer#layerRpcHandlers`: Moved into core
  Effect; generated handlers require Workflow.RequirementsHandler rather than
  the undirected Requirements union.
