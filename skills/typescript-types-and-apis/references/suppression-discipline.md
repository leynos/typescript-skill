# Suppression discipline

A suppression is a promise to the compiler that the author knows better. Make
every promise short, specific, and findable.

## Forms, strongest first

| Form                        | Scope                        | Use                                                         |
| --------------------------- | ---------------------------- | ----------------------------------------------------------- |
| Fix the type                | None                         | Always first                                                |
| `satisfies` or `as const`   | One expression               | Checking without widening; never unsafe                     |
| Narrowing guard             | One branch                   | When a runtime check exists anyway                          |
| `as T` on a typed value     | One expression               | A downcast the author has verified; comment required        |
| `@ts-expect-error <reason>` | The next line                | A known checker gap or a deliberate negative test           |
| `!` non-null assertion      | One expression               | Avoid; a guard or `?? fail()` is clearer                    |
| `as unknown as T`           | One expression               | Boundary adapter only, in one function                      |
| `@ts-ignore`                | The next line                | Never in new code; it does not fail when the error vanishes |
| `any`                       | Everything the value touches | Never in new code                                           |

_Table 1: Suppression forms ordered from safest to most dangerous._

## Rules

- `@ts-expect-error` must carry a reason on the same line, and the reason
  names the invariant or the upstream issue. The marker fails when the error
  disappears, which is the point: it reports that the suppression is stale.
- One suppression per line, on the narrowest statement. Never at the top of
  a function or file.
- In tests, `@ts-expect-error` is an assertion: it proves the compiler rejects
  a shape. Keep those in `.test-d.ts` files or alongside the type they test,
  and route the testing question to `typescript-testing`.
- Count suppressions in CI. The count is allowed to fall; a rise needs a
  review comment that says why.
- Lint rules that ban `any` and unchecked assertions belong to the linter;
  the compiler cannot express "this `as` needs a comment". Route that to
  `typescript-quality-tools`.

## Brownfield exceptions

Legacy code with hundreds of `any` uses is not fixed by a search-and-replace to
`unknown`; that moves the error to every call site at once. Instead:

1. Turn on `noImplicitAny` for the directory and annotate what the compiler
   points at; leave explicit `any` alone for now.
2. Replace `any` on public signatures first, because they propagate.
3. Replace `any` in leaf functions last, one module at a time, with a test
   around each.

Record the starting count and the direction in the directory's `tsconfig`
comment so the ratchet is visible.
