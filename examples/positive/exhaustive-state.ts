// Linked from skills/typescript-data-and-state/SKILL.md.
//
// A discriminated state machine whose transitions are total: the `switch`
// returns from every arm and `assertNever` makes a missing arm a compile error
// instead of a silent fall-through to `undefined`.

export type Connection =
  | { readonly kind: "idle" }
  | { readonly kind: "connecting"; readonly attempt: number }
  | { readonly kind: "open"; readonly socketId: string }
  | { readonly kind: "closed"; readonly reason: string };

export type Event =
  | { readonly type: "dial" }
  | { readonly type: "opened"; readonly socketId: string }
  | { readonly type: "failed"; readonly reason: string }
  | { readonly type: "hangup" };

function assertNever(value: never): never {
  throw new Error(`unhandled case: ${JSON.stringify(value)}`);
}

export function transition(state: Connection, event: Event): Connection {
  switch (state.kind) {
    case "idle":
      return event.type === "dial" ? { kind: "connecting", attempt: 1 } : state;
    case "connecting":
      switch (event.type) {
        case "opened":
          return { kind: "open", socketId: event.socketId };
        case "failed":
          return state.attempt < 3
            ? { kind: "connecting", attempt: state.attempt + 1 }
            : { kind: "closed", reason: event.reason };
        case "hangup":
          return { kind: "closed", reason: "hung up while connecting" };
        case "dial":
          return state;
        default:
          return assertNever(event);
      }
    case "open":
      return event.type === "hangup"
        ? { kind: "closed", reason: "hung up" }
        : state;
    case "closed":
      return state;
    default:
      return assertNever(state);
  }
}
