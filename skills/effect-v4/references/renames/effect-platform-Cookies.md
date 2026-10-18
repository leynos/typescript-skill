<!-- Generated from Effect-TS/effect migration/v3-to-v4.md (MIT). Entries
marked 'Still exported in v4' upstream are omitted: those APIs keep their name.
-->
# `@effect/platform/Cookies` v3 → v4

- `Cookies.CookieTypeId` -> `Cookies.isCookie`: The cookie brand is private in
  v4; use the public refinement instead of reading the type-id symbol.
- `Cookies.CookiesError` -> `Cookies.CookiesError`: The error tag is
  CookiesError rather than CookieError. Update catchTag calls and \_tag
  comparisons; validation details are in the reason field.
- `Cookies.ErrorTypeId` -> `Cookies.CookiesError`: The error brand is private
  in v4; identify the exported error class instead.
- `Cookies.TypeId` -> `Cookies.isCookies`: The collection brand is private in
  v4; use the public refinement instead.
- `Cookies.unsafeMakeCookie` -> `Cookies.makeCookieUnsafe`: Renamed to put
  Unsafe last; it still throws on invalid cookie data.
- `Cookies.unsafeSet` -> `Cookies.setUnsafe`: Renamed to put Unsafe last; the
  dual throwing behavior is retained.
- `Cookies.unsafeSetAll` -> `Cookies.setAllUnsafe`: Renamed to put Unsafe last;
  the dual all-or-throw behavior is retained.
