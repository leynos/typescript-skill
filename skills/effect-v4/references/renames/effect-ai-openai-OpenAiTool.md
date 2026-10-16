<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/ai-openai/OpenAiTool` v3 → v4

- `OpenAiTool.WebSearch` -> `OpenAiTool.WebSearch`: Results now include action
  alongside status. Only completed is successful; other statuses produce
  failure results. Inspect isFailure before treating a result as a successful
  search. Inspect each search source by its type: URL sources have url, while
  API sources have name and no url.
- `OpenAiTool.WebSearchPreview` -> `OpenAiTool.WebSearchPreview`: Results now
  include action alongside status. Only completed is successful; other statuses
  produce failure results. Inspect isFailure before treating a result as a
  successful search. Inspect each search source by its type: URL sources have
  url, while API sources have name and no url.
