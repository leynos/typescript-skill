<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openrouter/OpenRouterClient` v3 → v4

- `OpenRouterClient.ChatStreamingChoice` -> `Generated.ChatStreamChoice`: The
  client-local streaming choice schema moved into the regenerated OpenRouter
  schema surface and changed shape.
- `OpenRouterClient.ChatStreamingMessageChunk` -> `Generated.ChatStreamDelta`:
  The client-local streaming message delta moved into the regenerated
  OpenRouter schema surface and changed shape.
- `OpenRouterClient.ChatStreamingMessageToolCall` ->
  `Generated.ChatStreamToolCall`: The client-local streaming tool-call delta
  moved into the regenerated OpenRouter schema surface and changed shape.
- `OpenRouterClient.ChatStreamingResponseChunk` ->
  `OpenRouterClient.ChatStreamingResponseChunkData`: The standalone streaming
  chunk schema was replaced by the decoded data type from
  Generated.ChatStreamingResponse.
