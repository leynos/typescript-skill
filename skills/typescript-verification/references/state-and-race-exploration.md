# State and race exploration

## Model-based testing

A stateful system (a store, a protocol handler, a cache, a scheduler) is tested
against a simplified model across generated operation sequences. Each command
checks whether it applies in the current model state, runs against both the
model and the real system, and asserts they agree.

The model must be simpler than the system. A model that mirrors the
implementation tests the code against itself. Good models: a `Map` for a
key-value store, an array for a queue, a counter for a rate limiter, a
transition table for a state machine.

```ts
class ScheduleCommand implements fc.Command<Model, Worker> {
  constructor(readonly at: number, readonly event: Event) {}
  check(model: Model): boolean {
    return this.at >= model.now;
  }
  run(model: Model, real: Worker): void {
    model.pending.push({ at: this.at, event: this.event });
    real.schedule({ at: this.at, event: this.event });
    real.drainSync();
    // Scheduling alone must apply nothing, even with no advance to follow.
    expect(real.journal.length).toBe(model.applied);
  }
  toString(): string {
    return `schedule(${this.at}, ${this.event.type})`;
  }
}

class AdvanceCommand implements fc.Command<Model, Worker> {
  constructor(readonly ms: number) {}
  check(): boolean {
    return true;
  }
  run(model: Model, real: Worker): void {
    model.now += this.ms;
    const due = model.pending.filter((p) => p.at <= model.now);
    model.pending = model.pending.filter((p) => p.at > model.now);
    real.clock.advance(this.ms);
    real.drainSync();
    expect(real.journal.length).toBe(model.applied + due.length);
    model.applied += due.length;
  }
  toString(): string {
    return `advance(${this.ms})`;
  }
}
```

"Never applies a transition before its virtual timestamp" falls out of the
assertion in `AdvanceCommand`: the journal length equals the number of due
transitions and no more. The full mechanics (`fc.commands`, `fc.modelRun`,
replay with `replayPath`) are in the
[`fast-check` deep dive](../../fast-check/SKILL.md).

## Race exploration

`fc.scheduler()` reorders scheduled promises to explore interleavings. Wrap the
async operations under test with `s.schedule(...)`, drive with `s.waitFor`, and
assert the invariant after each run. Typical targets: a cache with concurrent
fills, a request deduplicator, a store that applies updates from two sources, a
shutdown sequence racing a late message.

Preconditions:

- The code under test accepts its promises or async functions through
  injectable ports, so the scheduler can wrap them.
- No real timers; use the scheduler's control or a virtual clock.
- The invariant is stated as a predicate over observable state, not as an
  expected sequence of calls.

## From exploration to proof

Move from sampled exploration to a proof when all of these hold:

- the property is load-bearing (ownership, money, permissions, terminal
  states, bounded resources);
- the function or kernel is pure, synchronous, and inside LemmaScript's
  supported fragment (no `async`, no closures over mutable state, no regex,
  integer semantics acceptable);
- a counter-example would be costly enough that sampled confidence is not
  acceptable.

Keep the `fast-check` property beneath the proof: it runs in milliseconds,
catches specification drift before a prover run, and covers the boundary code
the proof trusts. The [`lemmascript` deep dive](../../lemmascript/SKILL.md)
covers annotations, the edit loop, and brownfield strategy.

## What exploration cannot show

- That a property holds for inputs the arbitrary never generates. Audit the
  arbitrary first.
- That an interleaving the scheduler cannot produce (a real thread, a real
  network partition) is safe. Those need integration or chaos tests.
- That the model is right. Review the model as a specification.
