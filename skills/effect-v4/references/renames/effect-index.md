<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/index` v3 → v4

- `index.Context` -> `Context`: Keep importing Context from effect; v4 removes
  declaration merges that made tags and references STM subtypes.
- `index.Effect` -> `Effect`: Keep importing Effect from effect; v4 removes
  declaration merges that made Effects structural Sink, Stream, and Channel
  subtypes.
- `index.Either` -> `Result`: Either was renamed to Result; Right and Left
  became Success and Failure, with Result.succeed and Result.fail constructors.
- `index.Option` -> `Option`: Keep importing Option from effect; Option is no
  longer an Effect or STM subtype, so use Effect.fromOption when needed.
