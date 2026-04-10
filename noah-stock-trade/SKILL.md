---
name: noah-stock-trade
description: 用于股票交易执行场景。当用户询问买入、卖出、下单、撤单、改单、订单状态、委托查询、条件单等问题时使用。适用于股票交易执行与订单管理，不适用于行情数据查询、持仓概览或条件选股。
---

# Noah Stock Trade

交易执行模块。用于下单、撤单、改单和订单状态管理。

## Installation / Prerequisites

使用前至少需要：
- Python 3
- requests
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`
- 后续交易接口如单独鉴权，需补充交易侧 API key / 账户配置

## Routing Boundary

适用于：
- 买入 / 卖出
- 下单 / 撤单 / 改单
- 委托状态
- 条件单 / 计划单（如后端支持）

不适用于：
- 行情数据查询（交给 market 模块）
- 持仓与账户概览（交给 portfolio 模块）
- 条件选股（交给 screener 模块）

## Risk / Confirmation Rule

- 所有写操作默认必须确认
- 高风险交易（市价单、大额单、批量单）建议二次确认
- 若未明确市场、标的、价格、数量，不应代用户猜测
- 若后端区分实盘 / 模拟盘，必须显式确认当前环境

## Known Limitations

- 当前仅为骨架，交易接口尚未接入
- 确认链路、账户环境、风控规则后续需要单独细化
- 高风险写操作的最终规则需以后端交易能力和业务要求为准
