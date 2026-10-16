---
name: typescript-quality-tools
description: Use for static quality tooling in TypeScript and JavaScript projects, assigning one owner to each concern across the TypeScript compiler, Biome, Oxlint and the shared df12-lints plugin, Stylelint, Semgrep, package checks, accessibility checks, and performance measurement, and deciding what static analysis must not pretend to know.
metadata:
  globs: "**/biome.json, **/biome.jsonc, **/.oxlintrc.json, **/oxlint.config.*, **/stylelint.config.*, **/.stylelintrc*, **/semgrep*.yml, **/tools/grit/**, **/package.json"
---

# TypeScript quality tools

Use this when the question is which tool should enforce a rule, how the tools
divide the work, and where static analysis stops and runtime evidence begins.
Skills encode judgement; references encode recipes; tools encode policy. The
shared `df12-lints` plugin is the executable source of truth for house rules.

## Working stance

- One owner per concern. Two tools checking the same thing disagree
  eventually, and the project then argues with its linters instead of its code.
- The compiler owns types. A lint rule that re-derives a type-level fact is
  slower and less accurate than `tsc`.
- Fast tools run on every save; slow tools run on pull requests; expensive
  tools run on a schedule. Cadence is part of the ownership decision.
- A rule exists to encode a settled policy. A policy that is still being
  argued is a review checklist item, not a rule.
- Static policy can point the torch; it cannot swear the dragon is there. The
  concerns in the third ring below are runtime evidence and must never be
  pretended into a lint rule.
- Prefer configuring an existing rule over writing one; prefer a conservative,
  AST-only custom rule over dataflow; prefer a Semgrep prototype over a
  half-right plugin rule.

## Owners

| Concern                                               | Owner                                                                  |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| Types, strictness, suppression validity               | `tsc` with the per-directory ratchet                                   |
| Formatting                                            | Biome                                                                  |
| General correctness and style lint, Grit patterns     | Biome (fast, on save)                                                  |
| House rules: complexity, JSDoc, custom structure      | Oxlint with the `df12-lints` JS plugin                                 |
| CSS tokens, units, `!important`, animation properties | Stylelint with the strict-value and high-performance-animation plugins |
| Cross-file semantic patterns, text-level policy       | Semgrep                                                                |
| Package shape and declarations                        | `publint`, `attw`, packed-install test                                 |
| Accessibility                                         | axe in component and end-to-end tests, Grit a11y patterns              |
| Spelling and prose                                    | `typos`, markdownlint                                                  |
| Frames, long tasks, queue depth, worker cost          | Traces, frame timing, benchmarks (not a linter)                        |

_Table 1: Each static concern and the single tool that owns it._

See [static-owners-matrix.md](references/static-owners-matrix.md) for the
reasoning per row and the estate's current arrangement.

## Three rings of enforcement

1. **High-confidence static policy.** Rules that are right nearly every time
   they fire: direct writes of static presentation values (`prefer-css-state`),
   layout-triggering properties in transitions and keyframes
   (`stylelint-high-performance-animation`), test IDs in markup, raw colour
   classes. Start each as a warning or a changed-code gate; promote when the
   false-positive rate is known. The rule specification and fixture policy are
   in [prefer-css-state.md](references/prefer-css-state.md).
2. **Conservative structural rules.** Patterns that need some flow analysis:
   layout read and write interleaving in one loop, repeated timer-driven writes
   to layout properties. Prototype in Semgrep or as an AST-only rule with
   explicit FLIP and adapter allowances; do not bless as fatal until real valid
   and invalid fixtures exist.
3. **Runtime evidence.** Whether a calculation is heavy enough for a worker,
   whether a queue needs dropping, whether a DOM read actually thrashes layout,
   whether an animation drops frames, whether a `Promise.all` is operationally
   unbounded. Traces, benchmarks, queue metrics, frame timing. Route to
   `browser-main-thread-performance`.

Browser rules are an opt-in preset for browser projects, not part of the
universal TypeScript baseline; a server package should not be lectured about
CSS.

## Decision surface

- **Adopting the shared plugin.** Install `df12-lints` as a pinned Git
  dependency, list it in `jsPlugins`, copy the sample configuration, and retire
  any vendored copy of the plugin. Bun consumers add it to
  `trustedDependencies`. Oxlint JS plugins are alpha; see
  [oxlint-js-plugins.md](references/oxlint-js-plugins.md) for the API facts as
  of its review date.
- **Biome configuration.** Biome's own deep dive owns rule selection,
  migration from ESLint and Prettier, CI, and hooks:
  [`biome-typescript`](../biome-typescript/SKILL.md). Load it when the question
  is Biome itself.
- **CSS policy.** Stylelint enforces tokens (`var(--…)` for colour), unit
  policy, and `!important`; adding the high-performance-animation rule covers
  layout-triggering transitions. See
  [stylelint-and-css-policy.md](references/stylelint-and-css-policy.md).
- **Suppressions.** Every suppression carries a reason; a CI count only falls.
  The same discipline as the compiler's, applied to `biome-ignore`,
  `oxlint-disable`, and `stylelint-disable`.
- **Testing a rule.** Behavioural tests that run the real linter against
  fixture workspaces and snapshot diagnostics, plus property tests over
  generated ASTs for counting rules. No autofix for a rule whose fix is an
  architectural choice.

## Red flags

- Two linters enabled for the same rule family with different settings.
- A vendored copy of the shared plugin drifting from the package.
- `noExplicitAny` off in the linter while the compiler is strict, with no
  ratchet plan.
- A Stylelint configuration present but the tool not installed or run.
- A lint rule that claims to know a computation is "too heavy".
- Browser rules in a server package's baseline.
- A custom rule with an autofix that picks a class name.
- A semantic CI step commented out because it was noisy, with no issue.

## Pairing

- Pair with `browser-main-thread-performance` to turn the CSS membrane into a
  rule, and to know what must stay runtime evidence.
- Pair with `typescript-types-and-apis` for the suppression ratchet.
- Pair with `react-and-accessible-ui` for test-ID and accessibility rules.
- Pair with `typescript-modules-and-packaging` for package checks.
