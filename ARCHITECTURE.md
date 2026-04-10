# Architecture

## Skill identity

`noah-agent-skills` 是一个总技能，而不是单一功能脚本。

## Current implementation stage

当前仓库中的 `noah-stock-market/` 代表第一阶段已落地模块。

## Why modular design

后续仍会扩展：
- 交易
- 持仓
- 账户
- 选股
- 其他接口能力

因此当前采用“总 skill + 子模块”的方式更合理，而不是把市场模块视为最终完整形态。
