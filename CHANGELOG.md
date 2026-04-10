# Changelog

## 2026-04-10

### Added
- Added top-level `README.md` for `noah-agent-skills` repository.
- Added top-level `SKILL.md`, `MODULES.md`, and `ARCHITECTURE.md` to describe the overall skill/project structure.
- Added skeleton `SKILL.md` files for planned modules:
  - `noah-stock-portfolio`
  - `noah-stock-trade`
  - `noah-stock-screener`
- Added `noah-stock-market/references/edge-cases.md`.
- Added `noah-stock-market/references/current-availability.md`.
- Added `noah-stock-market/references/install-troubleshooting.md`.
- Added `noah-stock-market/references/output-policy.md`.
- Added `noah-stock-market/references/routing-spec.md`.
- Added `noah-stock-market/references/market-examples.md`.
- Added `noah-stock-market/references/name-resolution.md`.
- Added `noah-stock-market/references/error-catalog.md`.
- Added distributable package artifacts:
  - `noah-stock-market.skill`
  - `noah-agent-skills.skill`

### Changed
- Refined installation guidance to use `NOAH_MARKET_APIKEY` as the preferred environment variable.
- Kept backward compatibility for the old `NOAH_MARKET_TOKEN` variable in code.
- Clarified that the required credential is the securities market API key, not a GitHub token.
- Updated installation and publishing docs to align with the top-level `noah-agent-skills` repository framing.
- Improved market module natural-language routing and symbol extraction.
- Added HK / US ambiguity clarification for high-frequency dual-market Chinese stock names.
- Improved user-facing clarification text to be more product-like.
- Added detail mode for:
  - capital flow
  - kline
  - intraday
- Added default detail-mode output limit of 10 records.
- Added handling for zero-value tail records in capital flow responses.
- Improved end-user response formatting to favor summary-first, product-oriented output.

### Verified
- Verified working main market paths in current environment:
  - snapshot
  - market state
  - intraday
  - kline (HK main path)
  - orderbook
  - capital flow
  - basic info
- Verified ambiguity clarification works for names such as:
  - 阿里巴巴
  - 百度
- Verified natural-language examples such as:
  - `看腾讯最近10根日K`
  - `查询阿里巴巴最近5条资金流向`
  - `看腾讯最近分时明细`

### Known Limits
- US kline still returns 404 in some current-environment scenarios.
- Some HK symbol / period combinations may also return 404 in the current environment.
- Plate and option-related capabilities remain unsupported or partially unsupported in the current environment.
- Name resolution still relies primarily on local hints rather than a formal search/matching service.

### Notes
- Current public packaging/install behavior still treats `noah-stock-market` as the installable skill module inside the broader repository layout.
- Repository structure was intentionally left unchanged for now, even though a future single-skill consolidation remains possible.
