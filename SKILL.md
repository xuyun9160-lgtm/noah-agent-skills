---
name: noah-agent-skills
description: 综合金融股票助手技能。用于港股与美股相关的市场数据查询，并为后续交易、持仓、账户、选股等能力预留统一入口。当前一期重点支持市场查询，包括个股快照、市场状态、分时、K线、摆盘、资金流向与基础信息。安装后必须配置公司证券行情服务的 API 访问参数才能执行真实查询。
---

# Noah Agent Skills

这是一个总技能入口，不是单一行情脚本。当前已落地的是 **market 模块**，后续可继续扩展：
- trade
- portfolio
- screener
- 其他金融接口能力

## Current Module Status

### Market module (current)
当前已实现并验证的能力：
- 快照 / 最新行情
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息

### Future modules (planned)
后续可逐步加入：
- 交易执行
- 账户 / 持仓 / 盈亏
- 条件选股
- 组合分析

## Installation / Usage Prerequisite

本总 skill 依赖公司内部证券 Open API。安装后必须配置：
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`

否则技能只能被识别，不能执行真实查询。

## Routing Rule

当前如果用户询问：
- 股票价格
- K线 / 分时 / 市场状态
- 资金流向
- 摆盘
- 基础信息

优先进入当前 market 模块处理。

## Module Layout

当前仓库中：
- `noah-stock-market/` 为已实现的市场查询模块

后续如继续扩展，可保持模块化设计。
