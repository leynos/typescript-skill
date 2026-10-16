# Node and Bun compatibility

Bun implements most of the Node API surface and runs TypeScript directly; it
also ships its own APIs. A project that supports both pins both in CI and keeps
runtime-specific code behind one adapter.

## Agree

- `node:fs`, `node:path`, `node:url`, `node:events`, `node:stream`,
  `node:child_process`, `node:worker_threads` for common cases.
- `fetch`, `Request`, `Response`, web streams, `AbortController`,
  `structuredClone`, `TextDecoder`.
- `package.json` `exports` and conditions; `"type": "module"`.
- `import.meta.dirname`, `import.meta.filename`, `import.meta.resolve`.

## Differ

| Area                                        | Node                                                                                              | Bun                                           | Guidance                                                           |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| Running `.ts` directly                      | Type stripping for erasable syntax; `.ts` imports need flags or `rewriteRelativeImportExtensions` | Native, including enums and decorators        | Keep source to erasable syntax (`erasableSyntaxOnly`) so both work |
| HTTP server                                 | `node:http`, frameworks on top                                                                    | `Bun.serve` (fast, web-shaped) or `node:http` | One adapter; the core takes `Request` and returns `Response`       |
| Test runner                                 | `node:test`                                                                                       | `bun test` (Jest-like API)                    | Pick one per package; do not mix in one suite                      |
| Package manager and lockfile                | npm, pnpm, yarn; `package-lock.json`                                                              | `bun install`; `bun.lock`                     | One lockfile per repository, frozen in CI                          |
| `trustedDependencies`                       | Lifecycle scripts run by default                                                                  | Lifecycle scripts blocked unless trusted      | List packages whose `prepare` must run                             |
| Native add-ons                              | N-API and legacy NAN modules                                                                      | N-API only                                    | Prefer N-API modules; test the load on both                        |
| `node:cluster`, `node:inspector`, some `vm` | Supported                                                                                         | Partial or absent                             | Avoid in shared code                                               |
| SQLite                                      | `node:sqlite` (recent)                                                                            | `bun:sqlite`                                  | One adapter behind a repository interface                          |
| Shell scripting                             | `child_process`                                                                                   | `Bun.$` template shell                        | Build scripts only; never in library code                          |
| Startup time                                | Slower                                                                                            | Faster                                        | Matters for CLIs; measure                                          |

_Table 1: Where Node and Bun diverge and how to write code that survives both._

## Patterns

- **Portable core, runtime adapters.** The core takes `Request`, returns
  `Response`, reads files through an injected interface, and never imports
  `bun:*` or `node:cluster`. Each runtime has one adapter module. A contract
  test asserts the core imports no runtime-specific module.
- **Runtime detection in one place.** `typeof Bun !== "undefined"` is fine,
  once, in the adapter selector; sprinkled through modules it is a maintenance
  cost.
- **Shebangs.** `#!/usr/bin/env node` for a `bin` that must run under Node;
  `#!/usr/bin/env bun` only when Bun is the stated requirement. A `bin` that is
  `.cjs` while the library is ESM is a deliberate compatibility decision;
  record it.
- **`engines`.** Declare the Node range; Bun reads it too. Pin exact versions
  in `packageManager` and in CI.

## Testing both

Run the suite under each runtime in CI. The cheap way is a matrix job that
installs with the declared package manager and runs the package's test script;
the expensive way is maintaining two suites. Choose the cheap way and keep
runtime-specific tests in the adapter directories, tagged so each runtime skips
the other's.
