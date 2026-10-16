# The CSS state membrane

JavaScript chooses semantic state; CSS decides how that state is presented. The
membrane keeps presentation decisions in one place, lets the compositor animate
without the main thread, and makes the state inspectable in the DOM.

## Signalling mechanisms, in order of preference

| Mechanism           | Use for                                                      | Example                                        |
| ------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Semantic class      | A named, enumerable state                                    | `panel--collapsed`, `is-loading`               |
| `data-*` attribute  | A state with several values, or one owned by a component lib | `data-state="open"`, `data-direction="rtl"`    |
| ARIA state          | A state that is genuinely an accessibility semantic          | `aria-expanded`, `aria-selected`, `aria-busy`  |
| CSS custom property | A dynamic scalar the stylesheet cannot know                  | `--split-position: 42%`, `--row-height: 28px`  |
| Inline style        | A documented imperative adapter only                         | Canvas sizing, measured geometry during a drag |

_Table 1: How JavaScript should signal state to CSS, most preferred first._

ARIA is for semantics, not styling convenience. `aria-expanded` on a button
that controls a region is correct and may be styled; `aria-hidden` to hide a
decorative panel because the selector was handy is not.

## Animation

- Animate `transform` and `opacity`. The compositor can run them while the
  main thread is busy, and a demonstration that blocks the main thread while a
  transform animation keeps moving is the clearest argument for the rule.
- Do not animate `top`, `left`, `width`, `height`, `margin`, or `padding`.
  Each frame triggers layout and paint on the main thread.
- For movement that changes layout, use FLIP: measure the first position,
  apply the layout change, measure the last position, apply an inverse
  transform, then animate the transform to identity. The layout cost is paid
  once; the animation is compositor-only.
- Prefer CSS transitions and `@keyframes` to JavaScript-driven animation
  loops. Use the Web Animations API when the animation must be controlled from
  script; it still runs on the compositor for the same properties.
- Honour `prefers-reduced-motion`.

## Named exceptions

The membrane is a default. These are legitimate reasons to write presentation
from JavaScript, and a lint rule must allow them:

| Exception                                   | Why                                                             | Shape                                                       |
| ------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------- |
| Measured geometry through a custom property | The stylesheet cannot know the value                            | `setProperty("--split-position", px)` on the pane element   |
| Imperative rendering surfaces               | Canvas, WebGL, a terminal emulator, a map library own their DOM | One adapter module; the library's API, not raw style writes |
| FLIP measurements                           | Reading and writing geometry is the technique                   | Measure, change, measure, transform, in one explicit block  |
| Third-party adapter code                    | The library demands inline styles                               | One adapter module, documented                              |
| One-shot interoperability fix               | Waiting for a library to unmount before navigating              | A single `requestAnimationFrame`, not a loop                |
| Temporary mockups and fixtures              | Reference HTML, test fixtures                                   | Scoped by directory; excluded from the rule                 |

_Table 2: Exceptions to the membrane and the shape each should take._

Two estate examples anchor the list. A split pane that writes its drag position
through `style.setProperty` during the drag is a geometry adapter: acceptable,
and better still when the property is a custom property (`--split-position`)
that the stylesheet consumes, rather than `left` directly. A command palette
that defers navigation with one `requestAnimationFrame` so a dialog unmounts
first is a one-shot interoperability fix, not an animation loop.

## Negative examples

- `element.style.display = "none"` to hide a panel. Toggle a class or
  `data-state` and let CSS decide.
- `element.style.transform = "scale(0.98)"` on a timer to make a button
  pulse. Use a class with a CSS transition.
- `element.style.opacity = "0"` followed by a `setTimeout` to remove the
  element. Use `transitionend` or the Web Animations API `finished` promise.
- `element.style.setProperty("background-color", …, "important")`. If
  `!important` is needed from script, the cascade is wrong; fix the stylesheet.

## Enforcement

A `prefer-css-state` rule reports direct writes of static presentation values
and recommends, in order, a semantic class, `data-state`, a custom property for
a dynamic scalar, and a documented escape hatch. It allows properties beginning
`--`, known adapter modules, explicit FLIP sections, generated files, tests,
and reference mockups, and permits a tightly scoped suppression with a reason.
It has no autofix because choosing the class name is architecture. The rule's
home is the shared lint package; route to `typescript-quality-tools`.
