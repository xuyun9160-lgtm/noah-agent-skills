---
name: noah-stock-screener
description: 用于股票筛选、条件选股、财务筛选、技术指标筛选、形态筛选等场景。当用户询问按条件找股票、按财务指标筛选、按技术形态筛选、筛选满足某类行情条件的股票时使用。不适用于交易执行、账户持仓查询或单只股票实时行情快照。
---

# Noah Stock Screener

条件选股模块。用于按行情、财务、技术指标和形态条件筛选股票。

## Installation / Prerequisites

使用前至少需要：
- Python 3
- requests
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`
- 若后端筛选接口依赖额外权限，后续需补充说明

## Routing Boundary

适用于：
- 条件选股
- 财务筛选
- 技术指标筛选
- 形态筛选
- 板块内筛选 / 市场内筛选

不适用于：
- 单只股票快照 / K线 / 市场状态（交给 market 模块）
- 交易下单（交给 trade 模块）
- 持仓与账户（交给 portfolio 模块）

## Risk / Confirmation Rule

- 默认只读，无需交易确认
- 若筛选结果过多，应做数量限制并优先摘要展示
- 不应把筛选结果直接表述成投资建议或收益承诺

## Known Limitations

- 当前仅为骨架，筛选接口尚未正式接入
- 条件字段、排序规则、分页策略以后端接口定义为准
- 若筛选结果过多，需额外设计摘要与分页输出规则
