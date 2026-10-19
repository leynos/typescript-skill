<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/ClusterError` v3 → v4

- `ClusterError.TypeId` -> `none`: The shared marker is private in v4. Use the
  exported tagged error classes, their \_tag fields, or class-specific is
  guards.
