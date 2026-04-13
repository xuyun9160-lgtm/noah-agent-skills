---
name: noah-stock-screener
description: 归档中的旧模块。原用于股票条件选股、财务筛选、技术指标筛选、形态筛选等场景。当前不再建议作为长期独立主模块保留；后续若继续建设，建议并入 `noah-stock-market` 作为市场侧筛选能力。
---

# Noah Stock Screener (Archived)

该模块当前处于归档/待合并阶段。

## Current Status

原计划能力包括：
- 条件选股
- 财务筛选
- 技术指标筛选
- 形态筛选

当前判断：
- 若后续继续建设，建议并入 `noah-stock-market`
- 不建议长期作为独立主模块保留

## Recommended Direction

优先保留的主模块为：
- `noah-stock-market`
- `noah-stock-trade`

其中选股类能力若继续建设，可视为 market 模块的扩展能力。

## Notes

- 当前目录保留的主要目的是兼容旧结构与历史引用。
- 后续在最终套件化与发布前，可考虑直接归档或移除该目录。
