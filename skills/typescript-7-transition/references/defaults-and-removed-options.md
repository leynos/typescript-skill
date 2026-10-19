# Defaults and removed options

Reviewed 2026-10-16 against the TypeScript 6.0 (2026-03-23) and 7.0
(2026-07-08) announcements.

## New defaults

| Option                         | 5.9 default               | 6.0 and 7.0 default                 | Likely effect                                                                        |
| ------------------------------ | ------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ |
| `strict`                       | `false`                   | `true`                              | Brownfield directories fail; apply the ratchet                                       |
| `module`                       | depends on `target`       | `esnext`                            | Node projects should set `nodenext` explicitly                                       |
| `target`                       | `es5`                     | latest stable (`es2025` at 6.0)     | Output changes; check downlevel assumptions                                          |
| `types`                        | every `@types/*` in scope | `[]`                                | `process`, `Buffer`, test globals vanish; set `["node"]` or `["*"]`                  |
| `rootDir`                      | inferred common root      | the `tsconfig.json` directory       | Emit layout changes; set `rootDir: "./src"`                                          |
| `noUncheckedSideEffectImports` | `false`                   | `true`                              | Side-effect imports of missing modules error                                         |
| `libReplacement`               | `true`                    | `false`                             | `@typescript/lib-*` packages ignored unless enabled                                  |
| `stableTypeOrdering`           | absent                    | `true` in 7.0, fixed; opt-in in 6.0 | Union ordering in declarations and errors changes; 6.0 opt-in costs up to 25 percent |
| `esModuleInterop`              | `false`                   | `true`, cannot be disabled          | Default imports of CJS behave consistently                                           |
| `alwaysStrict`                 | `false` unless `strict`   | `true`, cannot be disabled          | All output is strict mode                                                            |

_Table 1: Defaults that changed, and what each change does to a project._

## Removed options

TypeScript 6.0 reports each with a deprecation error that
`"ignoreDeprecations": "6.0"` silences. TypeScript 7.0 rejects each outright
with no escape hatch.

| Option                                      | Replacement                                                  |
| ------------------------------------------- | ------------------------------------------------------------ |
| `target: es5`                               | `es2015` or later; drop IE11 assumptions                     |
| `downlevelIteration`                        | Delete; targets at or above `es2015` iterate natively        |
| `moduleResolution: node` / `node10`         | `nodenext` for Node code, `bundler` for bundled code         |
| `moduleResolution: classic`                 | As above                                                     |
| `module: amd` / `umd` / `systemjs` / `none` | `esnext` or `nodenext`; let a bundler produce legacy formats |
| `baseUrl`                                   | `paths` relative to the project root, or workspace packages  |
| `outFile`                                   | A bundler                                                    |
| `esModuleInterop: false`                    | Delete; it is always on                                      |
| `allowSyntheticDefaultImports: false`       | Delete                                                       |
| `alwaysStrict: false`                       | Delete                                                       |
| `module Foo {}` namespace syntax            | `namespace Foo {}` (`declare module "x"` is unaffected)      |
| `import x from "y" asserts { … }`           | `with { … }`                                                 |
| `/// <reference no-default-lib="true"/>`    | `noLib` or an explicit `lib` list                            |
| `tsc file.ts` beside a `tsconfig.json`      | `tsc -p` or `--ignoreConfig` (TS5112)                        |

_Table 2: Options removed in 7.0 and their replacements._

## Semantic changes with no type error

- **Template literal inference** treats a code point as one unit. A utility
  type that counted UTF-16 code units through template literal recursion gives
  different results for emoji and other astral characters.
- **JavaScript files** are analysed with the `.ts` rules: a value cannot be
  used as a type (use `typeof`), `@enum` and `@class` have no special meaning,
  a bare `?` type is invalid (use `any`), postfix `!` is unsupported, type
  names need `@typedef`, Closure-style function types are gone, and `this`
  aliasing and `prototype` reassignment are not specially handled. Projects with
  `checkJs` should expect new diagnostics.
- **Parallel checking** (`--checkers`, default 4) can in rare cases surface
  order-dependent results; `--singleThreaded` is the control.

## Order of work for one project

1. Upgrade to 6.0.x. Read every TS5107-class deprecation and fix the option;
   do not add `ignoreDeprecations`.
2. Turn on `stableTypeOrdering` in 6.0 and fix any declaration or snapshot
   diffs it produces.
3. Set `types` explicitly and `rootDir` explicitly.
4. Install 7.0 beside 6.0 and run the compare script; investigate each diff.
5. Switch the gate's `tsc` to 7.0. Keep 6.0 for library consumers until they
   release against the 7.1 API.
6. Remove 6.0 when no dependency imports `typescript`.
