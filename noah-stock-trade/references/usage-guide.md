# Usage Guide

## 1. What This Module Is For
`noah-stock-trade` 当前一期用于：
- 订单查询
- 成交查询
- 订单详情查询
- 订单费用查询
- 下单前费用预估
- 可买可卖数量查询
- 融资最大可买数量查询

当前一期**不用于**：
- 真实下单
- 改单
- 撤单

## 2. Access Prerequisites
当前测试口径下，需要：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

当前交易侧测试前提：
- Base URL：`https://stock-open-api.t2.test.noahgrouptest.com`
- Header：`groupNo: 100636524`

## 3. Suitable Query Scenarios
适合的场景包括：
- 看今天的订单
- 查未完成订单
- 查历史订单
- 看今天的成交
- 查历史成交
- 看某笔订单详情
- 看某笔订单费用
- 查询某只股票可买可卖数量
- 查询某只股票融资最大可买数量
- 查询某笔拟下单的预估费用

## 4. Example Query Styles
### 订单 / 成交
- `看今天的订单`
- `查未完成订单`
- `看历史成交`
- `查这笔订单详情`
- `看这笔订单费用`

### 可买可卖 / 可下单能力
- `查腾讯可买可卖数量`
- `查腾讯融资最大可买数量`
- `看腾讯下单预估费用`

## 5. Symbol Format Note
交易接口当前使用的证券代码格式是：
- `HK.00700`
- `US.AAPL`

这与 market 模块常用的：
- `HK-00700`
- `US-AAPL`

不同，后续脚本层需要做统一转换。

## 6. Order Status Note
订单查询结果中可能同时包含：
- OpenAPI 统一状态
- sec-trade 原始状态码

建议优先向最终用户展示统一状态；如需补充解释，再结合：
- `references/order-status-mapping.md`

## 7. Current Limitations
当前已知限制包括：
- 写操作接口（下单 / 改单 / 撤单）在 OpenAPI 中仍为 TEMP DISABLED
- 当前仓库中尚未正式接入 trade 脚本
- 一期先聚焦只读交易查询与交易前评估能力
- 证券代码格式仍需额外转换适配

## 8. Relationship with Other Modules
- 行情 / K线 / 分时 / 摆盘 → `noah-stock-market`
- 账户 / 持仓 / 资产 / 资金流水 → `noah-stock-portfolio`
- 条件选股 → `noah-stock-screener`
