<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/MessageStorage` v3 → v4

- `MessageStorage.Encoded` -> `effect/cluster/MessageStorage#Encoded`: Moved
  into core Effect; use the v4 Envelope.Encoded and Reply.Encoded aliases.
  Custom drivers now implement batched resetAddresses, and unprocessedMessages
  receives optional limit and address filters.
- `MessageStorage.make` -> `effect/cluster/MessageStorage#make`: Moved into
  core Effect. Context service projections now use the Service property instead
  of Type. Custom service implementations must also provide resetAddresses for
  batched mailbox resets.
- `MessageStorage.makeEncoded` -> `effect/cluster/MessageStorage#makeEncoded`:
  Moved into core Effect. Custom encoded drivers must replace resetAddress with
  resetAddresses and may use the new limit and addresses options passed to
  unprocessedMessages.
