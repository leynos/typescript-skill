<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/Activity` v3 → v4

- `Activity.Any` -> `effect/workflow/Activity#Any`: Moved into core Effect. V4
  Any is minimal; use AnyWithProps when schemas or execution properties are
  required.
- `Activity.CurrentAttempt` -> `effect/workflow/Activity#CurrentAttempt`: Moved
  into core Effect and changed from a Context.Tag subclass to a
  Context.Reference value with the same default of 1.
- `Activity.TypeId` -> `none`: The activity marker is private in v4. Use
  Activity, Activity.Any, or Activity.AnyWithProps constraints.
- `Activity.make` -> `effect/workflow/Activity#make`: Moved into core Effect
  with the same constructor shape, v4 Schema.Constraint service directions, and
  optional annotations.
- `Activity.raceAll` -> `effect/workflow/Activity#raceAll`: Moved into core
  Effect with the same named durable race behavior.
