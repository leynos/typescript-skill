<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/ClusterWorkflowEngine` v3 → v4

- `ClusterWorkflowEngine.layer` ->
  `effect/cluster/ClusterWorkflowEngine#layer`: Moved into core Effect with the
  same cluster-backed WorkflowEngine layer composition.
- `ClusterWorkflowEngine.make` -> `effect/cluster/ClusterWorkflowEngine#make`:
  Moved into core Effect; the constructor still uses Sharding and
  MessageStorage.
