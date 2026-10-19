<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Message` v3 → v4

- `Message.serialize` -> `effect/cluster/Message#serialize`: Moved into core
  Effect. Pass the transport's codecFor as the second argument; use
  serializeEnvelope for the JSON Envelope.Encoded form.
