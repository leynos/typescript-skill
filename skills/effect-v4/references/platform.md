# Platform modules: HTTP, HttpApi, CLI, processes, files, SQL, AI

All of these moved into `effect` in v4 and import from `effect/<area>`. They
carry `@stability unstable`: minor releases may break them, so pin exact
versions and read the installed `.d.ts` before relying on a detail. Platform
implementations come from `@effect/platform-node` (or `-bun`, `-browser`,
`-deno`), whose `NodeServices.layer` supplies `FileSystem`, `Path`,
`ChildProcessSpawner`, `Terminal` and friends together.

Blocks compile against `effect@4.0.5` + `@effect/platform-node@4.0.5`.

## HTTP client

```ts
import { Context, Effect, flow, Layer, Schedule, Schema } from "effect"
import { FetchHttpClient, HttpClient, HttpClientRequest, HttpClientResponse } from "effect/http"

class Todo extends Schema.Class<Todo>("Todo")({
  id: Schema.Int,
  title: Schema.String,
  completed: Schema.Boolean
}) {}

export class TodoApiError extends Schema.TaggedError<TodoApiError>()("TodoApiError", { cause: Schema.Defect() }) {}

export class TodoApi extends Context.Service<TodoApi, {
  get(id: number): Effect.Effect<Todo, TodoApiError>
  create(title: string): Effect.Effect<Todo, TodoApiError>
}>()("myapp/TodoApi") {
  static readonly layer = Layer.effect(
    TodoApi,
    Effect.gen(function*() {
      // Configure once: base URL, JSON accept header, non-2xx as errors, transient retries
      const client = (yield* HttpClient.HttpClient).pipe(
        HttpClient.mapRequest(flow(
          HttpClientRequest.prependUrl("https://jsonplaceholder.typicode.com"),
          HttpClientRequest.acceptJson
        )),
        HttpClient.filterStatusOk,
        HttpClient.retryTransient({ schedule: Schedule.exponential(100), times: 3 })
      )

      const get = Effect.fn("TodoApi.get")((id: number) =>
        client.get(`/todos/${id}`).pipe(
          Effect.flatMap(HttpClientResponse.schemaBodyJson(Todo)),
          Effect.mapError((cause) => new TodoApiError({ cause }))
        )
      )

      const create = Effect.fn("TodoApi.create")((title: string) =>
        HttpClientRequest.post("/todos").pipe(
          HttpClientRequest.bodyJsonUnsafe({ title, completed: false }),
          client.execute,
          Effect.flatMap(HttpClientResponse.schemaBodyJson(Todo)),
          Effect.mapError((cause) => new TodoApiError({ cause }))
        )
      )

      return TodoApi.of({ get, create })
    })
  ).pipe(Layer.provide(FetchHttpClient.layer)) // or NodeHttpClient.layerUndici
}
```

## Plain routes with HttpRouter

```ts
import { NodeHttpServer, NodeRuntime } from "@effect/platform-node"
import { Effect, Layer } from "effect"
import { HttpRouter, HttpServerResponse } from "effect/http"
import { createServer } from "node:http"

export const HealthRoutes = HttpRouter.use(Effect.fn(function*(router) {
  yield* router.add("GET", "/health", Effect.succeed(HttpServerResponse.text("ok")))
}))

export const Server = HttpRouter.serve(HealthRoutes).pipe(
  Layer.provide(NodeHttpServer.layer(createServer, { port: 3000 }))
)

NodeRuntime.runMain(Layer.launch(Server))
```

`HttpRouter.toWebHandler(routesLayer.pipe(Layer.provide(HttpServer.layerServices)))`
returns `{ handler, dispose }` for Fetch-style hosts (Workers, Bun.serve, Next
route handlers).

## Schema-first APIs with HttpApi

Define the contract once (shareable between server and client), implement
groups as layers, serve, and derive a typed client and OpenAPI document.

