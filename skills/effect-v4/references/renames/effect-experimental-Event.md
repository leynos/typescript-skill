<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/Event` v3 → v4

- `Event.Event.AddError` -> `effect/eventlog/Event#AddError`: This type moved
  from the Event namespace to a top-level export.
- `Event.Event.Any` -> `effect/eventlog/Event#Any`: This type moved from the
  Event namespace to a top-level export.
- `Event.Event.Context` -> `effect/eventlog/Event#Services`: Event schema
  context is now represented by decoding and encoding Services.
- `Event.Event.ContextWithTag` ->
  `effect/eventlog/Event#Services<effect/eventlog/Event#WithTag<Events, Tag>>`:
  Filter with WithTag and derive its decoding and encoding Services.
- `Event.Event.Error` -> `effect/eventlog/Event#Error`: This type moved from
  the Event namespace to a top-level export.
- `Event.Event.ErrorSchema` -> `effect/eventlog/Event#ErrorSchema`: This type
  moved from the Event namespace to a top-level export.
- `Event.Event.Payload` -> `effect/eventlog/Event#Payload`: This type moved
  from the Event namespace to a top-level export.
- `Event.Event.PayloadSchema` -> `effect/eventlog/Event#PayloadSchema`: This
  type moved from the Event namespace to a top-level export.
- `Event.Event.Success` -> `effect/eventlog/Event#Success`: This type moved
  from the Event namespace to a top-level export.
- `Event.Event.SuccessSchema` -> `effect/eventlog/Event#SuccessSchema`: This
  type moved from the Event namespace to a top-level export.
- `Event.Event.Tag` -> `effect/eventlog/Event#Tag`: This type moved from the
  Event namespace to a top-level export.
- `Event.Event.ToService` -> `effect/eventlog/Event#ToService`: This type moved
  from the Event namespace to a top-level export.
- `Event.TypeId` -> `effect/eventlog/Event#TypeId`: Import TypeId from the v4
  unstable Event module; its runtime representation is now a string brand.
- `Event.make` -> `effect/eventlog/Event#make`: Import make from the v4
  unstable Event module.
