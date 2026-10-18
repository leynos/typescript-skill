<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cluster/Envelope` v3 → v4

- `Envelope.Envelope.Encoded` -> `effect/cluster/Envelope#Encoded`: The encoded
  envelope union moved to the module-level Encoded type.
- `Envelope.Envelope.PartialEncoded` -> `effect/cluster/Envelope#Partial`: The
  partially decoded runtime union was renamed to Partial; use PartialJson for
  its JSON codec.
- `Envelope.EnvelopeFromSelf` -> `effect/cluster/Envelope#Envelope`: The self
  schema was renamed to Envelope and declaration-merges with the envelope type
  and namespace.
- `Envelope.PartialEncoded` -> `effect/cluster/Envelope#PartialJson`: The
  partially decoded envelope JSON codec was renamed to PartialJson.
- `Envelope.PartialEncodedArray` -> `effect/cluster/Envelope#PartialArray`: The
  mutable array codec was renamed to PartialArray.
- `Envelope.PartialEncodedFromSelf` -> `effect/cluster/Envelope#Partial`: The
  separate self schema was folded into Partial; derive JSON encoding with
  PartialJson.
- `Envelope.PartialEncodedRequest` ->
  `Schema.toCodecJson(Envelope.PartialRequest)`: V4 exports the self schema as
  PartialRequest and derives its JSON codec with Schema.toCodecJson.
- `Envelope.PartialEncodedRequestFromSelf` ->
  `effect/cluster/Envelope#PartialRequest`: The partially decoded request self
  schema was renamed to PartialRequest.
- `Envelope.Request` -> `effect/cluster/Envelope#Request`: The request
  interface remains and declaration-merges with the exported Request schema.
- `Envelope.Request.Encoded` ->
  `effect/cluster/Envelope#PartialRequestEncoded`: The JSON request shape moved
  to the module-level PartialRequestEncoded interface.
- `Envelope.Request.PartialEncoded` ->
  `effect/cluster/Envelope#PartialRequest`: The partially decoded request shape
  moved to the module-level PartialRequest class and type.
- `Envelope.RequestFromSelf` -> `effect/cluster/Envelope#Request`: The request
  self schema was renamed to Request and declaration-merges with the runtime
  interface.
- `Envelope.TypeId` -> `typeof Envelope.TypeId`: The marker value remains, but
  the type alias was removed and the value is now a string literal; use typeof
  in type position.
