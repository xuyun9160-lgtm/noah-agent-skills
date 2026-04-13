# Final Status Snapshot

## Current target shape

Noah Agent Skills 当前目标形态已收敛为两个主模块：
- `noah-stock-market`
- `noah-stock-trade`

## Market
`noah-stock-market` 当前承担：
- 股票快照 / 最新行情
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息
- 后续可扩展板块 / 成分股 / 筛选能力

## Trade
`noah-stock-trade` 当前承担：
- 账户信息
- 持仓
- 证券资产
- 证券资金流水
- 可买可卖数量
- 融资最大可买数量
- 今日未完成订单
- 今日成交
- 历史成交
- 下单费用预估
- 后续继续接订单详情 / 已完成订单 / 订单费用详情等能力

## Trade verified abilities
当前已实际联调成功：
- `account-info`
- `positions`
- `sec-asset`
- `sec-capital-flow`
- `fee-estimate`
- `stock-amount`
- `max-enable-buy-amt`
- `today-deals`
- `history-deals`
- `unfinished-orders`

## Trade open issues
当前仍待确认 / 待修复：
- `/trade/get_order_list`
- `/trade/get_finished_order_list`
- `/trade/get_order_detail`
- `/trade/get_order_fee_detail`

## Archived modules
以下模块当前已不建议作为长期独立主模块继续保留，并已移动到 `archive/`：
- `archive/noah-stock-portfolio`
- `archive/noah-stock-screener`

它们目前主要用于：
- 历史兼容
- 旧结构保留
- 后续归档前的过渡

## Next milestone
下一阶段重点：
1. 继续完善 `noah-stock-trade` 的异常接口
2. 最终确认 `market + trade` 两模块结构
3. 之后按 Futu 风格整理成可安装的 Noah Agent Skills 套件
