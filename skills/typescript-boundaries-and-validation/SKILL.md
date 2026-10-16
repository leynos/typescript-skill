---
name: typescript-boundaries-and-validation
description: Use for trust boundaries in TypeScript and JavaScript, including HTTP, JSON, environment variables, CLI arguments, storage, IPC and worker messages, plugins, native bindings, generated clients, schema validation, and where validation belongs.
metadata:
  globs: "**/*.ts, **/*.tsx, **/*.mts, **/*.cts, **/*.js, **/*.mjs, **/*.cjs, **/.env*, **/openapi*.json, **/*.graphql, **/*.proto"
---

# TypeScript boundaries and validation

Use this when data enters the program from somewhere the compiler cannot see.
Every such place is a trust boundary, and the boundary is where a value stops
being `unknown` and starts being a type the rest of the program can rely on.

## Working stance

- Name the boundary first: HTTP response, request body, JSON file, environment,
  CLI argument, `localStorage`, `postMessage`, IPC channel, plugin return
  value, native binding result, or generated client. Each has a different trust
  level and a different failure story.
- Parse, do not validate. The boundary function takes `unknown` and returns a
  typed value or an explicit failure; it does not return a boolean that the
  caller then has to honour.
- Validate once, at the edge, then trust the type. Re-validating internal calls
  is ceremony that hides where the real edge is.
- The schema is the contract. A generated type is a claim about what the
  server intends to send, not evidence of what it sent.
- Reject by default. Unknown keys, extra fields, and out-of-range values are
  failures unless the boundary is documented as lenient and the leniency is
  tested.

## Decision surface

- **Which boundaries need a schema.** Anything crossing a process, a network,
  a disk, or a privilege level. Function arguments inside typed code do not;
  `postMessage` payloads do, even when both ends are in the same repository,
  because the two ends are versioned and deployed separately. See
  [boundary-catalogue.md](references/boundary-catalogue.md).
- **Which schema library.** Choose by what the boundary needs: inference,
  transforms, JSON Schema output, bundle size, or integration with a runtime
  framework. Hand-written guards suit one or two small shapes; a library pays
  for itself at the third. See
  [schema-library-selection.md](references/schema-library-selection.md). Zod 4
  is the default for application boundaries; its deep dive is
  [`zod4-typescript`](../zod4-typescript/SKILL.md).
- **Environment and configuration.** Read `process.env` in one module, parse
  it into a typed configuration object at startup, and fail fast with every
  missing variable listed at once. Nothing else reads the environment.
- **Generated clients.** Treat generated types as transport types and the
  client as a boundary: validate responses against the schema the types were
  generated from, or accept that a server drift becomes a runtime `undefined`.
  See [generated-clients.md](references/generated-clients.md).
- **IPC and worker messages.** Validate on the receiving side, always, and on
  the sending side when the message is built from untrusted input. A typed
  channel registry (`satisfies Record<Channel, Schema>`) keeps the two in step.
- **Plugins and native bindings.** A plugin's return value and a native
  function's result are untrusted. Wrap each native call in one adapter that
  validates the result and converts errors; route the error shape to
  `typescript-errors-and-outcomes`.
- **Privilege boundaries.** Validation is necessary but not sufficient when
  the boundary also changes privilege, such as a renderer asking a main process
  to run a command. Route that to `electron-and-ipc`.

## Placement

```plaintext
untrusted input ──► parse(unknown) ──► typed transport ──► convert ──► model
                        │
                        └─► explicit failure (route to errors-and-outcomes)
```

The parse function is the only code that sees `unknown`. The converter is the
only code that sees the transport type. Everything else sees the model.

## Red flags

- `JSON.parse(text) as Foo`, `await response.json() as Foo`, or
  `event.data as Message`.
- A type predicate used as the validator for external data; predicates do not
  report what was wrong.
- `process.env.X!` or `process.env["X"] ?? "default"` scattered through
  modules.
- A schema that allows unknown keys by default on a request body.
- Generated types imported into domain code as if they were model types.
- A validation library present in `package.json` but the HTTP client bypasses
  it for "simple" responses.
- Two schemas for the same message, one on each side of a channel, that are
  not derived from a shared definition.
- A plugin host that calls into a plugin and uses the result without a shape
  check.

## Pairing

- Pair with `typescript-errors-and-outcomes` for what a failed parse returns
  and who reports it.
- Pair with `typescript-data-and-state` for the converter from transport to
  model.
- Pair with `electron-and-ipc` when the boundary is also a privilege boundary.
- Pair with `typescript-modules-and-packaging` when the schema or the generated
  client is shared across packages.
