---
name: react-and-accessible-ui
description: Use for React component design and accessible user interfaces in TypeScript, including state and effect ownership, derived state, external systems, controlled APIs, transitions, expressing state through CSS, accessible interaction, localization, component testing, and framework-specific scheduling judgement.
metadata:
  globs: "**/*.tsx, **/*.jsx, **/*.css, **/*.ftl, **/locales/**"
---

# React and accessible UI

Use this when the question is inside a component tree: who owns a piece of
state, when an effect is the right tool, how a control exposes itself to
assistive technology, or how a component is tested without testing React.

## Working stance

- Derive before storing. State that can be computed from other state is a
  bug source, not a cache. Store the minimum and compute the rest during
  render, memoizing only when a measurement says so.
- Effects synchronize with external systems: a map library, a WebSocket, a
  document attribute, a subscription. An effect that only sets state in
  response to other state is a derived value in disguise.
- Every effect that starts something returns a cleanup that stops it. Stale
  results must not set state on a component that has moved on.
- Components express state; CSS presents it. A component sets `data-state`,
  ARIA attributes, or a class and lets the stylesheet decide appearance. See the
  [CSS membrane](../browser-main-thread-performance/references/css-state-membrane.md).
- Accessibility is the interaction contract, not a layer on top. A control
  that is not reachable, nameable, and operable from the keyboard is not done.
- Test behaviour through roles and names, never through test IDs or DOM
  structure. If a test needs a test ID, the control has no accessible name.

## Decision surface

- **Where state lives.** Local when one component reads and writes it; lifted
  to the nearest common ancestor when siblings share it; in a store
  (`useSyncExternalStore`, a reducer, or a state library) when it outlives the
  tree or is read by many unrelated branches. URL state for anything the user
  would expect to survive a reload or share. See
  [state-and-effect-ownership.md](references/state-and-effect-ownership.md).
- **Effects versus events.** User actions belong in event handlers. Effects are
  for subscriptions, imperative library instances, and syncing a document or
  window property. An effect with a dependency array that keeps growing is a
  sign the logic belongs in a handler or a derived value.
- **Controlled and uncontrolled.** Expose `value` and `onChange` for controlled
  use, `defaultValue` for uncontrolled, and never both silently. Document which
  mode a composite component supports.
- **Transitions and scheduling.** `startTransition` marks an update as
  interruptible so a keystroke is not blocked by an expensive re-render;
  `useDeferredValue` lets a slow consumer lag a fast input. Neither makes work
  cheaper; they reorder it. Work outside the tree (parsing, indexing) uses the
  project scheduler, not a transition. See
  [transitions-and-scheduling.md](references/transitions-and-scheduling.md).
- **Imperative surfaces.** Maps, canvases, terminals, and editors own their
  DOM. Wrap each in one component that creates the instance in an effect,
  drives it from props in further effects, and destroys it in cleanup. Nothing
  else touches that DOM.
- **Accessible interaction.** Use native elements first; a `<button>` gets
  focus, keyboard activation, and a role for free. For composite widgets, use a
  headless primitive library that implements the ARIA pattern and expose its
  `data-state`. Localize every string and every direction-sensitive style. See
  [accessible-interaction-and-i18n.md](references/accessible-interaction-and-i18n.md).
- **Testing.** Render with the real provider stack, query by role and name,
  interact with user-event, assert on what the user perceives, and run an
  accessibility checker on representative screens. See
  [component-testing.md](references/component-testing.md).

## Red flags

- `useEffect` that calls `setState` from values already in scope.
- An effect that fetches without an `AbortSignal` or a cancelled flag in its
  cleanup.
- `useMemo` or `useCallback` added without a profile showing the cost.
- `div` with `onClick` and no role, name, or keyboard handler.
- A `data-testid` in production markup, or a test that queries by class name.
- `element.style.X` written inside a component for a static value; use
  `data-state` and CSS.
- A `key` derived from an array index on a list that reorders.
- A string literal in JSX that users will read, outside the localization
  layer.
- A `requestAnimationFrame` loop inside a component with no cancellation in
  cleanup. A one-shot `requestAnimationFrame` to wait for a dialog to unmount
  is fine and is not this flag.
- Two sources of truth for one value: a prop and a copied state.

## Pairing

- Pair with `browser-main-thread-performance` when the question is frames or
  interaction latency rather than ownership.
- Pair with `typescript-data-and-state` when the state is a transition model
  the component merely renders.
- Pair with `typescript-testing` for the wider testing hierarchy; this skill
  owns component tests only.
- Pair with `typescript-quality-tools` when a rule should enforce a
  convention (no test IDs, semantic class policy, token usage).
