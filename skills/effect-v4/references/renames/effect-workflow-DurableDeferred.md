<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/workflow/DurableDeferred` v3 → v4

- `DurableDeferred.Any` -> `effect/workflow/DurableDeferred#Any`: Moved into
  core Effect. V4 Any is minimal; use AnyWithProps when success, error, or exit
  schemas are required.
- `DurableDeferred.TypeId` -> `none`: The durable-deferred marker is private in
  v4. Use DurableDeferred, Any, or AnyWithProps constraints.
- `DurableDeferred.await` -> `effect/workflow/DurableDeferred#await`: Moved
  into core Effect with the same persisted-result and workflow-suspension
  behavior.
- `DurableDeferred.done` -> `effect/workflow/DurableDeferred#done`: Moved into
  core Effect; schema requirements now use explicit directional encoding
  services.
- `DurableDeferred.fail` -> `effect/workflow/DurableDeferred#fail`: Moved into
  core Effect and now requires the error schema encoding services.
- `DurableDeferred.failCause` -> `effect/workflow/DurableDeferred#failCause`:
  Moved into core Effect and now requires the error schema encoding services.
- `DurableDeferred.into` -> `effect/workflow/DurableDeferred#into`: Moved into
  core Effect with the same exit recording and suspension propagation behavior.
  Provide both decoding and encoding services for the success and error
  schemas; recording the exit requires encoding services.
- `DurableDeferred.make` -> `effect/workflow/DurableDeferred#make`: Moved into
  core Effect with the same name and optional schemas, expressed through v4
  Schema.Constraint.
- `DurableDeferred.raceAll` -> `effect/workflow/DurableDeferred#raceAll`: Moved
  into core Effect with the same persisted-winner behavior.
- `DurableDeferred.succeed` -> `effect/workflow/DurableDeferred#succeed`: Moved
  into core Effect and now requires the success schema encoding services.
