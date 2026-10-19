<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai/McpServer` v3 → v4

- `McpServer.McpServer` -> `McpServer.McpServer`: The service is now a
  Context.Service. initializedClients and notificationsMailbox are no longer
  exposed. Registration callbacks use McpSchema.McpRequestContext;
  McpServerClient is only supplied for initialized stateful requests. Prefer
  registerToolkit, registerResource, and registerPrompt over implementing the
  registry shape directly.
- `McpServer.layer` -> `McpServer.layer`: Moved to effect/ai/McpServer. Pass a
  non-empty protocols array of adapters, such as [McpProtocol.v2025\_06\_18],
  imported with McpProtocol from effect/ai; it still runs over a
  caller-provided RpcServer.Protocol.
- `McpServer.layerHttp` -> `McpServer.layerHttp`: Moved to effect/ai/McpServer
  and the unified HttpRouter. Pass a non-empty protocols array of adapters,
  such as [McpProtocol.v2025\_06\_18], imported with McpProtocol from effect/ai.
- `McpServer.layerHttpRouter` -> `McpServer.layerHttp`: Renamed and
  consolidated. V4 layerHttp registers the Streamable HTTP endpoint in the
  unified HttpRouter; pass a non-empty protocols array of adapters, such as
  [McpProtocol.v2025\_06\_18], imported with McpProtocol from effect/ai.
- `McpServer.layerStdio` -> `McpServer.layerStdio`: Moved to
  effect/ai/McpServer. Pass a non-empty protocols array of adapters, such as
  [McpProtocol.v2025\_06\_18], imported with McpProtocol from effect/ai.
- `McpServer.prompt` -> `McpServer.prompt`: Moved to effect/ai/McpServer. The
  registration layer excludes McpSchema.McpRequestContext from prompt decoding,
  handler, and completion callback requirements instead of McpServerClient.
- `McpServer.registerPrompt` -> `McpServer.registerPrompt`: Moved to
  effect/ai/McpServer. Prompt decoding, handler, and completion callback
  requirements now exclude McpSchema.McpRequestContext instead of
  McpServerClient; use the request context for protocol-neutral client metadata.
- `McpServer.registerResource` -> `McpServer.registerResource`: Moved to
  effect/ai/McpServer. Resource and completion handler requirements now exclude
  McpSchema.McpRequestContext instead of McpServerClient; use the request
  context for protocol-neutral client metadata.
- `McpServer.registerToolkit` -> `McpServer.registerToolkit`: Moved to
  effect/ai/McpServer. Requirements from every tool handler are propagated,
  excluding McpSchema.McpRequestContext instead of McpServerClient; provide the
  remaining handler services. Strict tools reject excess input properties; raw
  JSON Schema dynamic tools cannot use strict mode. Declared handler failures
  produce isError results, while parameter validation fails with InvalidParams.
- `McpServer.resource` -> `McpServer.resource`: Moved to effect/ai/McpServer.
  The registration layer excludes McpSchema.McpRequestContext from resource and
  completion handler requirements instead of McpServerClient.
- `McpServer.run` -> `McpServer.run`: Moved to effect/ai/McpServer. Pass a
  non-empty protocols array of adapters, such as [McpProtocol.v2025\_06\_18],
  imported with McpProtocol from effect/ai; it remains the Effect-level runner
  over RpcServer.Protocol.
- `McpServer.toolkit` -> `McpServer.toolkit`: Moved to effect/ai/McpServer. The
  registration layer supplies McpSchema.McpRequestContext to handlers instead
  of excluding McpServerClient from requirements. Its requirements include
  services from every tool handler. Strict tools reject excess properties and
  require an Effect Schema rather than raw dynamic JSON Schema.
