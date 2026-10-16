<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Reply` v3 → v4

- `Reply.Reply` -> `Reply.Reply(rpc, codecFor)`: Pass the transport codec.
  Decoding replies requires Rpc.ServicesClient; encoding replies requires
  Rpc.ServicesServer.
- `Reply.ReplyEncoded` -> `effect/cluster/Reply#Encoded`: Renamed to Encoded
  and no longer parameterized by an Rpc; payload fields are unknown and
  validated by Reply.Reply(rpc, codecFor) with the transport's codec.
- `Reply.TypeId` -> `none`: The reply marker is private in v4. Use
  Reply.isReply for runtime refinement.
- `Reply.serialize` -> `effect/cluster/Reply#serialize`: Moved into core Effect
  and now returns the non-generic Reply.Encoded wire union. Pass the
  transport's codecFor as the second argument.
