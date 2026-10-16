<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Entity` v3 → v4

- `Entity.HandlersFrom` -> `effect/cluster/Entity#HandlersFrom`: Moved into
  core Effect; handler results now use Rpc.WrapperOr, which accepts either the
  raw RPC result or its wrapper.
- `Entity.Replier.Success` -> `effect/cluster/Entity#Replier.Success`: Moved
  into core Effect; streaming replies may use Queue.Dequeue with Cause.Done
  instead of the removed Mailbox type.
- `Entity.TypeId` -> `none`: The entity marker is private in v4. Use
  Entity.isEntity for runtime refinement.
