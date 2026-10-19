<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/ClusterSchema` v3 → v4

- `ClusterSchema.ClientTracingEnabled` ->
  `effect/cluster/ClusterSchema#ClientTracingEnabled`: Moved into core Effect
  and changed from a Context.Tag subclass to a Context.Reference value.
- `ClusterSchema.Persisted` -> `effect/cluster/ClusterSchema#Persisted`: Moved
  into core Effect and changed from a Context.Tag subclass to a
  Context.Reference value with the same false default.
- `ClusterSchema.ShardGroup` -> `effect/cluster/ClusterSchema#ShardGroup`:
  Moved into core Effect and changed from a Context.Tag subclass to a
  Context.Reference value.
- `ClusterSchema.Uninterruptible` ->
  `effect/cluster/ClusterSchema#Uninterruptible`: Now a Context.Reference
  value. Replace its static methods with
  ClusterSchema.isUninterruptibleForServer and isUninterruptibleForClient.
