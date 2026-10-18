#!/usr/bin/env python3
"""Scan TypeScript sources for Effect 3 (and Effect 4 pre-release) APIs that do not exist in Effect 4.

Usage:
    check_v3_patterns.py [--json] PATH [PATH ...]

Prints `file:line:col  rule  ->  replacement` for every hit and a per-rule summary.
Exit status is 1 when anything was found (handy in CI), 0 when clean.

The rules are deliberately conservative regexes, not a type checker: they find the
usual suspects quickly. `tsc --noEmit` remains the final word. Rules tagged REVIEW mark
APIs that still exist but changed meaning, so a hit needs a human look rather than a
mechanical rewrite.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    replacement: str
    review: bool = False


def r(name: str, pattern: str, replacement: str, review: bool = False) -> Rule:
    return Rule(name, re.compile(pattern), replacement, review)


MERGED_PACKAGES = r"@effect/(?:platform|rpc|cluster|cli|ai|sql|workflow|experimental|typeclass)(?:/[\w/]+)?"

RULES: list[Rule] = [
    # ---- packages and imports ----
    r("merged-package import", rf"""from\s+["']{MERGED_PACKAGES}["']""",
      "package merged into `effect`: import from effect/<area> (http, http-api, cli, sql, ai, rpc, cluster, workflow, process, …); see references/renames/_imports.md"),
    r("unstable path (beta)", r"""["']effect/unstable/""", "drop the `unstable` segment: effect/<area>"),
    r("effect/Either", r"""["']effect/Either["']|\bEither\.(?:right|left|isRight|isLeft|match|map|getOrElse)\b""",
      "Either became Result: effect/Result (Result.succeed/fail/isSuccess/isFailure/match)"),
    r("effect/FiberRef", r"""["']effect/FiberRef["']|\bFiberRef\.""", "FiberRef removed: use References.* / Context.Reference and Effect.provideService"),
    r("effect/ParseResult", r"""["']effect/ParseResult["']|\bParseResult\.""", "ParseResult removed: SchemaIssue / SchemaParser; failures are Schema.SchemaError"),
    r("effect/TestClock path", r"""["']effect/Test(?:Clock|Services|Context)["']""", "import { TestClock } from \"effect/testing\""),
    r("STM modules", r"""["']effect/(?:STM|TRef|TMap|TSet|TQueue|TPubSub|TSemaphore|TDeferred|TArray)["']|\bSTM\.""", "transactional modules are Tx*: TxRef, TxHashMap, TxQueue, …"),
    r("effect/FastCheck", r"""["']effect/FastCheck["']""", "import fast-check directly, or use effect/Arbitrary"),
    r("ServiceMap (beta)", r"\bServiceMap\.", "ServiceMap.* (beta) is Context.* in 4.0 stable"),

    # ---- services and layers ----
    r("Context.Tag", r"\bContext\.(?:Tag|GenericTag)\s*[(<]", "Context.Service<Self, Shape>()(\"id\") (class) or Context.Service<Shape>(\"id\")"),
    r("Effect.Tag", r"\bEffect\.Tag\s*\(", "Context.Service<Self, Shape>()(\"id\"); replace accessors with yield* or .use()"),
    r("Effect.Service", r"\bEffect\.Service\s*<", "Context.Service<Self>()(\"id\", { make }) + static layer = Layer.effect(this, this.make)"),
    r(".Default layer", r"\b[A-Z]\w*\.Default\b", "v3 Effect.Service default layer: define `static readonly layer` explicitly", review=True),
    r("Layer.scoped", r"\bLayer\.scoped(?:Discard)?\b", "Layer.effect / Layer.effectDiscard (scope provided automatically)"),
    r("Layer.provideSome/…", r"\bLayer\.(?:fromEffect|fromFunction|scopedContext|passthrough)\b", "see references/renames/effect-Layer.md"),
    r("Effect.runtime", r"\bEffect\.runtime\s*<", "Effect.context<R>() + Effect.runForkWith/runPromiseWith(context)"),
    r("Runtime.run*", r"\bRuntime\.run(?:Fork|Promise|Sync|Callback)\w*\b", "Effect.run*With(context); Runtime<R> was removed"),

    # ---- Effect combinators ----
    r("catchAll*", r"\b(?:Effect|Stream|Layer)\.catchAll(Cause|Defect)?\b", "catch / catchCause / catchDefect"),
    r("catchSome*", r"\b(?:Effect|Stream)\.catchSome(Cause|Defect)?\b", "catchFilter / catchCauseFilter (Filter module) or catchIf"),
    r("Effect.either", r"\b(?:Effect|Stream)\.either\b", "Effect.result / Stream.result (Result instead of Either)"),
    r("fork / forkDaemon", r"\bEffect\.(?:fork|forkDaemon|forkAll|forkWithErrorHandler)\b(?!\w)", "Effect.forkChild / forkDetach (forkAll/forkWithErrorHandler removed)"),
    r("Effect.async", r"\b(?:Effect|Stream)\.async(?:Effect|Scoped|Push)?\b", "Effect.callback / Stream.callback"),
    r("zipLeft/zipRight", r"\bEffect\.zip(?:Left|Right)\b", "Effect.tap / Effect.andThen"),
    r("tapErrorCause", r"\b(?:Effect|Stream)\.tapErrorCause\b", "tapCause"),
    r("timeoutFail/To", r"\b(?:Effect|Stream)\.timeout(?:Fail|FailCause|To)\b", "timeoutOrElse"),
    r("repeatN", r"\bEffect\.repeatN\b", "Effect.repeat({ times: n })"),
    r("fromNullable", r"\bEffect\.fromNullable\b", "Effect.fromNullishOr"),
    r("locally", r"\bEffect\.locally(?:With|Scoped|ScopedWith)?\b", "Effect.provideService(effect, References.X, value) / updateService"),
    r("orElse family", r"\bEffect\.orElse(?:Fail|Either)?\b", "Effect.catch(() => fallback) / mapError"),
    r("Effect.if/unless", r"\bEffect\.(?:if|unless|unlessEffect|whenEffect|iterate|loop)\b", "plain control flow in Effect.gen; Effect.when accepts Effect<boolean>"),
    r("makeSemaphore/Latch", r"\bEffect\.(?:unsafeM|m)ake(?:Semaphore|Latch)\b", "Semaphore.make / Latch.make (makeUnsafe)"),
    r("mapErrorCause", r"\bEffect\.mapErrorCause\b", "Effect.catchCause + Effect.failCause"),
    r("withConcurrency", r"\bEffect\.withConcurrency\b", "pass { concurrency } to all/forEach/mapEffect"),
    r("Effect.gen(this,…)", r"\bEffect\.gen\(\s*this\s*,", "Effect.gen({ self: this }, function*() {…})"),
    r("Scope.extend", r"\bScope\.extend\b", "Scope.provide"),
    r("yield non-effect", r"yield\*\s+(?:fiber|ref|deferred|someFiber|counterRef)\b", "Fiber.join / Ref.get / Deferred.await — these are no longer effects", review=True),
    r("Effect.partition", r"\bEffect\.partition\b", "tuple order is now [passes, fails] (was [failures, successes])", review=True),

    # ---- Cause ----
    r("Cause.*Exception", r"\b(?:Cause\.)?(?:NoSuchElement|Timeout|IllegalArgument|ExceededCapacity|Unknown|Runtime|Interrupted)Exception\b", "*Error (Cause.NoSuchElementError, Cause.TimeoutError, …)"),
    r("Cause tree API", r"\bCause\.(?:isFailure|isDie|isInterrupted|isInterruptedOnly|failureOption|failureOrCause|dieOption|failures|defects|sequential|parallel|isEmptyType|isFailType|isDieType|isSequentialType|isParallelType)\b",
      "flat Cause: hasFails/hasDies/hasInterrupts, findErrorOption/findDefect, cause.reasons, Cause.combine"),

    # ---- Schema ----
    r("Schema variadic Union/Tuple", r"\bSchema\.(?:Union|Tuple|TemplateLiteral)\(\s*(?!\[)[A-Za-z_]", "Schema.Union([A, B]) / Tuple([A, B]) — array argument"),
    r("Schema.Literal many", r"\bSchema\.Literal\(\s*(?:\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'|[^,\"'()\n]+?)\s*,", "Schema.Literals([\"a\", \"b\"])"),
    r("Schema.Literal(null)", r"\bSchema\.Literal\(\s*null\s*\)", "Schema.Null"),
    r("Schema decode names", r"\bSchema\.(?:decodeUnknown|decode|encodeUnknown|encode|validate\w*)(?=\s*\()(?!\s*\(\s*\{)|\bSchema\.(?:decode|encode)(?:Unknown)?Either\b",
      "decodeUnknownEffect / decodeEffect / encodeEffect / *Exit; validate* removed"),
    r("Schema.transform*", r"\bSchema\.(?:transform|transformOrFail|transformLiteral|transformLiterals|compose)\b",
      "from.pipe(Schema.decodeTo(to, SchemaTransformation.transform({ decode, encode }))) / SchemaGetter.transformEffect"),
    r("Schema.filter", r"\bSchema\.filter(?:Effect)?\b", "schema.check(Schema.makeFilter(p)) or Schema.refine(refinement)"),
    r("Schema v3 filters", r"\bSchema\.(?:pattern|int|positive|negative|nonNegative|nonPositive|minLength|maxLength|length|between|greaterThan|lessThan|greaterThanOrEqualTo|lessThanOrEqualTo|multipleOf|finite|nonEmptyString)\s*\(",
      "Schema.check(Schema.isPattern/isInt/isMinLength/isBetween/isGreaterThan/…) — positive/negative removed"),
    r("Schema.optionalWith", r"\bSchema\.(?:optionalWith|optionalToOptional|optionalToRequired|requiredToOptional|propertySignature|fromKey|rename)\b",
      "optionalKey / withDecodingDefault* / decodeTo + SchemaGetter.transformOptional (see references/schema.md §5)"),
    r("Schema.*FromSelf", r"\bSchema\.\w+FromSelf\b", "drop the FromSelf suffix (DateFromSelf → Date, OptionFromSelf → Option, …)"),
    r("Schema.Record({…})", r"\bSchema\.Record\(\s*\{", "Schema.Record(key, value)"),
    r("Schema.parseJson", r"\bSchema\.parseJson\b", "Schema.fromJsonString(schema) (parseJson() → fromJsonString(Schema.Unknown))"),
    r("Schema misc renames", r"\bSchema\.(?:annotations|asSchema|encodedSchema|typeSchema|keyof|pick|omit|partial|partialWith|required|extend|Data|TaggedRequest|pluck|attachPropertySignature)\b(?=\s*[(<])",
      "annotate / revealCodec / toEncoded / toType / mapFields(Struct.pick|omit|map|assign) — see references/renames/effect-Schema.md"),
    r("Schema.Date meaning", r"\bSchema\.Date\b(?!\w)", "v4 Schema.Date decodes a Date value; for ISO strings use Schema.DateFromString", review=True),
    r(".annotations(…)", r"(?<!OpenApi)\.annotations\(\s*\{", "Schema: .annotate({ … }) (OpenApi.annotations is still valid)", review=True),

    # ---- Stream / Chunk ----
    r("Stream chunk APIs", r"\bStream\.(?:mapChunks\w*|flattenChunks|fromChunk\w*|runForEachChunk\w*|mapConcat\w*|repeatEffect\w*|repeatValue|runScoped|run\w+Scoped|zipAll\w*|unfoldChunk\w*|paginateChunk\w*|paginateEffect|unfoldEffect)\b",
      "Chunk → Array renames (mapArray, flattenArray, fromArray, runForEachArray, fromEffectRepeat, …); see references/renames/effect-Stream.md"),
    r("Chunk from runCollect", r"Chunk\.(?:toReadonlyArray|toArray)\(", "Stream.runCollect already returns an Array in v4", review=True),

    # ---- testing / cli ----
    r("it.scoped", r"\bit\.(?:scoped|scopedLive)\b", "it.effect / it.live (every test is scoped)"),
    r("CLI v3 names", r"\b(?:Options|Args)\.(?:text|integer|boolean|choice|file|directory|optional|withDefault|withAlias)\b", "effect/cli Flag.* / Argument.* (Flag.String, Flag.Int, Flag.Boolean, …)"),
]


