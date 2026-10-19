<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/EntityResource` v3 → v4

- `EntityResource.TypeId` -> `effect/cluster/EntityResource#TypeId`: Moved into
  core Effect; its literal changed to \~effect/cluster/EntityResource.
- `EntityResource.make` -> `effect/cluster/EntityResource#make`: Moved into
  core Effect. Acquisition is lazy by default in v4; set acquireEagerly: true
  to preserve v3 behavior.
