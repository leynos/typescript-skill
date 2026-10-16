# Plugins and extension protocols

A plugin is code the host did not write, running with whatever access the host
gives it. Design the protocol as a boundary.

## Capabilities, not internals

```ts
export interface PluginApi {
  readonly version: 2;
  readonly commands: {
    register(name: string, handler: (input: CommandInput) => Promise<CommandOutput>): Disposable;
  };
  readonly ui: {
    addStatusItem(item: StatusItem): Disposable;
  };
  readonly storage: {
    get(key: string): Promise<unknown>;
    set(key: string, value: Json): Promise<void>;
  };
}

export interface Plugin {
  readonly name: string;
  readonly apiVersion: 2;
  activate(api: PluginApi, signal: AbortSignal): Promise<void> | void;
}
```

- The plugin receives an API object, not the host's store, emitter, window, or
  DOM.
- Every registration returns a `Disposable`, and the host disposes everything a
  plugin registered when it deactivates.
- Inputs from the plugin are validated like IPC; outputs to the plugin are
  transport types, never model objects by reference.
- An `AbortSignal` tells the plugin to stop; the host does not wait forever.

## Where plugins run

| Location                    | Access                   | Isolation                        | Use when                                 |
| --------------------------- | ------------------------ | -------------------------------- | ---------------------------------------- |
| In-process, same realm      | Everything the host has  | None                             | Trusted first-party extensions only      |
| Worker or worker thread     | Message-passing API only | Memory and event loop            | Untrusted CPU-bound extensions           |
| Separate process            | IPC API only             | Full process isolation           | Untrusted extensions needing Node access |
| Electron utility process    | IPC API only             | Process isolation within the app | Extensions that must not touch main      |
| Sandboxed iframe or webview | `postMessage` API only   | Origin isolation                 | UI extensions                            |

_Table 1: Where plugins can run and what each location implies._

An Electron application migrating away from renderer-side Node access needs a
plugin API over the bridge; the plugins that used `require` directly cannot be
preserved as they are. Treat that as a protocol design, with a compatibility
shim for the common cases and a deprecation period.

## Versioning

- The API carries a version; the plugin declares which it targets; the host
  refuses mismatches with a clear message.
- Additive changes (new methods, new optional fields) do not bump the version.
  Removals and semantic changes do.
- Keep the previous version's adapter for one release cycle when feasible.

## Failure containment

- A plugin that throws during `activate` is disabled and reported; the host
  keeps running.
- Handlers registered by a plugin run with a timeout and a `catch` that
  attributes the failure to the plugin.
- Resource use (storage size, number of registrations, timers) is bounded per
  plugin.

## Testing a plugin API

- A contract test loads a fixture plugin against the real API object and
  asserts registrations, disposal, and failure containment.
- A compile-time test asserts that the `PluginApi` type does not expose host
  internals (for example, that `keyof PluginApi` is exactly the intended set).
- The fixture plugin is published under `./testing` so third-party authors can
  run the same contract.
