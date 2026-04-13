---
name: noah-agent-skills
description: 综合金融股票助手技能集合。用于港股与美股相关的市场数据、账户持仓、证券资产、资金流水、订单成交、费用预估、可买可卖与交易前评估等场景。当前仓库正在收敛为两个主模块：`noah-stock-market` 和 `noah-stock-trade`。当用户询问股票价格、K线、分时、摆盘、资金流向、基础信息时使用 market；当用户询问账户信息、持仓、证券资产、资金流水、今日成交、历史成交、未完成订单、费用预估、可买可卖、最大可买数量时使用 trade。
---

# Noah Agent Skills

这是一个总技能入口，不是单一行情脚本。当前仓库正在收敛为两个主模块：
- `noah-stock-market`
- `noah-stock-trade`

## Current Module Status

### Market module
当前已实现并验证的能力：
- 快照 / 最新行情
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息

### Trade module
当前已打通或部分打通的能力：
- 账户信息
- 当前持仓
- 证券资产
- 证券资金流水
- 今日未完成订单
- 今日成交
- 历史成交
- 可买可卖数量
- 融资最大可买数量
- 下单费用预估

当前仍作为已知问题保留：
- 订单列表
- 已完成订单列表
- 订单详情
- 订单费用详情

## Installation / Usage Prerequisite

本总 skill 依赖公司内部证券 Open API。安装后按模块配置：

### Market
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`

### Trade
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

否则技能只能被识别，不能执行真实查询。

## Routing Rule

当前如果用户询问：
- 股票价格
- K线 / 分时 / 市场状态
- 资金流向
- 摆盘
- 基础信息

优先进入 `noah-stock-market`。

如果用户询问：
- 账户信息
- 当前持仓
- 证券资产
- 资金流水
- 今日成交 / 历史成交
- 未完成订单
- 下单费用预估
- 可买可卖 / 最大可买数量

优先进入 `noah-stock-trade`。

## Module Layout

当前仓库中：
- `noah-stock-market/` 为主市场模块
- `noah-stock-trade/` 为主交易与账户模块
- `archive/` 保存已归档的旧模块目录
