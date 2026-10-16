# `prefer-css-state` and the browser preset

A specification for the first browser rule in `df12-lints`, and the fixture
policy that makes it trustworthy. The rule does not exist yet; this is the
proposal the plugin should implement.

## What it reports

Direct writes of static presentation values from application code:

```ts
element.style.display = "none";
element.style.opacity = "0";
element.style.transform = "scale(0.98)";
element.style.setProperty("background-color", "red", "important");
```

Static means a literal or a value that is not a CSS custom property. The rule
reports the assignment or `setProperty` call, names the property, and
recommends in order:

1. a semantic class;
2. a `data-state` attribute;
3. a CSS custom property for a genuinely dynamic scalar;
4. a documented imperative escape hatch.

No autofix: choosing the class name is architecture, not punctuation.

## What it allows

| Allowance                             | Mechanism                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Custom properties                     | `setProperty` whose first argument starts with `--`                                             |
| Known geometry adapters               | Option: a list of module globs (`**/split-pane.tsx`)                                            |
| Canvas, WebGL, map, terminal adapters | Option: module globs; the rule never reads library code                                         |
| Explicit FLIP sections                | A `// flip:start` … `// flip:end` block comment pair, or a wrapper function name in the options |
| Generated files                       | Standard ignore patterns                                                                        |
| Tests and reference mockups           | Standard ignore patterns (`**/*.test.tsx`, `**/examples/**`)                                    |
| Scoped suppression                    | `// oxlint-disable-next-line df12/prefer-css-state -- reason` with a reason required            |

_Table 1: Allowances the rule must honour._

## Rollout

- Ship in an opt-in browser preset, never in the universal TypeScript
  baseline.
- Start as a warning or a changed-code gate (only files touched in the pull
  request).
- Promote to an error once the two front ends run it for a release with a
  known false-positive rate.

## Fixtures

Draw valid and invalid fixtures from the estate before writing the rule:

- **Invalid:** `style.display` toggles and a timer-driven `style.transform`
  scale effect in reference mockups; a `style.padding` write to a terminal
  element; a `background-color` write with `!important`.
- **Valid:** a split pane writing `--split-position` through `setProperty`; a
  map adapter module listed in the allowance; a FLIP block; a one-shot
  `requestAnimationFrame` that touches no style at all (not this rule's
  concern).

The reference mockups also demonstrate why file scope matters: they live under
legacy directories that the rule must ignore.

## Testing the rule

- Behavioural tests spawn the real linter against a temporary workspace with a
  generated configuration and snapshot the diagnostics, as the plugin already
  does for its JSDoc rules.
- Property tests generate assignments with `fast-check` (property name, value
  kind, `setProperty` versus assignment, custom property or not) and assert the
  report decision matches a reference predicate.
- A negative control: the same fixtures with the preset disabled produce no
  diagnostics.

## Two further rules, later

- `df12/no-layout-read-write-interleaving`: detect the obvious loop-local
  pattern where a layout-sensitive read (`getBoundingClientRect`,
  `offsetWidth`) and an invalidating write alternate. FLIP must be a valid
  fixture. Cross-branch flow analysis is beyond a small AST rule; prototype in
  Semgrep first.
- `df12/no-js-layout-animation`: detect repeated timer or
  `requestAnimationFrame` updates to layout properties (`top`, `left`, `width`,
  `height`), leaving one-shot writes and listed geometry adapters alone.

Neither is fatal until real fixtures exist.
