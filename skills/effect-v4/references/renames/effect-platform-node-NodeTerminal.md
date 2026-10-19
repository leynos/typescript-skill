<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform-node/NodeTerminal` v3 → v4

- `NodeTerminal.layer` -> `NodeTerminal.layer`: The default layer now ends key
  input on bare Esc as well as Ctrl+C and Ctrl+D. To keep Esc as input, build a
  layer with Layer.effect(Terminal.Terminal, NodeTerminal.make(shouldQuit))
  using a custom quit predicate.
- `NodeTerminal.make` -> `NodeTerminal.make`: V4 ends key input on bare Esc as
  well as Ctrl+C and Ctrl+D. Pass a custom shouldQuit predicate to make if your
  application needs to receive Esc; the v3 default quit only on Ctrl+C and
  Ctrl+D.