```ts
import { NodeHttpServer, NodeRuntime } from "@effect/platform-node"
import { Context, Effect, Layer, Schema } from "effect"
import { FetchHttpClient, HttpRouter } from "effect/http"
import { HttpApi, HttpApiBuilder, HttpApiClient, HttpApiEndpoint, HttpApiGroup, HttpApiScalar } from "effect/http-api"
import { createServer } from "node:http"

// ---- contract ----
class Item extends Schema.Class<Item>("Item")({ id: Schema.Int, name: Schema.String }) {}
class ItemNotFound extends Schema.TaggedError<ItemNotFound>()(
  "ItemNotFound",
  { id: Schema.Int },
  { httpApiStatus: 404 }
) {}

class ItemsGroup extends HttpApiGroup.make("items")
  .add(
    HttpApiEndpoint.get("list", "/", { success: Schema.Array(Item) }),
    HttpApiEndpoint.get("byId", "/:id", {
      params: { id: Schema.NumberFromString },
      success: Item,
      error: ItemNotFound
    }),
    HttpApiEndpoint.post("create", "/", {
      payload: Schema.Struct({ name: Schema.String }),
      success: Item
    })
  )
  .prefix("/items")
{}

export class Api extends HttpApi.make("shop").add(ItemsGroup) {}

// ---- server ----
const ItemsLive = HttpApiBuilder.group(Api, "items", Effect.fn(function*(handlers) {
  const items = new Map<number, Item>([[1, new Item({ id: 1, name: "kettle" })]])
  return handlers.handleAll({
    list: () => Effect.succeed([...items.values()]),
    byId: ({ params }) => {
      const item = items.get(params.id)
      return item ? Effect.succeed(item) : Effect.fail(new ItemNotFound({ id: params.id }))
    },
    create: ({ payload }) =>
      Effect.sync(() => {
        const item = new Item({ id: items.size + 1, name: payload.name })
        items.set(item.id, item)
        return item
      })
  })
}))

const Routes = Layer.mergeAll(
  HttpApiBuilder.layer(Api, { openapiPath: "/openapi.json" }).pipe(Layer.provide(ItemsLive)),
  HttpApiScalar.layer(Api, { path: "/docs" })
)

export const ServerLive = HttpRouter.serve(Routes).pipe(
  Layer.provide(NodeHttpServer.layer(createServer, { port: 3000 }))
)

// ---- client ----
export class ShopClient extends Context.Service<ShopClient, HttpApiClient.ForApi<typeof Api>>()("myapp/ShopClient") {
  static readonly layer = Layer.effect(ShopClient, HttpApiClient.make(Api, { baseUrl: "http://localhost:3000" })).pipe(
    Layer.provide(FetchHttpClient.layer)
  )
}

export const useClient = Effect.gen(function*() {
  const client = yield* ShopClient
  const item = yield* client.items.byId({ params: { id: 1 } })
  return item.name
})

NodeRuntime.runMain(Layer.launch(ServerLive))
```

Notes:

- Error status comes from the `httpApiStatus` annotation (third argument of
  `Schema.TaggedError`); unannotated errors map to 500.
- Endpoint options: `params`, `query`, `payload`, `headers`, `success`, `error`
  (single schema or array). `HttpApiSchema.asText`, `asNoContent`, `status(n)`,
  `HttpApiSchema.NoContent` tune encodings.
- Authentication:
  `HttpApiMiddleware.Service<Self, { provides; requires }>()(id, { security,
  error })`
  with `HttpApiSecurity.bearer|apiKey|basic`; server implementations get the
  credential and wrap the handler effect with
  `Effect.provideService(httpEffect, CurrentUser, user)`. Full worked example:
  `upstream/examples/51_http-server/`.
- Test handlers without a socket via `HttpApiTest` (see
  `upstream/examples/51_http-server/20_testing.ts`).

## CLI

```ts
import { NodeRuntime, NodeServices } from "@effect/platform-node"
import { Console, Effect, Option } from "effect"
import { Argument, Command, Flag } from "effect/cli"

const greet = Command.make(
  "greet",
  {
    name: Argument.String("name"),
    shout: Flag.Boolean("shout").pipe(Flag.withAlias("s"), Flag.withDefault(false)),
    times: Flag.Int("times").pipe(Flag.withDefault(1)),
    title: Flag.String("title").pipe(Flag.optional)
  },
  Effect.fn(function*({ name, shout, times, title }) {
    const who = Option.match(title, { onNone: () => name, onSome: (t) => `${t} ${name}` })
    for (let i = 0; i < times; i++) yield* Console.log(shout ? `HELLO ${who.toUpperCase()}` : `hello ${who}`)
  })
).pipe(Command.withDescription("Print a greeting"))

greet.pipe(
  Command.run({ version: "1.0.0" }),
  Effect.provide(NodeServices.layer),
  NodeRuntime.runMain
)
```

