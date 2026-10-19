# The testing hierarchy

A decision hierarchy, not a prestige ranking. Each rung answers a different
question; climb only when the question changes.

| Rung | Evidence                                          | Tool                                        | Signal that the rung is wrong                                                   |
| ---- | ------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------- |
| 0    | The compiler rejects the illegal shape            | Types; `.test-d.ts` for public vocabularies | A runtime test asserts what a type already guarantees                           |
| 1    | One scenario behaves as specified                 | A named test                                | The name is "works" or "handles input"                                          |
| 2    | Each row of a finite table behaves as specified   | `test.each` or a loop over named cases      | Rows differ only in a number and sample one relation                            |
| 3    | One relation holds over many cheap inputs         | `fast-check` property                       | The property filters most inputs, or needs a model                              |
| 4    | A sequence of operations keeps an invariant       | `fast-check` commands or scheduler          | The model mirrors the implementation                                            |
| 5    | A property holds for every input, unconditionally | LemmaScript proof                           | The code is outside the supported fragment, or the property is not load-bearing |

_Table 1: The rungs, the evidence each produces, and the tool for each._

Beside the hierarchy: **mutation testing** (does the suite notice a plausible
defect?). Outside it: component, integration, end-to-end, benchmark, and
packed-install tests, each answering a question the hierarchy cannot.

## Examples remain valuable at every rung

Keep exact protocol examples and named regressions beside a property. A
property searches the domain; an example documents a case a human cared about.
Do not delete readable specification because a generator can rediscover it.

## Rung 1 and 2 shapes

```ts
test("rejects a connecting state that receives hangup by closing", () => {
  expect(transition({ kind: "connecting", attempt: 1 }, { type: "hangup" }))
    .toEqual({ kind: "closed", reason: "hung up while connecting" });
});

test.each([
  ["idle", "dial", "connecting"],
  ["connecting", "opened", "open"],
  ["open", "hangup", "closed"],
  ["closed", "dial", "closed"],
] as const)("%s + %s -> %s", (from, event, to) => {
  expect(transition(stateOf(from), eventOf(event)).kind).toBe(to);
});
```

The table is the transition specification; every cell is a sentence someone
would write in a design document. When a row says "attempt 1", "attempt 2",
"attempt 17" to check that attempts never exceed three, the table has become a
sample of a relation. That relation is rung 3.

## Mutation testing

StrykerJS mutates production code and reruns the suite; survivors are
assertions that do not bite. Use it:

- as an informational, scheduled job, never a pull-request gate;
- scoped to the modules whose correctness matters most, with generated code
  and adapters excluded;
- as a worklist: each survivor becomes a stronger assertion or a documented
  equivalent mutant.

A dedicated deep dive waits until a project in the estate adopts the tool.
Until then, `typescript-verification` carries the selection guidance.

## Runner choice

| Runner      | Fits                                                   | Note                                                     |
| ----------- | ------------------------------------------------------ | -------------------------------------------------------- |
| `bun test`  | Bun-first packages; fast; Jest-like API; `--randomize` | Concurrency and shuffle flags surface order dependence   |
| Vitest      | Vite applications; browser mode; rich plugin ecosystem | Also hosts jest-axe accessibility suites with a full DOM |
| `node:test` | Dependency-free Node libraries                         | Smaller matcher surface; pair with `node:assert/strict`  |
| Playwright  | Browser and Electron end-to-end                        | Not a unit runner; keep it for what needs a real browser |

_Table 2: Test runners and where each fits._

One unit runner per package. A second runner is justified only for a different
environment (a full DOM for accessibility assertions, a real browser for
end-to-end), and it runs a separate suite.
