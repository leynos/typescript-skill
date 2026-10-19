<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/SingleProducerAsyncInput` v3 → v4

- `SingleProducerAsyncInput.AsyncInputConsumer` -> `Queue.Dequeue`: Use v4
  Queue producer and consumer views and bridge to Channel with
  Channel.fromQueue, Channel.callback, or Channel.fromPull. Queue.make({
  capacity: 0 }) is the closest rendezvous backpressure but is not one-for-one.
- `SingleProducerAsyncInput.AsyncInputProducer` -> `Queue.Enqueue`: Use v4
  Queue producer and consumer views and bridge to Channel with
  Channel.fromQueue, Channel.callback, or Channel.fromPull. Queue.make({
  capacity: 0 }) is the closest rendezvous backpressure but is not one-for-one.
- `SingleProducerAsyncInput.SingleProducerAsyncInput` -> `Queue.Queue`: Use v4
  Queue producer and consumer views and bridge to Channel with
  Channel.fromQueue, Channel.callback, or Channel.fromPull. Queue.make({
  capacity: 0 }) is the closest rendezvous backpressure but is not one-for-one.
- `SingleProducerAsyncInput.make` -> `Queue.make`: Use v4 Queue producer and
  consumer views and bridge to Channel with Channel.fromQueue,
  Channel.callback, or Channel.fromPull. Queue.make({ capacity: 0 }) is the
  closest rendezvous backpressure but is not one-for-one.
