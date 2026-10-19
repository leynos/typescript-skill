# Dependency direction and layering

## Layers

For screen readers: the diagram shows four layers with arrows pointing inward
from composition to adapters to ports to core.

```plaintext
composition  ──►  adapters  ──►  ports  ──►  core
(entry point)     (HTTP, DB,     (interfaces   (pure logic,
                   Electron       the core      model types,
                   main, Bun)     needs)        transitions)
```

_Figure 1: Dependencies point inward; the core imports nothing
runtime-specific._

- **Core** has no imports from `node:*`, `bun:*`, `electron`, a database
  driver, or a framework. It imports its own model types and port interfaces.
- **Ports** are interfaces: `Clock`, `Storage`, `Transport`, `Logger`. The core
  depends on them; adapters implement them.
- **Adapters** implement ports with a runtime. One adapter per runtime or
  backend.
- **Composition** wires adapters into the core at the entry point. It is the
  only layer allowed to know about every other layer.

## Enforcing direction

A diagram enforces nothing. Use one of:

- A boundary check script that parses imports with the TypeScript API or a
  lightweight parser and fails on an edge against the direction, with an
  allowlist for the handful of justified exceptions, each with a comment.
- A lint rule (`import/no-restricted-paths` style, or a custom rule in the
  shared lint package) with the same allowlist.
- Separate packages in a workspace, so the core's `package.json` simply has no
  dependency on the adapters and the compiler cannot resolve the import.

The third is the strongest and the most work. Start with the first, graduate to
the third when the layers stabilize.

## Where things go

| Thing                             | Layer                                     |
| --------------------------------- | ----------------------------------------- |
| State machine transition function | Core                                      |
| Zod schema for a wire message     | Ports (shared protocol package)           |
| `ipcMain.handle` registration     | Adapter                                   |
| `fetch` call to a remote API      | Adapter                                   |
| Retry policy as pure data         | Core                                      |
| Retry loop that sleeps            | Adapter (uses a `Clock` port)             |
| Environment parsing               | Composition                               |
| Logger implementation             | Adapter                                   |
| Test double for a port            | `./testing` subpath of the port's package |

_Table 1: Where common pieces belong in the layering._

## Shared protocol packages

A `shared` package in an Electron application or a client-server pair holds
channel names, schemas, derived types, and constants. Rules:

- No runtime imports from main, renderer, server, or client.
- No side effects on import; a schema module that registers something on load
  breaks tree-shaking and ordering.
- Versioned with the protocol, and the version is exported.
- Tested on its own: schemas parse their examples, and a compile-time test
  asserts that invalid shapes are rejected.

## Signs the direction is wrong

- The core has a `switch` on `process.platform` or `typeof window`.
- An adapter imports another adapter.
- Composition logic (reading configuration, choosing adapters) appears in a
  handler.
- A test for the core needs a database or a window.
