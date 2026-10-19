# State and effect ownership

## Where state lives

| State                                    | Home                                          | Why                                                   |
| ---------------------------------------- | --------------------------------------------- | ----------------------------------------------------- |
| Open or closed, hovered, focused         | Local `useState` or the primitive's own state | One component reads and writes it                     |
| Selected item shared by list and detail  | Nearest common ancestor                       | Siblings share it; lifting keeps one source           |
| Theme, locale, unit preference           | Context, backed by storage                    | Read everywhere, written rarely                       |
| Server data                              | A query cache                                 | Needs deduplication, staleness, retries               |
| Map viewport, editor document            | The imperative instance, mirrored on demand   | The library owns it; copying every change is wasteful |
| Current route, filters, pagination       | The URL                                       | Survives reload; shareable                            |
| Anything read by many unrelated branches | `useSyncExternalStore` or a reducer store     | Avoids prop drilling and re-render storms             |

_Table 1: Where each kind of state belongs._

## Derive, do not store

```tsx
// Stored copy: two sources of truth, one of which drifts.
const [total, setTotal] = useState(0);
useEffect(() => setTotal(items.reduce((a, i) => a + i.price, 0)), [items]);

// Derived: one source of truth, always current.
const total = items.reduce((a, i) => a + i.price, 0);
```

Memoize the derived value only when a profile shows the computation on the hot
path. `useMemo` is a cache with its own cost, not free speed.

## Effects are for external systems

```tsx
useEffect(() => {
  const map = new MapLibrary.Map({ container: ref.current });
  return () => map.remove();
}, []);

useEffect(() => {
  mapRef.current?.easeTo({ center, zoom });
}, [center, zoom]);
```

One effect creates the instance and destroys it; further effects push props
into it. The component never reads the instance's state back into React state
on every change; it subscribes to the few events the UI needs.

## Cleanup and stale results

```tsx
useEffect(() => {
  const controller = new AbortController();
  load(id, controller.signal).then(setData).catch((error: unknown) => {
    if (!isAbortError(error)) report(error);
  });
  return () => controller.abort();
}, [id]);
```

The cleanup aborts the previous request when `id` changes or the component
unmounts, so a slow response for an old `id` cannot overwrite the new one.

## Document and window properties

Setting `data-theme` on `<html>` or `dir` on `<body>` is a sync with an
external system (the document) and belongs in an effect in the provider that
owns the value. Nothing else writes those attributes.

## Signs the ownership is wrong

- A prop is copied into state "so it can be edited"; expose `value` and
  `onChange` instead, or make the component uncontrolled with `defaultValue`.
- A dependency array that keeps growing; the effect is doing work that belongs
  in an event handler or a derived value.
- `useRef` used to smuggle state past the render cycle to avoid re-renders;
  profile first, then consider `useSyncExternalStore` with a selector.
- A reducer whose actions mirror every input field; collocate form state with
  the form and reduce at submit.
