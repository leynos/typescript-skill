<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiLanguageModel` v3 → v4

- `OpenAiLanguageModel.ProviderMetadata` ->
  `Prompt.ProviderOptions / Response.ProviderMetadata`: The OpenAI metadata
  service wrapper was removed; v4 declares OpenAI-specific fields directly on
  Prompt and Response provider metadata.
- `OpenAiLanguageModel.ProviderMetadata.Service` ->
  `Prompt.ProviderOptions / Response.ProviderMetadata`: The OpenAI metadata
  service wrapper was removed; v4 declares OpenAI-specific fields directly on
  Prompt and Response provider metadata.
- `OpenAiLanguageModel.layerWithTokenizer` -> `OpenAiLanguageModel.layer`: The
  tokenizer-combining layer was removed; provide the language model and any
  Tokenizer service separately.
- `OpenAiLanguageModel.modelWithTokenizer` -> `OpenAiLanguageModel.model`: The
  tokenizer-combining model was removed; use the v4 model descriptor and
  provide any Tokenizer service separately.
