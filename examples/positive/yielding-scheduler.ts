/**
 * @file Positive fixture for a project-level scheduler abstraction over the
 * Prioritized Task Scheduling API with a timer fallback. Compiled by
 * `make examples` to evidence the browser main-thread skill.
 */
// Linked from skills/browser-main-thread-performance/SKILL.md.
//
// A project-level scheduler abstraction. Components call `scheduler.yield()`
// and `scheduler.postTask()`; the platform check lives here, once, with a
// fallback for browsers that lack the Prioritized Task Scheduling API.

export type Priority = "user-blocking" | "user-visible" | "background";

export interface Scheduler {
  /** Yield to the event loop so input and rendering can run. */
  readonly yield: () => Promise<void>;
  /** Run `task` at `priority`, honouring `signal` if it aborts first. */
  readonly postTask: <T>(
    task: () => T | Promise<T>,
    options?: { readonly priority?: Priority; readonly signal?: AbortSignal },
  ) => Promise<T>;
}

// The platform API is not Baseline, so its shape is declared here rather than
// relied on from lib.dom. Only the members this module uses are described.
interface PlatformScheduler {
  readonly yield?: () => Promise<void>;
  readonly postTask?: <T>(
    task: () => T | Promise<T>,
    options?: { readonly priority?: Priority; readonly signal?: AbortSignal },
  ) => Promise<T>;
}

function platformScheduler(): PlatformScheduler | undefined {
  const candidate: unknown = (globalThis as { scheduler?: unknown }).scheduler;
  return typeof candidate === "object" && candidate !== null
    ? (candidate as PlatformScheduler)
    : undefined;
}

const fallbackDelay: Record<Priority, number> = {
  "user-blocking": 0,
  "user-visible": 0,
  background: 50,
};

function yieldWithTimeout(delay: number): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(resolve, delay);
  });
}

// Native `postTask` rejects a queued task the moment its signal aborts. The
// fallback must do the same rather than let the timer run out first, or a
// background task would add its 50 ms delay to every cancellation.
function sleepUnlessAborted(delay: number, signal?: AbortSignal): Promise<void> {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      signal?.removeEventListener("abort", onAbort);
      resolve();
    }, delay);
    function onAbort(): void {
      clearTimeout(timer);
      reject(signal?.reason);
    }
    signal?.addEventListener("abort", onAbort, { once: true });
  });
}

async function postTaskWithTimeout<T>(
  task: () => T | Promise<T>,
  options?: { readonly priority?: Priority; readonly signal?: AbortSignal },
): Promise<T> {
  options?.signal?.throwIfAborted();
  await sleepUnlessAborted(fallbackDelay[options?.priority ?? "user-visible"], options?.signal);
  return task();
}

export function createScheduler(): Scheduler {
  const platform = platformScheduler();
  const nativeYield = platform?.yield?.bind(platform);
  const nativePostTask = platform?.postTask?.bind(platform);
  return {
    yield: nativeYield ?? (() => yieldWithTimeout(0)),
    postTask: nativePostTask ?? postTaskWithTimeout,
  };
}

export const scheduler: Scheduler = createScheduler();
