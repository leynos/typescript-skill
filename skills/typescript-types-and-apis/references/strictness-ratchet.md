# Strictness ratchet

A ratchet moves one direction. The goal is a repository whose strictest
configuration is the one the gate runs, and whose relaxations are per
directory, named, and shrinking.

## Switch order for a brownfield directory

Enable in this order. Each row says what the switch typically rejects and the
usual fix. Fix rather than suppress where the fix is mechanical; suppress with
a reason where the fix needs a design change, and track the count.

| Switch                               | Typical rejection                              | Usual fix                                                                 |
| ------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------- |
| `noImplicitAny`                      | Untyped parameters and callbacks               | Annotate; derive callback types from the library                          |
| `useUnknownInCatchVariables`         | `error.message` on an `any` catch variable     | Classify with a guard before reading fields                               |
| `strictNullChecks`                   | Fields read without checking for `undefined`   | Narrow; model absence explicitly                                          |
| `strictPropertyInitialization`       | Class fields assigned outside the constructor  | Initialize in the constructor, or make the field optional                 |
| `strictFunctionTypes`                | Callbacks typed with a wider parameter         | Narrow the parameter; use a method signature where bivariance is intended |
| `strictBindCallApply`                | `fn.call(this, wrongArgs)`                     | Fix the argument list; the error points at the call site                  |
| `noImplicitThis`                     | `this` inside a plain function                 | Annotate `this`, or use an arrow function                                 |
| `alwaysStrict`                       | Sloppy-mode code such as octal literals        | Fix the construct; the emitted `"use strict"` is harmless                 |
| `strictBuiltinIteratorReturn`        | Reading `.value` after `done` without a check  | Check `done` before using `value`                                         |
| `noImplicitOverride`                 | Subclass methods that shadow a base method     | Add `override`; delete accidental shadows                                 |
| `noFallthroughCasesInSwitch`         | Case arms that fall through                    | Add `break` or `return`; make intent explicit                             |
| `noUncheckedIndexedAccess`           | `array[0].field`, `record[key].field`          | Destructure or check; use `.at()` and narrow                              |
| `noPropertyAccessFromIndexSignature` | `env.HOME`, `headers.accept`                   | Use bracket access; it marks the read as possibly missing                 |
| `exactOptionalPropertyTypes`         | `{ retries: undefined }` for an optional field | Omit the key, or widen the type to `number \| undefined`                  |
| `verbatimModuleSyntax`               | Type-only imports without `import type`        | Add `type`; the fix is mechanical and the linter can do it                |
| `isolatedModules`                    | Re-exported types without `export type`        | Add `type`; required for single-file transpilers                          |
| `strict`                             | Nothing new once the family above passes       | Enable once the directory passes every member individually                |

_Table 1: The order in which to enable switches, what breaks, and the fix._

`strict` goes last on purpose: it turns on `strictNullChecks` and the rest of
the family at once, so enabling it first would defeat the one-switch-at-a-time
migration. Every member of the family has its own row above, so the final
switch should reject nothing new; if it does, a member was skipped.
`exactOptionalPropertyTypes` goes late because it changes the meaning of every
optional property in the directory. Expect it to surface genuine bugs where
code set a field to `undefined` to "clear" it and other code checked `in`.

## Layout

```plaintext
tsconfig.base.json        strict, every switch on, no include
tsconfig.json             extends base; references the per-directory configs
src/app/tsconfig.json     extends base; include src/app; no relaxations
src/legacy/tsconfig.json  extends base; include src/legacy; relaxations with
                          a comment per switch naming the issue that tracks it
```

The repository gate runs `tsc --build` over the root, so every directory is
checked with its own posture. A separate `tsconfig.typecheck.json` that relaxes
everything to make `--noEmit` pass is the anti-pattern: it means the gate
proves less than the editor shows, and nobody notices because the editor opens
the strict configuration.

## Measuring progress

- Count suppressions with a grep in CI and fail when the count rises:
  `@ts-expect-error`, `@ts-ignore`, `as any`, `: any`, and `!.` are the usual
  set.
- Record the per-directory relaxation list in the configuration file itself,
  one comment per switch, so a reviewer sees it where it applies.
- When a legacy directory's relaxation list is empty, delete its configuration
  and let it extend the base directly.

## When not to ratchet

- Vendored or generated code is excluded, not relaxed. Point `exclude` at it
  and keep its generator honest instead.
- Third-party declaration files are not fixed by local strictness; use
  `skipLibCheck` deliberately and document which packages motivate it.
- A directory scheduled for deletion is not worth migrating; mark it and move
  on.
