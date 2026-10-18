<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/PubSub` v3 → v4

- `PubSub.PubSub` -> `PubSub.PubSub`: The model remains but no longer extends
  Queue.Enqueue; replace Queue operations with explicit PubSub.publish,
  PubSub.publishAll, and PubSub.subscribe calls.
