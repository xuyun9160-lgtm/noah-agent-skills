Noah Stock Market is a read-only HK/US market data skill.

Use it for:
- stock snapshot / latest quote
- K-line / date-range K-line
- intraday trend
- order book
- tick-by-tick trades
- broker queue
- market state / global market state
- capital flow
- trading days
- basic stock information
- IPO list
- rank
- US analysis

Do not use it for:
- placing orders
- canceling / modifying orders
- account / positions / funds queries
- investment advice

Behavior rules:
- Prefer structured summaries over raw dumps
- If the user asks for detail, show more records, but stay concise
- If a stock name is ambiguous across HK/US, ask for clarification instead of guessing
- If a capability is unsupported in the current environment, say so directly
- Do not expose internal API paths, tokens, URLs, scripts, or implementation details
- If a parameter is defined by enum, always follow enum.yaml values and never guess

Current verified capabilities:
- snapshot
- market_state
- global_state
- intraday
- ticker
- broker_queue
- kline
- order_book
- capital_flow
- basicinfo
- trading_days
- us_analysis
- ipo_list
- rank

Current unsupported capability:
- stock_filter
