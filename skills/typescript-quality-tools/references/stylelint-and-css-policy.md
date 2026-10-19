# Stylelint and CSS policy

Stylelint owns CSS. Re-implementing CSS parsing in a JavaScript linter is
wasted effort; configuring Stylelint is not.

## The estate's token policy

```js
// tools/stylelint.config.cjs
module.exports = {
  plugins: ["stylelint-declaration-strict-value", "stylelint-high-performance-animation"],
  rules: {
    "color-no-hex": true,
    "color-named": "never",
    "scale-unlimited/declaration-strict-value": [
      ["/color/", "fill", "stroke", "background", "border-color", "outline-color"],
      { ignoreValues: ["transparent", "currentColor", "inherit"] },
    ],
    "declaration-no-important": true,
    "declaration-property-unit-disallowed-list": {
      "/^(margin|padding|gap|inset|top|right|bottom|left)/": ["px"],
    },
    "plugin/no-low-performance-animation-properties": [
      true,
      { ignoreProperties: ["color", "background-color"] },
    ],
  },
};
```

- Colour properties must be `var(--…)`, `transparent`, or `currentColor`; the
  token set is the source of truth.
- Spacing uses `rem` or tokens, never `px`.
- `!important` is banned; a need for it from script or stylesheet means the
  cascade is wrong.
- Transitions and keyframes may not animate layout-triggering properties.
  `stylelint-high-performance-animation` (2.0.0 as of 2026-10-16) flags
  `margin`, `top`, `width`, and the rest in `transition` declarations and
  `@keyframes`; `ignore: "paint-properties"` restricts it to layout-only
  properties, and `ignoreProperties` exempts named ones.

## Where the rule sits in the three rings

The animation-property rule is ring one: high confidence, few false positives,
and a direct complement to `prefer-css-state`. The CSS side says "do not
animate layout"; the JavaScript side says "do not write presentation from
script". Together they make the compositor path the default.

## Tailwind and utility classes

- Semgrep or a Grit pattern catches raw colour utilities (`text-[#ff0000]`,
  `bg-red-500` when the design system says `bg-primary`).
- A class-list length check and a near-duplicate class-list scan catch
  utility soup that should be a component.
- Stylelint still runs over the generated CSS for `!important` and tokens,
  but the utility policy is a JavaScript-side concern because the classes are
  in JSX.

## Orphaned configuration

A `.stylelintrc` with no `stylelint` in `devDependencies` and no script that
runs it enforces nothing. Either install and wire it (`make lint` and CI) or
delete it so the repository does not claim a policy it does not keep.

## Checking the policy itself

- A fixture stylesheet with one violation per rule, run in the lint test
  suite, so a configuration change that silently disables a rule fails.
- The token file is generated (Style Dictionary or similar); the strict-value
  rule reads the names the generator emits, and a renamed token fails lint
  everywhere it was used.
