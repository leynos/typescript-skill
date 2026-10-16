<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Readable` v3 → v4

- `Readable.Readable` -> `Effect.Effect`: The branded wrapper was removed;
  represent read access directly as Effect.Effect\<A, E, R\>.
- `Readable.TypeId` -> `Effect.TypeId`: The Readable brand was removed; use
  Effect.TypeId only when branding checks remain necessary after collapsing to
  Effect.
- `Readable.isReadable` -> `Effect.isEffect`: Readable was removed; after
  representing reads directly as Effect, use the Effect guard.
- `Readable.make` -> `Effect.Effect`: Use the supplied Effect directly; the v3
  constructor only wrapped it as a get property.
- `Readable.map` -> `Effect.map`: Represent Readable as Effect and map it
  directly.
- `Readable.mapEffect` -> `Effect.flatMap`: Represent Readable as Effect and
  flatMap it directly.
- `Readable.unwrap` -> `Effect.flatten`: After replacing the inner Readable
  with Effect, flatten the nested Effect directly.
