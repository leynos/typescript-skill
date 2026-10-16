# Mutation testing

Mutation testing changes production code one small step at a time (flip a
comparison, drop a statement, replace a constant) and reruns the suite. A
mutant the suite does not kill is an assertion that does not bite.

## When

- The behaviour is already specified by tests that pass consistently.
- The question is "would these tests notice a plausible defect", not "is the
  code correct".
- The suite is fast and deterministic. A slow or flaky suite makes mutation
  runs take hours and report noise.

## Tool

StrykerJS (`@stryker-mutator/core`, 10.x at the time of writing) is the
JavaScript and TypeScript mutation framework. It supports Vitest, Jest, and
Mocha runners through plugins, and a command runner for others. Bun's test
runner needs the command runner or a shim; check the current plugin list before
adopting it.

## Shape of a rollout

1. **Scope.** Mutate the modules whose correctness matters most: transition
   functions, parsers, protocol handling, pricing. Exclude generated code,
   adapters, UI components, and anything with heavy I/O.
2. **Informational first.** Run on a schedule (nightly or weekly) and publish
   the score and the survivor list. Never gate pull requests on it in the first
   months; the first run will have hundreds of survivors.
3. **Triage.** Each survivor is one of: a missing assertion (write it), an
   equivalent mutant (mark it with a comment and the tool's ignore directive),
   or dead code (delete it).
4. **Incremental mode.** Use the tool's incremental or changed-files mode so a
   daily run mutates only what changed and stays cheap.
5. **Threshold, eventually.** Once the survivor list is a short, understood
   set, a `break` threshold on the scoped modules can gate; keep it narrow.

## Reading the result

- A killed mutant proves one assertion bites once. It says nothing about
  mutants the tool does not generate.
- A surviving mutant in a property test's target usually means the property is
  weaker than it looks (an oracle too close to the implementation, a relation
  that holds for the mutant too).
- A high score on a module with no behavioural tests is suspicious: look for
  tests that assert the implementation rather than the behaviour.

## The deliberate-mutation habit

Independent of the tool: before considering a property or a test finished,
break the production code by hand, run the test, confirm it fails with a useful
message, and restore. The estate's verification review trigger expects this,
and it takes a minute.

## Why no specialist yet

No project in the estate runs StrykerJS today. The selector reserves mutation
testing's place and carries this guidance. A deep-dive skill arrives when a
project adopts the tool and produces real configuration, survivor triage, and
CI wiring to write from, rather than being manufactured for symmetry.