v3 → v4 CLI vocabulary: `Options` → `Flag` (`Options.integer` → `Flag.Int`),
`Args` → `Argument`, `CliApp`/`Command.run` → `Command.run({ version })`,
`ValidationError` → `CliError`. Subcommands: `Command.withSubcommands([...])`;
shared parent flags: `Command.withSharedFlags({...})` and
`yield* parentCommand` inside a child handler to read them.

## Files and child processes

```ts
import { NodeServices } from "@effect/platform-node"
import { Effect, FileSystem, Path, Stream, String } from "effect"
import { ChildProcess, ChildProcessSpawner } from "effect/process"

export const program = Effect.gen(function*() {
  const fs = yield* FileSystem.FileSystem
  const path = yield* Path.Path
  const target = path.join("out", "report.txt")
  yield* fs.makeDirectory("out", { recursive: true })
  yield* fs.writeFileString(target, "hello\n")
  const text = yield* fs.readFileString(target)

  const spawner = yield* ChildProcessSpawner.ChildProcessSpawner
  const version = yield* spawner.string(ChildProcess.make("node", ["--version"])).pipe(Effect.map(String.trim))
  const files = yield* spawner.lines(ChildProcess.make("git", ["ls-files"]))

  // Streaming output from a long-running process (scoped: killed on scope close)
  yield* Effect.scoped(Effect.gen(function*() {
    const handle = yield* spawner.spawn(ChildProcess.make("ls", ["-la"]))
    yield* handle.stdout.pipe(Stream.decodeText(), Stream.splitLines, Stream.runForEach(Effect.log))
  }))

  return { text, version, fileCount: files.length }
}).pipe(Effect.provide(NodeServices.layer))
```

`@effect/platform/Command` + `CommandExecutor` became `effect/process`
`ChildProcess` + `ChildProcessSpawner`.

## SQL

`SqlClient`, `SqlSchema`, `SqlModel`, `SqlError`, `Migrator` live in
`effect/sql`; `Model` (schema variants for select/insert/update/json) lives in
`effect/schema`. Drivers are separate, version-locked packages: `@effect/sql-pg`
(`PgClient.layer`,
`PgClient.layerConfig({ url: Config.Redacted("DATABASE_URL") })`),
`@effect/sql-sqlite-node`, `@effect/sql-mysql2`, `@effect/sql-pglite`, …

```ts
import { Context, Effect, Layer, Option, Schema } from "effect"
import { SqlClient, SqlError } from "effect/sql"

export class RepoError extends Schema.TaggedError<RepoError>()("RepoError", { reason: SqlError.SqlError }) {}

export class Users extends Context.Service<Users, {
  findById(id: string): Effect.Effect<Option.Option<{ readonly id: string; readonly name: string }>, RepoError>
}>()("myapp/Users") {
  // Depends on SqlClient; provide a driver layer (e.g. PgClient.layerConfig) at the edge
  static readonly layerNoDeps = Layer.effect(
    Users,
    Effect.gen(function*() {
      const sql = yield* SqlClient.SqlClient
      const findById = Effect.fn("Users.findById")(
        function*(id: string) {
          // template parameters are bound, never interpolated as text
          const rows = yield* sql<{ readonly id: string; readonly name: string }>`
            SELECT id, name FROM users WHERE id = ${id}
          `
          return Option.fromNullishOr(rows[0])
        },
        Effect.mapError((reason) => new RepoError({ reason }))
      )
      return Users.of({ findById })
    })
  )
}
```

For a full model/repository/migration example see
`upstream/examples/40_sql/10_basics.ts`.

## AI

`effect/ai` provides `LanguageModel`, `Tool`, `Toolkit`, `Chat`,
`EmbeddingModel`, `McpServer`; providers are `@effect/ai-openai`,
`@effect/ai-anthropic`, `@effect/ai-openrouter`, `@effect/ai-openai-compat`.
Read `upstream/examples/71_ai/` before writing AI code — this surface is young
and unstable.
