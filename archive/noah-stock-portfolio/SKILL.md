---
name: noah-stock-portfolio
description: 归档中的旧模块。原用于股票账户、持仓、资产、资金流水等查询场景。当前这些能力已逐步并入 `noah-stock-trade`，后续不再建议作为独立主模块继续使用。仅在维护历史结构或兼容旧目录时保留。
---

# Noah Stock Portfolio (Archived)

该模块已进入归档阶段。

## Current Status

原本由 `noah-stock-portfolio` 承担的能力，包括：
- 账户信息
- 当前持仓
- 证券资产
- 证券资金流水

当前已逐步并入：
- `noah-stock-trade`

## Recommended Usage

请优先改用：
- `noah-stock-trade/SKILL.md`
- `noah-stock-trade/scripts/noah_trade_cli.py`

典型替代命令：
- `python3 scripts/noah_trade_cli.py account-info`
- `python3 scripts/noah_trade_cli.py positions`
- `python3 scripts/noah_trade_cli.py sec-asset`
- `python3 scripts/noah_trade_cli.py sec-capital-flow --start-date 20260401 --end-date 20260413`

## Notes

- 当前目录保留的主要目的是兼容旧结构与历史引用。
- 后续在最终套件化与发布前，可考虑直接归档或移除该目录。
