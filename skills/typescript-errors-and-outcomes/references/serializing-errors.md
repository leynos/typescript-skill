# Serializing errors

`JSON.stringify(new Error("x"))` is `{}`. `structuredClone` carries `name`,
`message`, `cause` (since recent runtimes), and `stack`, but not subclass
identity or custom fields. Any error that crosses a worker, IPC, HTTP, or
storage boundary needs an explicit wire shape.

## Wire shape

```ts
export interface ErrorDto {
  readonly name: string;
  readonly code: string;
  readonly message: string;
  readonly data?: Record<string, unknown>;
  readonly cause?: ErrorDto;
}

export function toErrorDto(error: unknown, depth = 0): ErrorDto {
  const classified = classify(error);
  return {
    name: classified.name,
    code: classified.code,
    message: classified.message,
    data: classified.data,
    cause:
      depth < 4 && classified.cause !== undefined
        ? toErrorDto(classified.cause, depth + 1)
        : undefined,
  };
}

export function fromErrorDto(dto: ErrorDto): AppError {
  return new AppError(dto.code as AppErrorCode, dto.message, {
    cause: dto.cause === undefined ? undefined : fromErrorDto(dto.cause),
    data: dto.data,
  });
}
```

Bound the cause chain. Validate `ErrorDto` on receipt like any other message; a
peer can send anything.

## What not to send

- Stack traces to a browser, a plugin, or any peer that is not a trusted log
  sink. They leak paths and versions.
- Raw `data` from an internal error to an HTTP client. Map internal codes to
  public codes at the HTTP boundary.
- `instanceof` expectations. The receiving side re-wraps; it does not expect
  the class to arrive.

## Realms and workers

`instanceof Error` is false for an error created in another realm (an iframe,
some worker setups, `vm` contexts). Check `name` and shape instead, or re-wrap
on receipt as above. The same applies to `DOMException` subclasses such as
`AbortError`: test `error.name === "AbortError"`.

## HTTP

Map to a problem-details body (`type`, `title`, `status`, `detail`, `instance`,
plus a `code` extension). Status comes from the code, not from the class. Log
the full chain server-side once; send the public subset.
