<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-anthropic/AnthropicTool` v3 → v4

- `AnthropicTool.ProviderDefinedTools` -> `AnthropicTool.AnthropicTool`: The
  provider-defined schema union was replaced by the union of v4 Anthropic
  provider tool constructor return types.
- `AnthropicTool.getProviderDefinedToolName` -> `Tool.NameMapper`: The
  Anthropic-specific name lookup was removed; v4 provider tools carry custom
  and provider names through the shared Tool.NameMapper.
