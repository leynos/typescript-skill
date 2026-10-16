# Accessible interaction and localization

## Native first

| Need              | Reach for                                            | Not                                |
| ----------------- | ---------------------------------------------------- | ---------------------------------- |
| Trigger an action | `<button type="button">`                             | `<div onClick>`                    |
| Navigate          | `<a href>`                                           | `<span onClick>` with `navigate()` |
| Choose one of few | `<input type="radio">` group with a `fieldset`       | Styled `div`s                      |
| Toggle            | `<input type="checkbox">` or `<button aria-pressed>` | A `div` that changes colour        |
| Show a region     | `<details>`/`<summary>` or a disclosure pattern      | Visibility toggled by class alone  |
| Dialog            | `<dialog>` or a headless dialog primitive            | A positioned `div`                 |

_Table 1: Native or primitive-library elements for common interactions._

Native elements bring focusability, keyboard handling, a role, and a name for
free. A styled `div` has to earn each of those by hand and usually misses one.

## Composite widgets

Tabs, menus, comboboxes, listboxes, and trees have ARIA patterns with specific
keyboard contracts. Use a headless primitive library that implements the
pattern and exposes state through `data-state`, `aria-selected`,
`aria-expanded`, and `aria-current`. Style those attributes; do not duplicate
the state into class names.

## Names and descriptions

- Every control has an accessible name: visible text, `aria-labelledby`, or
  `aria-label` as a last resort. Icon-only buttons need `aria-label`.
- Error messages are linked with `aria-describedby` and announced with
  `aria-live` or `role="alert"` where appropriate.
- Decorative images get `alt=""`; informative images get a real description.

## Keyboard

- Tab order follows reading order; do not fight it with `tabindex` greater
  than zero.
- Focus moves into a dialog on open and returns to the trigger on close.
- Escape closes transient surfaces; arrow keys move within composites.
- Focus is visible. Removing the outline without a replacement is a defect.

## Localization

- Every user-facing string goes through the localization layer. A string
  literal in JSX that a user reads is a defect a lint rule can catch.
- Plurals, genders, and ordinals use the message format (Fluent, ICU), not
  string concatenation.
- Direction is a document property (`dir` on `<html>` or `<body>`, or
  `data-direction`) set by the locale provider; styles use logical properties
  (`margin-inline-start`, `inset-inline-end`) so they flip with it.
- Dates, numbers, and units format through `Intl` with the active locale.
- Pseudo-localization in development catches truncation and concatenation.

## Checking

- An accessibility checker (axe) runs on representative screens in component
  tests and in end-to-end tests. Exclude only elements with a stated reason (a
  WebGL canvas, for instance).
- Colour contrast is checked against the token palette, not per screen.
- A manual keyboard pass is part of review for any new composite widget.
