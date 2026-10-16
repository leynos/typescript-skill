# Privilege separation migration

An application that started life with `nodeIntegration: true` and
`contextIsolation: false` has renderer code that calls Node APIs, requires
native modules, and uses `@electron/remote` directly. Flipping the flags breaks
all of it at once. Migrate in layers.

## Target state

```ts
new BrowserWindow({
  webPreferences: {
    contextIsolation: true,
    nodeIntegration: false,
    sandbox: true,
    preload: path.join(import.meta.dirname, "preload.js"),
  },
});
```

No `@electron/remote`. The preload exposes a named API:

```ts
import { contextBridge, ipcRenderer } from "electron";

contextBridge.exposeInMainWorld("app", {
  shell: {
    run: (request: ShellRunRequest) => ipcRenderer.invoke("shell:run", request),
  },
  onSessionData: (listener: (chunk: SessionChunk) => void) => {
    const handler = (_: unknown, chunk: SessionChunk) => listener(chunk);
    ipcRenderer.on("session:data", handler);
    return () => ipcRenderer.off("session:data", handler);
  },
} satisfies AppBridge);
```

Each method names one channel; the renderer cannot invent new ones.

## Order of work

1. **Inventory.** Grep the renderer for `require(`, `import … from "electron"`,
   `@electron/remote`, `process.`, `node:` imports, and native module names.
   Each hit is a privilege the renderer currently has.
2. **Shared protocol.** Create a `shared/` package with channel names, request
   and response schemas, and the `AppBridge` type. No runtime imports from main
   or renderer.
3. **Main handlers.** For each inventoried capability, add an `ipcMain.handle`
   with request validation, sender checks, and an allowlist where the
   capability is dangerous (shell, file system paths, plugin install).
4. **Preload bridge.** Expose exactly the methods the protocol defines.
5. **Renderer adapter.** Replace direct Node and remote calls with calls
   through `window.app`, behind one transport module so the rest of the
   renderer never sees `window.app` directly. Validate responses.
6. **Flip one window.** Enable `contextIsolation` and disable
   `nodeIntegration` for the window whose renderer is fully migrated. Run the
   end-to-end suite.
7. **Sandbox.** Enable `sandbox: true`, which also constrains the preload to
   a subset of Node. Move anything the preload needed from Node into main.
8. **Remove `@electron/remote`.** It is the last thing to go because it is the
   easiest to lean on during migration.

## Traps

- Plugins that run in the renderer and expect Node. They need a plugin API
  over the bridge, which is a protocol design question; route to
  `arch-typescript-package-design`.
- Renderer code that reads configuration from disk. Configuration is read in
  main, validated once, and sent to the renderer as data.
- Synchronous IPC (`ipcRenderer.sendSync`) used to make the migration easier.
  It blocks the renderer; convert to `invoke`.
- `webSecurity: false` or a permissive Content Security Policy left over from
  development. Fix both before shipping the flipped window.
- The preload bundled with the renderer's bundler and picking up browser
  polyfills; build it as its own entry with a Node target.

## Evidence the migration is done

- A test that creates each window and asserts the three flags.
- A lint rule or contract test that fails when renderer code imports
  `electron`, `node:*`, or a native module.
- Fuses (`@electron/fuses`) set to disable `runAsNode` and Node CLI inspect
  arguments in the packaged build.
