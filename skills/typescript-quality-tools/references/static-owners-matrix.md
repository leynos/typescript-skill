# Static owners matrix

## Why one owner per concern

| Concern                                 | Owner                             | Why this tool                                                                                       | Cadence            |
| --------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------ |
| Types and strictness                    | `tsc`                             | Only the checker knows the types; lint re-derivations are approximations                            | Save, push         |
| Formatting                              | Biome                             | One formatter; no second opinion                                                                    | Save               |
| General lint, Grit patterns             | Biome                             | Fast enough for every save; GritQL patterns express project conventions without writing a plugin    | Save, push         |
| House rules (complexity, JSDoc, custom) | Oxlint + `df12-lints`             | The shared plugin is where estate-wide rules live; Oxlint runs ESLint-compatible JS plugins quickly | Push, pull request |
| CSS policy                              | Stylelint                         | The CSS parser lives there; re-implementing it in Oxlint is wasted effort                           | Push               |
| Cross-file text patterns                | Semgrep                           | Pattern language suits prototypes and text-level policy; slower, so pull request                    | Pull request       |
| Package shape                           | `publint`, `attw`, packed test    | They test the artefact, not the source                                                              | Pull request       |
| Accessibility                           | axe (tests), Grit (markup)        | Runtime tree for real checks; markup patterns for the obvious misuse                                | Pull request       |
| Prose                                   | `typos`, markdownlint, mdtablefix | Documentation has its own tools                                                                     | Push               |
| Mutation score                          | StrykerJS                         | Measures tests, not code                                                                            | Nightly            |
| Performance                             | Traces, benchmarks                | Not static at all                                                                                   | Scheduled          |

_Table 1: Owners, reasons, and cadence._

## The estate's current arrangement

Two families exist today, documented in
[the source inventory](../../../docs/source-inventory.md):

- **Front-end mockups** run Biome with 46 GritQL plugins (accessibility,
  component-library misuse, state slots, banned testing patterns), Stylelint
  with `stylelint-declaration-strict-value` and a `px` ban on spacing, Semgrep
  for raw colour classes and test IDs, and custom class-list scripts. No
  Oxlint, no `df12-lints`, no animation-property rule. One repository's
  semantic CI step is commented out.
- **Simulators and the terminal** run a Hyper-derived Biome configuration with
  `noExplicitAny` off and other relaxations. One simulator runs Oxlint with a
  vendored, older copy of the `df12-lints` plugin; the other dropped Oxlint.
  The terminal has an orphaned Stylelint configuration.

No repository consumes `df12-lints` as a package. The plugin ships four rules
(`complex-conditional`, `require-module-jsdoc`, `require-public-jsdoc`,
`require-private-jsdoc`) plus curated `complexity` and `max-depth` settings,
and no presets.

## Recommended moves

1. Replace the vendored plugin copy with the pinned package
   (`github:leynos/df12-lints#vX.Y.Z`,
   `jsPlugins: ["df12-lints/oxlint-plugin"]`).
2. Add `stylelint-high-performance-animation` to the two front ends' Stylelint
   configurations as a warning.
3. Prototype `prefer-css-state` in `df12-lints` as an opt-in browser preset
   with fixtures drawn from the estate's reference mockups and the terminal's
   inline writes.
4. Either install and run Stylelint in the terminal or delete its
   configuration.
5. Re-enable the mockup's semantic CI step or delete the job; a commented-out
   gate is a false promise.

## Division with Biome's deep dive

`biome-typescript` owns Biome's configuration, rule semantics, migration from
ESLint and Prettier, CI, and hooks. This skill owns the question of whether
Biome, Oxlint, Stylelint, or Semgrep should carry a given rule, and what no
linter should carry.
