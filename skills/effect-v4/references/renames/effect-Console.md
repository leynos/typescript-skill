<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/Console` v3 → v4

- `Console.Console` -> `Console.Console`: Name retained, but v4 is a
  Context.Reference whose service methods are synchronous. Rewrite custom
  implementations from effectful methods plus .unsafe to direct console
  methods; module accessors such as Console.log still return Effect values.
- `Console.TypeId` -> `none`: The public console brand was removed; v4
  Console.Console is structural.
- `Console.UnsafeConsole` -> `Console.Console`: The v4 service interface is the
  old unsafe/direct interface; .unsafe no longer exists.
- `Console.setConsole` -> `Layer.succeed(Console.Console, console)`: Provide
  the v4 console reference as a layer.
- `Console.withConsole` ->
  `Effect.provideService(effect, Console.Console, console)`: Console overrides
  now use the reference/service provider pattern.
- `Console.withGroup` -> `Console.withGroup`: The API and data-first/data-last
  behavior remain.
- `Console.withTime` -> `Console.withTime`: The API and data-first/data-last
  behavior remain.
