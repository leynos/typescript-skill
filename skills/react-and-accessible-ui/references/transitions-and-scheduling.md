# Transitions and scheduling inside React

React owns a scheduler. It batches state updates, commits DOM changes in one
pass, and can interrupt low-priority renders when a higher-priority update
arrives. Use its tools for work inside the tree; use the project scheduler for
work outside it.

## Tools

| Tool                    | What it does                                            | Use when                                                    |
| ----------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| `startTransition`       | Marks an update as interruptible and non-urgent         | A filter or tab change triggers an expensive re-render      |
| `useTransition`         | The above plus an `isPending` flag                      | The UI should show the pending state                        |
| `useDeferredValue`      | Lets a consumer lag behind a fast-changing value        | A heavy list renders from a text input                      |
| `React.lazy` + Suspense | Defers loading a subtree until needed                   | A route or heavy component is not on the first screen       |
| `useSyncExternalStore`  | Subscribes to an external store with tearing protection | The store lives outside React (map state, a global emitter) |
| `flushSync`             | Forces a synchronous commit                             | Almost never; a measurement after a DOM write in an adapter |

_Table 1: React scheduling tools and when each applies._

Transitions reorder work; they do not reduce it. If a render is slow because a
component does too much, a transition hides the cost behind the keystroke and
still burns the frame later. Profile, then memoize or virtualize.

## What stays outside React

- Parsing a large payload, building an index, decoding an image: these are not
  renders. Chunk them with the project scheduler or offload them; route to
  `browser-main-thread-performance`.
- Frame timing samplers and visibility-aware loops: an effect creates them,
  cleanup cancels them, and the loop itself is plain `requestAnimationFrame`
  code that stops when hidden.
- Layout measurement in imperative adapters: a measure/mutate discipline in the
  adapter, not `flushSync` in the component.

## One-shot `requestAnimationFrame`

Deferring a navigation by one frame so a dialog's exit animation and unmount
complete first is a legitimate one-shot interoperability fix:

```tsx
const frame = useRef<number | null>(null);
const close = useCallback(() => {
  setOpen(false);
  frame.current = requestAnimationFrame(() => {
    frame.current = null;
    navigate(target);
  });
}, [navigate, target]);
useEffect(
  () => () => {
    if (frame.current !== null) cancelAnimationFrame(frame.current);
  },
  [],
);
```

It is not an animation loop and it does not touch style, so a lint rule that
bans every `requestAnimationFrame` in components would flag it wrongly. It
still needs the unmount cleanup: if the component unmounts before the frame
fires, an obsolete dialog action would otherwise redirect over whatever
navigation caused the unmount.

## Effects and the frame

Effects run after commit, before the browser paints in the case of
`useLayoutEffect`, and after paint for `useEffect`. Reading layout in
`useLayoutEffect` and writing in the same effect is the read-then-write
discipline applied to one component. Doing it in many components in one commit
is how layout thrashing creeps into React code; keep measurement in one adapter.
