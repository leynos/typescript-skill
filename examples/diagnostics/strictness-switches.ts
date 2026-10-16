// Linked from skills/typescript-types-and-apis/SKILL.md.
//
// Each `@ts-expect-error` below documents a diagnostic that one of the sharper
// strictness switches produces. The gate compiles this file, so a marker with
// no error underneath it fails the build: the fixture proves the switch bites.

// exactOptionalPropertyTypes: an optional property may be absent, but it may
// not be set to `undefined` unless the type says so.
interface Options {
  readonly retries?: number;
}

// @ts-expect-error `undefined` is not assignable to `number` under exactOptionalPropertyTypes
export const explicitUndefined: Options = { retries: undefined };

export const absent: Options = {};

// noUncheckedIndexedAccess: an index read may miss, so the element type gains
// `| undefined` and must be narrowed before use.
export function firstLength(words: readonly string[]): number {
  // @ts-expect-error `words[0]` is `string | undefined`
  return words[0].length;
}

export function firstLengthChecked(words: readonly string[]): number {
  const [first] = words;
  return first === undefined ? 0 : first.length;
}

// noPropertyAccessFromIndexSignature: dotted access on an index signature
// looks like a typo-safe property read but is not; use bracket access.
declare const env: Record<string, string | undefined>;

// @ts-expect-error property comes from an index signature, so it must use ['HOME']
export const home = env.HOME;

export const homeChecked = env["HOME"];

// noImplicitOverride: a subclass method that shadows a base method must say so.
class Base {
  describe(): string {
    return "base";
  }
}

export class Derived extends Base {
  // @ts-expect-error missing `override` modifier
  describe(): string {
    return "derived";
  }
}
