# Component testing

## What a component test asserts

A component test checks what a user would perceive: text, roles, names, states,
and the effects of interaction. It does not check React internals, hook call
order, or DOM structure.

```tsx
render(<SaveButton onSave={onSave} />, { wrapper: Providers });
await user.click(screen.getByRole("button", { name: "Save" }));
expect(onSave).toHaveBeenCalledOnce();
expect(screen.getByRole("status")).toHaveTextContent("Saved");
```

## Query order

1. `getByRole` with a `name` option. If this fails, the control lacks an
   accessible name; fix the component.
2. `getByLabelText` for form fields.
3. `getByText` for static content.
4. Never `getByTestId`, `querySelector`, or class names. Test IDs in
   production markup are a lint error in the estate's front ends, and the rule
   is right: a control that needs one has no name.

## Environment

- A DOM implementation (happy-dom or jsdom) under the project's test runner for
  fast component tests.
- The real provider stack (theme, locale, router, query client) through a
  `wrapper`, so tests exercise the same tree as production.
- User-event rather than `fireEvent`, so focus, keyboard, and pointer
  sequences behave as they do for a user.
- An accessibility assertion (`toHaveNoViolations`) on representative screens,
  in a suite that runs under a runner with a full DOM when the fast runner's
  DOM is not enough.

## Timers and async

- Fake timers for debounce and timeout logic; advance them explicitly.
- `findBy*` queries and `waitFor` for asynchronous appearance; never
  `setTimeout` in a test to "let things settle".
- Abort and cleanup are tested by unmounting mid-request and asserting no
  state update or error is reported.

## Imperative surfaces

A map, canvas, or terminal component is tested at its adapter boundary: mock
the library module, assert the adapter calls it with the right props, and
assert cleanup destroys the instance. Rendering the real library in a DOM
emulator is slow and proves little; render it in an end-to-end test instead.

## End-to-end

Playwright on a representative viewport, with an accessibility scan and
accessibility-tree snapshots for key screens. Run the deep suite on pull
requests and the fast smoke on every push. Flaky end-to-end tests are
quarantined with an issue, not retried into green.

## What belongs elsewhere

- Pure logic extracted from components is unit-tested without rendering;
  route to `typescript-testing`.
- A transition model that the component renders is tested as a table or a
  property; route to `typescript-data-and-state` and `typescript-verification`.
