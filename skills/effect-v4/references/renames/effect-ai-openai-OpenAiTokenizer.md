<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiTokenizer` v3 → v4

- `OpenAiTokenizer.layer` -> `Tokenizer.make`: The provider-specific tokenizer
  module was removed; build and provide an effect/ai/Tokenizer service
  explicitly, using gpt-tokenizer if equivalent OpenAI counting is required.
- `OpenAiTokenizer.make` -> `Tokenizer.make`: The provider-specific tokenizer
  module was removed; build and provide an effect/ai/Tokenizer service
  explicitly, using gpt-tokenizer if equivalent OpenAI counting is required.
