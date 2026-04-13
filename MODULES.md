# Noah Agent Skills Modules

## Current modules

### noah-stock-market
当前主市场模块。

能力范围：
- 港股快照
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息
- 后续可继续承接板块 / 成分股 / 条件选股等市场侧能力

### noah-stock-trade
当前主交易与账户模块。

能力范围：
- 账户信息
- 持仓
- 证券资产
- 证券资金流水
- 可买可卖数量
- 融资最大可买数量
- 今日未完成订单
- 今日成交
- 历史成交
- 订单费用预估
- 后续继续承接订单详情、已完成订单、订单费用详情等交易侧能力

## Modules being merged / retired

### archive/noah-stock-portfolio
原账户、持仓、资产、资金流水模块。

当前状态：
- 能力已转入 `noah-stock-trade`
- 目录已移入 `archive/`
- 后续可在最终发布前彻底移除

### archive/noah-stock-screener
原条件选股模块。

当前状态：
- 当前不再作为长期主模块保留
- 目录已移入 `archive/`
- 后续若继续建设，建议并入 `noah-stock-market`

## Design principle

`noah-agent-skills` 的目标形态是收敛为两个主模块：
- `noah-stock-market`
- `noah-stock-trade`

也就是：
- 市场相关问题 → market
- 账户 / 持仓 / 订单 / 成交 / 费用 / 交易前评估 → trade

这样更符合用户心智，也更利于 OpenClaw 的技能路由与后续套件化发布。
