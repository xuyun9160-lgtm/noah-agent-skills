# Noah Agent Skills

`noah-agent-skills` 是一个面向股票场景的综合金融 skill 仓库，当前正在收敛为两个主模块：

- `noah-stock-market`
- `noah-stock-trade`

其中：
- `noah-stock-market` 负责市场数据、行情、K线、分时、摆盘、资金流向等能力
- `noah-stock-trade` 负责账户、持仓、资产、资金流水、订单、成交、费用、可买可卖、交易前评估等能力

## Current Status

| Module | Description | Auth Required | Status |
|---|---|:---:|:---:|
| `noah-stock-market` | 港股 / 美股市场数据查询（快照、K线、分时、摆盘、资金流向、基础信息） | Yes | Ready |
| `noah-stock-trade` | 账户、持仓、证券资产、资金流水、订单、成交、费用、可买可卖、交易前评估 | Yes | In Progress / Partially Verified |
| `archive/noah-stock-portfolio` | 原账户、持仓、证券资产、资金流水模块 | Yes | Archived / merged into trade |
| `archive/noah-stock-screener` | 原条件选股模块 | Yes | Archived / planned to merge into market |

## What This Repository Is

这是一个股票技能仓库，用于让 OpenClaw / Agent 通过自然语言调用内部股票市场与交易能力。

当前方向不是长期维持多个松散模块，而是逐步收敛为：
- 一个市场模块
- 一个交易模块

## Current Capabilities

### Market module
当前 `noah-stock-market` 已支持：
- 股票快照 / 最新行情
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息

### Trade module
当前 `noah-stock-trade` 已打通或部分打通：
- 账户信息
- 当前持仓
- 证券资产
- 证券资金流水
- 可买可卖数量
- 融资最大可买数量
- 今日未完成订单
- 今日成交
- 历史成交
- 下单费用预估

当前仍在排查：
- `get_order_list`
- `get_finished_order_list`
- `get_order_detail`
- `get_order_fee_detail`

## Requirements

使用前至少需要：
- Python 3
- `requests`
- 公司证券行情服务访问地址
- 公司证券行情服务 API key（market）
- 交易测试环境 Base URL 与 `groupNo`（trade）

## Configuration

### Market module
安装 market 模块后必须配置：
- `NOAH_API_BASE_URL`
- `NOAH_MARKET_APIKEY`

推荐放在：

```text
<repo-or-workspace-root>/.secrets/noah-market.env
```

示例：

```bash
NOAH_API_BASE_URL=https://securities-open-api.t2.test.noahgrouptest.com
NOAH_MARKET_APIKEY=your_api_key_here
```

### Trade module
当前测试口径下，交易与账户相关能力使用：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

示例：

```bash
NOAH_TRADE_API_BASE_URL=https://stock-open-api.t2.test.noahgrouptest.com
NOAH_TRADE_GROUP_NO=100636524
```

说明：
- 当前交易侧通过请求头中的 `groupNo` 访问账户分组
- 当前测试口径下暂不需要单独 token

## Installation

请优先阅读：
- `SKILL.md`
- `MODULES.md`
- `INSTALL.md`
- `noah-stock-market/SKILL.md`
- `noah-stock-trade/SKILL.md`

建议安装后：
- market 模块先执行 smoke test，再进行自然语言查询验证
- trade 模块先确认 Base URL 与 `groupNo` 前提，再进行 CLI 联调与自然语言查询验证

## Quick Examples

示例问法：
- `看腾讯最近10根日K`
- `看腾讯资金流向`
- `看腾讯盘口`
- `查我的持仓`
- `看今天的未完成订单`
- `看历史成交`
- `查腾讯可买可卖数量`
- `估算买 100 股腾讯的费用`

## Known Limitations

当前已知限制包括：
- 板块接口在当前环境未完全开放
- 期权接口在当前环境未开放或返回 404
- `get_order_list` / `get_finished_order_list` 与文档存在不一致
- `get_order_detail` / `get_order_fee_detail` 当前测试环境返回服务端异常

更多已知边界见：
- `noah-stock-market/references/known-limitations.md`
- `noah-stock-trade/references/api-issues.md`

## Repository Structure

```text
repo-root/
  README.md
  SKILL.md
  MODULES.md
  ARCHITECTURE.md
  INSTALL.md
  noah-stock-market/
    SKILL.md
    references/
    scripts/
  noah-stock-trade/
    SKILL.md
    references/
    scripts/
  archive/
    noah-stock-portfolio/
    noah-stock-screener/
```

## Roadmap

下一阶段优先方向：
1. 继续补齐并稳定 `noah-stock-trade`
2. 将 `noah-stock-portfolio` 完全并入 `noah-stock-trade`
3. 将 `noah-stock-screener` 并入 `noah-stock-market` 或下线
4. 最终收敛为 `market + trade` 两大模块
5. 再按 Futu 风格整理成可安装的 Noah Agent Skills 套件

## Documentation Map

### Market
- `noah-stock-market/SKILL.md`
- `noah-stock-market/references/README.md`

### Trade
- `noah-stock-trade/SKILL.md`
- `noah-stock-trade/references/README.md`
- `noah-stock-trade/references/current-availability.md`
- `noah-stock-trade/references/api-issues.md`

## Notes

- 当前更成熟的是 `market` 模块；`trade` 已进入实际联调和收口阶段
- 账户 / 持仓 / 资产 / 资金流水能力已逐步并入 `trade`
- 当前阶段只承诺只读市场查询、账户查询和交易前评估能力
- 不提供投资建议
- 不应向最终用户暴露内部接口 URL、token、header 细节或脚本实现细节
