<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/cli/HelpDoc` v3 → v4

- `HelpDoc.DescriptionList` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.Empty` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.Enumeration` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.Header` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.HelpDoc` -> `HelpDoc.HelpDoc`: The name remains, but v4 is a
  structured command-help record rather than a tagged document AST.
- `HelpDoc.Paragraph` -> `none`: The v3 document-node ADT was removed; v4 uses
  a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.Sequence` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.blocks` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.descriptionList` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.empty` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.enumeration` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.getSpan` -> `none`: The Span ADT and document-to-span conversion
  were removed; v4 help fields are strings.
- `HelpDoc.h1` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.h2` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.h3` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.isDescriptionList` -> `none`: The v3 document-node ADT was removed;
  v4 uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.isEmpty` -> `none`: The Empty variant was removed when HelpDoc
  became a structured record; inspect the relevant flags, args, subcommands,
  and examples arrays when an application-specific emptiness test is needed.
- `HelpDoc.isEnumeration` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.isHeader` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.isParagraph` -> `none`: The v3 document-node ADT was removed; v4
  uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.isSequence` -> `none`: The v3 document-node ADT was removed; v4 uses
  a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.mapDescriptionList` -> `none`: The v3 document-node ADT was removed;
  v4 uses a structured HelpDoc record rendered by CliOutput.
- `HelpDoc.orElse` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.p` -> `none`: The v3 document-node ADT was removed; v4 uses a
  structured HelpDoc record rendered by CliOutput.
- `HelpDoc.toAnsiDoc` -> `none`: CliOutput owns rendering and exposes formatted
  text rather than an AnsiDoc.
- `HelpDoc.toAnsiText` -> `CliOutput.defaultFormatter().formatHelpDoc`: Format
  the structured help record; inside Effect code prefer the CliOutput.Formatter
  service.
