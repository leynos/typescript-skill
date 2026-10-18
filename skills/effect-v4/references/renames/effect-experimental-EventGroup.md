<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/experimental/EventGroup` v3 → v4

- `EventGroup.EventGroup.Any` -> `effect/eventlog/EventGroup#Any`: This type
  moved from the EventGroup namespace to a top-level export.
- `EventGroup.EventGroup.AnyWithProps` ->
  `effect/eventlog/EventGroup#AnyWithProps`: This type moved from the
  EventGroup namespace to a top-level export.
- `EventGroup.EventGroup.Context` ->
  `effect/eventlog/EventGroup#ServicesClient | effect/eventlog/EventGroup#ServicesServer`:
  Choose the client or server schema services for the required direction.
- `EventGroup.EventGroup.ToService` -> `effect/eventlog/EventGroup#ToService`:
  This type moved from the EventGroup namespace to a top-level export.
- `EventGroup.TypeId` -> `effect/eventlog/EventGroup#TypeId`: Import TypeId
  from the v4 unstable EventGroup module; its runtime representation is now a
  string brand.
