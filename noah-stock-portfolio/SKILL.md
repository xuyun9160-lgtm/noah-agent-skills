---
name: noah-stock-portfolio
description: 用于股票账户、持仓、资产、资金流水、盈亏、仓位分布、账户概览等查询场景。当用户询问当前持仓、账户资产、证券资产、资金流水、仓位占比、组合概览等问题时使用。仅用于账户与组合信息读取，不用于下单、撤单或改价。
---

# Noah Stock Portfolio

账户与持仓查询模块。用于展示账户状态、资产、持仓、资金流水和仓位结构。

## Current Scope

基于当前交易 OpenAPI，一期优先覆盖以下只读能力：
- 获取账户信息：`/trade/get_account_info`
- 获取持仓列表：`/trade/get_positions`
- 获取证券资产：`/trade/get_sec_asset`
- 获取证券资金流水：`/trade/get_sec_capital_flow`

## Installation / Prerequisites

使用前至少需要：
- Python 3
- requests
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

当前测试口径下：
- 交易侧暂不需要单独 token
- 通过请求头中的 `groupNo` 访问交易账户分组

## Routing Boundary

适用于：
- 当前持仓
- 账户信息
- 证券资产
- 资金流水
- 仓位概览
- 组合概览

不适用于：
- 行情快照 / K线 / 摆盘（交给 market 模块）
- 下单 / 撤单 / 改单 / 订单成交查询（交给 trade 模块）
- 条件选股（交给 screener 模块）

## Risk / Confirmation Rule

- 当前阶段默认按只读能力设计
- 读取类查询一般无需确认
- 即使后续补充组合分析，也不应自动触发交易动作
- 若未来加入资金划转等敏感能力，应升级为显式确认

## Known Limitations

- 当前仍为文档骨架，脚本尚未正式接入这些接口
- 交易侧接口依赖 `groupNo` header，与 market 模块的接入前提不同
- 证券代码格式使用 `MARKET.CODE`，例如 `HK.00700`、`US.AAPL`，后续需要与 market 模块的 `HK-00700` / `US-AAPL` 统一转换
