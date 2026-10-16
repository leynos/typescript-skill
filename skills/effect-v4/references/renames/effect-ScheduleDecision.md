<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/ScheduleDecision` v3 → v4

- `ScheduleDecision.Done` -> `Cause.Done`: ScheduleDecision was removed from
  the v4 public model. A Schedule.fromStep step recurs by returning [output,
  Duration] and terminates with Cause.done(output).
- `ScheduleDecision.ScheduleDecision` -> `none`: ScheduleDecision was removed
  from the v4 public model. A Schedule.fromStep step recurs by returning
  [output, Duration] and terminates with Cause.done(output).
- `ScheduleDecision.continue` -> `Effect.succeed([output, duration])`:
  ScheduleDecision was removed from the v4 public model. A Schedule.fromStep
  step recurs by returning [output, Duration] and terminates with
  Cause.done(output).
- `ScheduleDecision.continueWith` -> `Effect.succeed([output, duration])`:
  ScheduleDecision was removed from the v4 public model. A Schedule.fromStep
  step recurs by returning [output, Duration] and terminates with
  Cause.done(output).
- `ScheduleDecision.isContinue` -> `none`: ScheduleDecision was removed from
  the v4 public model. A Schedule.fromStep step recurs by returning [output,
  Duration] and terminates with Cause.done(output). Branch on the Pull result
  instead of inspecting a decision value.
- `ScheduleDecision.isDone` -> `Cause.isDone`: ScheduleDecision was removed
  from the v4 public model. A Schedule.fromStep step recurs by returning
  [output, Duration] and terminates with Cause.done(output).
