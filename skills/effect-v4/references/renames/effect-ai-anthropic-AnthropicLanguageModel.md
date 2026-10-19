<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-anthropic/AnthropicLanguageModel` v3 → v4

- `AnthropicLanguageModel.AnthropicReasoningInfo` ->
  `Prompt.ReasoningPartOptions / Response reasoning metadata`: The standalone
  reasoning-info union was removed; v4 declares Anthropic thinking and
  redacted-thinking data directly on Prompt and Response provider metadata.
- `AnthropicLanguageModel.AnthropicTools` ->
  `AnthropicLanguageModel.AnthropicUserDefinedTool | AnthropicLanguageModel.AnthropicProviderDefinedTool`:
  The old combined tool union was split into explicit user-defined and
  provider-defined Anthropic request tool types.
- `AnthropicLanguageModel.layerWithTokenizer` ->
  `AnthropicLanguageModel.layer`: The tokenizer-combining layer was removed;
  provide the language model and any Tokenizer service separately.
- `AnthropicLanguageModel.modelWithTokenizer` ->
  `AnthropicLanguageModel.model`: The tokenizer-combining model was removed;
  use the v4 model descriptor and provide any Tokenizer service separately.
- `AnthropicLanguageModel.prepareTools` -> `none`: Tool conversion became an
  internal part of the v4 Anthropic language model; use AnthropicTool
  constructors and pass tools through LanguageModel provider options instead.
