<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `effect/StreamEmit` v3 → v4

- `StreamEmit.EmitOps` ->
  `Queue.offer / Queue.offerAll / Queue.end / Queue.fail / Queue.failCause`:
  Method-by-method mapping onto the Queue passed to Stream.callback: single(a)
  -\> Queue.offer(queue, a); chunk(c) -\> Queue.offerAll(queue, c); end() -\>
  Queue.end(queue); fail(e) -\> Queue.fail(queue, e); halt(cause) -\>
  Queue.failCause(queue, cause); die(d)/dieMessage(m) -\>
  Queue.failCause(queue, Cause.die(d)); done(exit) -\> Queue.offer then
  Queue.end on success, Queue.failCause on failure; fromEffect(eff) -\> run eff
  and offer its value (Effect.flatMap(eff, (a) =\> Queue.offer(queue, a))).
- `StreamEmit.EmitOpsPush` ->
  `Queue.offerUnsafe / Queue.offerAllUnsafe / Queue.endUnsafe / Queue.failCauseUnsafe`:
  The synchronous push interface of v3 Stream.asyncPush maps to the \*Unsafe
  Queue operations on the Queue given to Stream.callback: single/array -\>
  Queue.offerUnsafe/Queue.offerAllUnsafe, end -\> Queue.endUnsafe,
  fail/halt/die -\> Queue.failCauseUnsafe (wrap plain errors with Cause.fail,
  defects with Cause.die).
