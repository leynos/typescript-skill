<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/sql/SqlClient` v3 → v4

- `SqlClient.SafeIntegers` -> `effect/sql/SqlClient#SafeIntegers`: Moved and
  changed from a Reference subclass to a Context.Reference value; provide it as
  a service.
- `SqlClient.SqlClient.MakeOptions`: TODO: needs guidance
- `SqlClient.TransactionConnection` ->
  `effect/sql/SqlClient#TransactionConnection`: Now a factory keyed by client
  id, not a singleton tag. Prefer the client's transactionService; the payload
  type is TransactionConnection.Service.
- `SqlClient.TypeId` -> `none`: The brand is private in v4; do not inspect or
  attach it, and obtain clients through SqlClient or SqlClient.make.
- `SqlClient.make` -> `effect/sql/SqlClient#make`: Moved; custom clients rename
  MakeOptions.reactiveMailbox to reactiveQueue and may supply
  transactionService.
