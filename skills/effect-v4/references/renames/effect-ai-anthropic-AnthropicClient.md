<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-anthropic/AnthropicClient` v3 → v4

- `AnthropicClient.CitationsDelta` -> `Generated.BetaCitationsDelta`: The
  client-local stream schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.ContentBlockDeltaEvent` ->
  `Generated.BetaContentBlockDeltaEvent`: The client-local stream schema moved
  to the regenerated v4 Anthropic schema surface; re-check its Type/Encoded
  shape.
- `AnthropicClient.ContentBlockStartEvent` ->
  `Generated.BetaContentBlockStartEvent`: The client-local stream schema moved
  to the regenerated v4 Anthropic schema surface; re-check its Type/Encoded
  shape.
- `AnthropicClient.ContentBlockStopEvent` ->
  `Generated.BetaContentBlockStopEvent`: The client-local stream schema moved
  to the regenerated v4 Anthropic schema surface; re-check its Type/Encoded
  shape.
- `AnthropicClient.ErrorEvent` -> `Generated.BetaErrorResponse`: The
  client-local stream error schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.InputJsonContentBlockDelta` ->
  `Generated.BetaInputJsonContentBlockDelta`: The client-local stream schema
  moved to the regenerated v4 Anthropic schema surface; re-check its
  Type/Encoded shape.
- `AnthropicClient.MessageDelta` -> `Generated.BetaMessageDelta`: The
  client-local stream schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.MessageDeltaEvent` -> `Generated.BetaMessageDeltaEvent`: The
  client-local stream schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.MessageDeltaUsage` ->
  `typeof Generated.BetaMessageDeltaEvent.Type["usage"]`: The standalone usage
  schema was inlined into the regenerated v4 message-delta event.
- `AnthropicClient.MessageStartEvent` -> `Generated.BetaMessageStartEvent`: The
  client-local stream schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.MessageStopEvent` -> `Generated.BetaMessageStopEvent`: The
  client-local stream schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.PingEvent` -> `none`: The v4 client consumes ping events
  internally and filters them from MessageStreamEvent, so no public ping schema
  is needed.
- `AnthropicClient.ServerToolUsage` -> `Generated.BetaServerToolUsage`: The
  client-local usage schema moved to the regenerated v4 Anthropic schema
  surface; re-check its Type/Encoded shape.
- `AnthropicClient.SignatureContentBlockDelta` ->
  `Generated.BetaSignatureContentBlockDelta`: The client-local stream schema
  moved to the regenerated v4 Anthropic schema surface; re-check its
  Type/Encoded shape.
- `AnthropicClient.TextContentBlockDelta` ->
  `Generated.BetaTextContentBlockDelta`: The client-local stream schema moved
  to the regenerated v4 Anthropic schema surface; re-check its Type/Encoded
  shape.
- `AnthropicClient.ThinkingContentBlockDelta` ->
  `Generated.BetaThinkingContentBlockDelta`: The client-local stream schema
  moved to the regenerated v4 Anthropic schema surface; re-check its
  Type/Encoded shape.
