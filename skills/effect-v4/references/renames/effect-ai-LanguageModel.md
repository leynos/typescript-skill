<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/LanguageModel` v3 → v4

- `LanguageModel.ConstructorParams` -> `none`: V4 inlines this provider-adapter
  shape in LanguageModel.make. Pass generateText and streamText directly to
  make, with optional codecTransformer, instead of naming a
  constructor-parameter type.
- `LanguageModel.ExtractContext` -> `LanguageModel.ExtractServices`: Renamed in
  effect/ai/LanguageModel. ExtractServices infers toolkit handler,
  result-decoding, and effectful-toolkit service requirements.
- `LanguageModel.LanguageModel` -> `LanguageModel.LanguageModel`: Use the
  LanguageModel interface for implementations and the Context.Service value as
  the service key; it is no longer a class. Prefer LanguageModel.make to
  construct the branded implementation.
- `LanguageModel.Service` -> `LanguageModel.LanguageModel`: Service was renamed
  to LanguageModel. Implementations require [LanguageModel.TypeId]:
  LanguageModel.TypeId; LanguageModel.make supplies the brand.
