---
name: noah-stock-portfolio
description: 用于股票账户、持仓、资产、盈亏、仓位分布、资金概览等查询场景。当用户询问当前持仓、资产余额、持仓盈亏、账户资金、仓位占比、组合概览、历史盈亏等问题时使用。仅用于账户与组合信息读取，不用于下单、撤单或改价。
---

# Noah Stock Portfolio

账户与持仓查询模块。用于展示资产、持仓、盈亏和仓位结构。

## Installation / Prerequisites

使用前至少需要：
- Python 3
- requests
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`
- 后续若账户接口单独鉴权，可再增加账户侧 key / profile 配置

## Routing Boundary

适用于：
- 当前持仓
- 账户资产
- 持仓盈亏
- 仓位占比
- 组合概览
- 历史盈亏 / 持仓回顾

不适用于：
- 行情快照 / K线 / 摆盘（交给 market 模块）
- 下单 / 撤单 / 交易执行（交给 trade 模块）
- 条件选股（交给 screener 模块）

## Risk / Confirmation Rule

- 当前阶段默认按只读能力设计
- 读取类查询一般无需确认
- 如果后续加入“调仓建议”“组合诊断”等能力，仍应保持只读，不自动触发交易
- 如果未来加入账户敏感操作（如资金划转），需升级为显式确认

## Known Limitations

- 当前仅为骨架，具体账户接口尚未接入
- 盈亏、持仓、资金口径需以后端接口定义为准
- 若后端区分实盘 / 模拟盘，后续需要补 profile 规则
