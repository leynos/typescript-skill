<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/MergeStrategy` v3 → v4

- `MergeStrategy.BackPressure` -> `Channel.mergeAll`: Remove the MergeStrategy
  value and configure the v4 merge directly: backpressure is the default;
  sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.BufferSliding` -> `Channel.mergeAll`: Remove the MergeStrategy
  value and configure the v4 merge directly: backpressure is the default;
  sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.MergeStrategy` -> `Channel.mergeAll`: Remove the MergeStrategy
  value and configure the v4 merge directly: backpressure is the default;
  sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.MergeStrategy.Proto` -> `Channel.mergeAll`: Remove the
  MergeStrategy value and configure the v4 merge directly: backpressure is the
  default; sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.MergeStrategyTypeId` -> `Channel.mergeAll`: Remove the
  MergeStrategy value and configure the v4 merge directly: backpressure is the
  default; sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.isBackPressure` -> `Channel.mergeAll`: Remove the
  MergeStrategy value and configure the v4 merge directly: backpressure is the
  default; sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.isBufferSliding` -> `Channel.mergeAll`: Remove the
  MergeStrategy value and configure the v4 merge directly: backpressure is the
  default; sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.isMergeStrategy` -> `Channel.mergeAll`: Remove the
  MergeStrategy value and configure the v4 merge directly: backpressure is the
  default; sliding replacement uses Channel.mergeAll with switch: true or
  Channel.switchMap.
- `MergeStrategy.match` -> `Channel.mergeAll`: Remove the MergeStrategy value
  and configure the v4 merge directly: backpressure is the default; sliding
  replacement uses Channel.mergeAll with switch: true or Channel.switchMap.