def iter_files(paths: list[pathlib.Path]):
    for root in paths:
        if root.is_file():
            yield root
            continue
        for path in root.rglob("*"):
            if path.suffix not in {".ts", ".tsx", ".mts", ".cts"} or path.name.endswith(".d.ts"):
                continue
            if any(part in {"node_modules", "dist", "build", ".git"} for part in path.parts):
                continue
            yield path


def strip_comments(line: str, in_block: bool) -> tuple[str, bool]:
    out, i = [], 0
    while i < len(line):
        if in_block:
            end = line.find("*/", i)
            if end == -1:
                return "".join(out), True
            i, in_block = end + 2, False
        elif line.startswith("/*", i):
            in_block = True
            i += 2
        elif line.startswith("//", i):
            break
        else:
            out.append(line[i])
            i += 1
    return "".join(out), in_block


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=pathlib.Path)
    parser.add_argument("--json", action="store_true", help="emit machine-readable findings")
    args = parser.parse_args()

    findings = []
    for path in iter_files(args.paths):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        in_block = False
        for lineno, raw in enumerate(lines, 1):
            code, in_block = strip_comments(raw, in_block)
            for rule in RULES:
                for m in rule.pattern.finditer(code):
                    findings.append({
                        "file": str(path), "line": lineno, "col": m.start() + 1,
                        "rule": rule.name, "match": m.group(0).strip(),
                        "replacement": rule.replacement, "review": rule.review,
                    })

    if args.json:
        json.dump(findings, sys.stdout, indent=2)
        print()
    else:
        for f in findings:
            tag = "REVIEW" if f["review"] else "FIX   "
            print(f"{f['file']}:{f['line']}:{f['col']}  {tag} {f['rule']}: `{f['match']}`\n    -> {f['replacement']}")
        counts: dict[str, int] = {}
        for f in findings:
            counts[f["rule"]] = counts.get(f["rule"], 0) + 1
        if counts:
            print("\nSummary:")
            for name, n in sorted(counts.items(), key=lambda kv: -kv[1]):
                print(f"  {n:5d}  {name}")
        else:
            print("No Effect 3 patterns found.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
