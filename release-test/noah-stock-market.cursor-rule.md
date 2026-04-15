# Noah Stock Market

Use this rule when the user asks about HK/US stock market data, including snapshot, latest quote, K-line, intraday trend, order book, tick-by-tick trades, broker queue, market status, global market state, capital flow, trading days, IPO list, rank, and US analysis.

## Scope
- Read-only market data only
- No trading, no account, no positions, no write actions
- No investment advice

## Supported examples
- What's Tencent's current price
- Show me Tencent daily K-line for the last 10 bars
- Show Tencent intraday data
- Show Tencent's order book
- Tencent capital flow
- Show HK IPO list
- Show HK top gainers rank
- Show AAPL analyst view

## Current verified capabilities
- snapshot / latest quote
- market_state / global_state
- intraday
- ticker
- broker_queue
- kline / date-range kline
- order_book
- capital_flow
- basicinfo
- trading_days
- us_analysis
- ipo_list
- rank

## Current unsupported capability
- stock_filter (do not expose as supported in the current environment)

## Output style
- Give a short conclusion first
- Then show key numbers
- Then add a concise observation if useful
- Keep wording clear and business-facing
- Do not expose internal API URLs, tokens, scripts, or implementation details

## Protocol rule
If an OpenAPI field is defined as an enum, always use values from enum.yaml. Do not guess enum values semantically.
