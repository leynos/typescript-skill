<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/DevTools/Client` v3 → v4

- `Client.Client` -> `effect/devtools/DevToolsClient#DevToolsClient`: Client
  was renamed to the DevToolsClient Context.Service class.
- `Client.ClientImpl` ->
  `effect/devtools/DevToolsClient#DevToolsClient["Service"]`: Use the service
  shape from DevToolsClient; unsafeAddSpan was replaced by sendUnsafe.
- `Client.layer` -> `effect/devtools/DevToolsClient#layer`: Import layer from
  the v4 unstable DevToolsClient module.
- `Client.make` -> `effect/devtools/DevToolsClient#make`: Import make from the
  v4 unstable DevToolsClient module.
