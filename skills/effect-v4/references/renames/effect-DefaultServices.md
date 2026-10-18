<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/DefaultServices` v3 → v4

- `DefaultServices.DefaultServices` -> `none`: The aggregate type and module
  were removed; Clock, Console, Random, ConfigProvider, and Tracer are
  independent defaulted references.
- `DefaultServices.currentServices` ->
  `Effect.context() and Context.get(context, reference)`: The aggregate
  FiberRef was removed; access and override default Context.Reference services
  individually.
- `DefaultServices.liveServices` ->
  `Context.empty() with individual Context.Reference defaults`: There is no
  live-services bundle; each default service reference supplies its own live
  default.
