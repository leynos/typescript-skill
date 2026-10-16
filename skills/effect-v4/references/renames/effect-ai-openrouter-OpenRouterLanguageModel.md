<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openrouter/OpenRouterLanguageModel` v3 → v4

- `OpenRouterLanguageModel.OpenRouterReasoningInfo` ->
  `OpenRouterLanguageModel.ReasoningDetails`: The bespoke reasoning-info union
  was replaced by the provider's raw reasoning-details array, preserved through
  Prompt options and Response metadata.
