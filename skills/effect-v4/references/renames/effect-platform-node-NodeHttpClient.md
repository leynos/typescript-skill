<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeHttpClient` v3 → v4

- `NodeHttpClient.Dispatcher` -> `NodeHttpClient.Dispatcher`: The identifier
  remains but is now a Context.Service class; use Dispatcher["Service"] for the
  concrete Undici dispatcher type.
- `NodeHttpClient.HttpAgent` -> `NodeHttpClient.HttpAgent`: The identifier
  remains but is now a Context.Service class; use HttpAgent["Service"] for the
  concrete http/https agent pair.
- `NodeHttpClient.HttpAgentTypeId` -> `none`: The public marker was removed;
  the HttpAgent Context.Service class supplies service identity.
- `NodeHttpClient.UndiciRequestOptions` -> `NodeHttpClient.UndiciOptions`: The
  required Context.Tag became a defaulted
  Context.Reference\<Partial\<Dispatcher.RequestOptions\>\>; override it with
  Effect.provideService.
- `NodeHttpClient.agentLayer` -> `NodeHttpClient.layerAgent`: Direct rename; it
  provides the default scoped Node HTTP and HTTPS agents.
- `NodeHttpClient.dispatcherLayer` -> `NodeHttpClient.layerDispatcher`: Direct
  rename; the layer owns and finalizes a scoped Undici Agent.
- `NodeHttpClient.layer` -> `NodeHttpClient.layerNodeHttp`: Use the renamed
  node:http/node:https backend layer; choose layerUndici only when
  intentionally changing backends.
- `NodeHttpClient.layerUndiciWithoutDispatcher` ->
  `NodeHttpClient.layerUndiciNoDispatcher`: Direct rename; the layer still
  requires NodeHttpClient.Dispatcher.
- `NodeHttpClient.layerWithoutAgent` -> `NodeHttpClient.layerNodeHttpNoAgent`:
  Direct rename; the node:http client layer still requires
  NodeHttpClient.HttpAgent.
- `NodeHttpClient.make` -> `NodeHttpClient.makeNodeHttp`: Direct rename of the
  node:http/node:https client constructor.
- `NodeHttpClient.makeAgentLayer` -> `NodeHttpClient.layerAgentOptions`: Direct
  rename; it accepts Https.AgentOptions and scopes both agents.
