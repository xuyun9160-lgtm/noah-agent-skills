---
name: noah-stock-trade
description: 用于股票交易相关的订单、成交、可买可卖数量、预估费用、订单详情等场景。当用户询问下单前准备、订单状态、成交记录、订单费用、可买可卖数量、融资最大可买数量等问题时使用。当前一期先覆盖交易侧只读与交易前评估能力，不直接开放真实下单、改单、撤单。
---

# Noah Stock Trade

交易查询与交易前评估模块。当前一期先做只读能力，不直接开放交易写操作。

## Current Scope

基于当前交易 OpenAPI，一期优先覆盖以下能力：
- 获取证券可买可卖数量：`/trade/get_stock_amount`
- 查询融资最大可买数量：`/trade/max_enable_buy_amt`
- 获取当日订单列表：`/trade/get_order_list`
- 获取未完成订单列表：`/trade/get_today_order_list`
- 获取历史订单列表：`/trade/get_history_order_list`
- 获取当日成交列表：`/trade/get_today_deal_list`
- 获取历史成交列表：`/trade/get_history_deal_list`
- 获取已完成订单列表：`/trade/get_finished_order_list`
- 获取订单详情：`/trade/get_order_detail`
- 获取订单费用详情：`/trade/get_order_fee_detail`
- 查询下单预估费用：`/trade/order_fee_query`
- 查询推送数据：`/trade/query_push_data`

## Deferred Write Operations

以下写操作目前在 OpenAPI 中仍为 TEMP DISABLED，暂不纳入一期主承诺：
- 提交下单：`/trade/place_order`
- 修改订单：`/trade/modify_order`
- 撤销订单：`/trade/cancel_order`

## Installation / Prerequisites

使用前至少需要：
- Python 3
- requests
- `NOAH_API_BASE_URL`
- 交易侧 API key / 鉴权配置（后续根据真实接入方式补齐）
- 交易账户分组标识 `groupNo`（交易接口 header 必填）

## Routing Boundary

适用于：
- 可买可卖数量
- 融资最大可买数量
- 订单列表 / 历史订单
- 当日成交 / 历史成交
- 订单详情 / 订单费用
- 下单预估费用

不适用于：
- 行情数据查询（交给 market 模块）
- 持仓 / 资产 / 资金流水 / 账户概览（交给 portfolio 模块）
- 条件选股（交给 screener 模块）
- 真实下单 / 撤单 / 改单（当前一期不开放）

## Risk / Confirmation Rule

- 当前一期默认只读，不直接执行真实交易写操作
- 若未来开放下单、改单、撤单，所有写操作必须确认
- 若未明确市场、标的、数量、价格，不应代用户猜测
- 若区分实盘 / 模拟盘，必须在交易前显式确认环境

## Known Limitations

- 当前仍为文档骨架，脚本尚未正式接入这些接口
- 证券代码格式使用 `MARKET.CODE`，例如 `HK.00700`、`US.AAPL`，后续需要做统一转换
- 订单状态码体系较复杂，后续需要补统一状态映射与用户态解释
- 写操作接口当前仍处于 TEMP DISABLED 状态，不应在一期对外承诺
