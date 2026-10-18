<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-anthropic/AnthropicTokenizer` v3 → v4

- `AnthropicTokenizer.layer` -> `Tokenizer.make`: The provider-specific
  tokenizer module was removed; build and provide an effect/ai/Tokenizer
  service explicitly, using @anthropic-ai/tokenizer if equivalent Anthropic
  counting is required.
- `AnthropicTokenizer.make` -> `Tokenizer.make`: The provider-specific
  tokenizer module was removed; build and provide an effect/ai/Tokenizer
  service explicitly, using @anthropic-ai/tokenizer if equivalent Anthropic
  counting is required.
