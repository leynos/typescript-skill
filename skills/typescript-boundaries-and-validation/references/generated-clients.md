# Generated clients and contracts

Types generated from OpenAPI, GraphQL, protobuf, or a JSON Schema describe what
the schema author intended. They say nothing about what the running server
sends today. Treat the generated client as a boundary.

## Three postures

| Posture                 | What happens on drift                               | Cost                             | Choose when                                             |
| ----------------------- | --------------------------------------------------- | -------------------------------- | ------------------------------------------------------- |
| Trust the types         | Runtime `undefined` far from the call               | None                             | Never for a remote deployed separately                  |
| Validate against schema | Parse failure at the call, named field              | A runtime validator per response | Default for remote services                             |
| Contract test           | CI fails when the recorded or live response changes | A test suite and fixtures        | When the team owns the server and it deploys separately |

_Table 2: Postures towards generated client types and their drift behaviour._

Validate against the schema that generated the types, so the two cannot
disagree. Tools that emit both a type and a runtime validator from one schema
(OpenAPI to Zod, GraphQL codegen with validation plugins, protobuf runtimes)
are preferable to a type generator plus a hand-maintained schema.

## Ownership of generated code

- The generator's input (the schema) is tracked and reviewed.
- The generator's output is either tracked and never hand-edited, or ignored
  and regenerated in the build. Not both: a file that is ignored in
  `.gitignore` yet present in the index is the worst of each.
- Regeneration is a `make` or package script that CI runs and then checks
  `git diff --exit-code`, so stale output fails the build.
- The output directory is excluded from lint and from the strictness ratchet;
  fix the generator, not the output.

Route the build wiring to `typescript-modules-and-packaging`.

## Versioning a shared protocol

When a protocol is shared across packages or processes (IPC commands, worker
messages, a plugin API), the schema module is the protocol:

```ts
export const Commands = {
  "shell:run": z.object({ command: z.string().min(1), cwd: z.string() }),
  "config:read": z.object({}),
} satisfies Record<string, z.ZodType>;

export type CommandName = keyof typeof Commands;
export type CommandInput<C extends CommandName> = z.input<(typeof Commands)[C]>;
```

Both ends import `Commands`. Adding a command is one edit; removing one fails
every caller at compile time; changing a shape fails the receiver at runtime
with a named issue. Add a protocol version field once the two ends can be
deployed at different times.
