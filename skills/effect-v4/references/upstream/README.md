# Upstream material (verbatim)

Copied from [Effect-TS/effect](https://github.com/Effect-TS/effect) at commit
`5a67e0b3a8118dd7be709a56d6d7af4f10e9c4f3` (15 October 2026, shortly after
`effect@4.0.5`), under the MIT licence in `LICENSE`. Paths inside the copied
files were rewritten to point at this bundle; the content is otherwise
unchanged.

| Path             | What it is                                                                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LLMS.md`        | The Effect team's own guidance for coding agents, with links into `examples/`                                                                                                                                                                                                                                                   |
| `MIGRATION.md`   | Overview of v3 → v4 changes, package consolidation, stability tags                                                                                                                                                                                                                                                              |
| `migration/*.md` | Topic guides: services, cause, error handling, forking, yieldable, fiber keep-alive, layer memoization, FiberRef, runtime, scope, equality, generators, Schema (long)                                                                                                                                                           |
| `examples/`      | The curated example programs (`ai-docs/src`) the Effect team maintains for LLMs: basics, schema, services, errors, resources, running, PubSub, streams, ManagedRuntime, batching, schedules, DateTime, observability, testing, Predicate, SQL, HTTP client, HttpApi (with fixtures), GraphQL, child processes, CLI, AI, cluster |

The giant generated API diff (`migration/v3-to-v4.md`, ~17k lines) is not
copied verbatim; it is split per module in `../renames/`.

## Known discrepancies with `effect@4.0.5`

Documentation can lag the code. Where they disagree, the installed `.d.ts` and
observed behaviour win. Found while building this skill:

- `migration/schema.md` (transformOrFail): the example treats `Number.parse` as
  returning `number | undefined`; in 4.0.5 it returns `Option<number>`. See
  `../schema.md` §5 for a compiling version.
- `migration/layer-memoization.md`: the `{ local: true }` example
  (`Effect.provide(L), Effect.provide(L, { local: true })`) builds the layer
  **once**, not twice — the inner provide reuses the outer local instance. Put
  `local` on the inner provide to isolate it. See `../core.md` §3.
- `examples/01_effect/03_services/20_layer-composition.ts`: the query wraps the
  bound parameter in quotes (`WHERE id = '${id}'`), which turns the placeholder
  into a string literal. Write `WHERE id = ${id}`; see `../platform.md` (SQL).
- `migration/schema.md` (Union extends Struct): the v3 example adds
  `c: Schema.Boolean` while the v4 example adds `c: Schema.Number`. The type
  change is a documentation slip, not a migration rule.
- `migration/schema.md` (Arbitrary): the link to `packages/effect/ARBITRARY.md`
  targets a file that is not part of this bundle. The 4.0.5 module is
  `effect/Arbitrary`; `../schema.md` covers the catalogue's guidance.
