# Noah Agent Skills

`noah-agent-skills` 是一个面向股票场景的综合金融 skill 仓库，当前已落地的第一阶段模块为 `noah-stock-market`。

它用于港股 / 美股的只读市场数据查询，并为后续交易、持仓、账户、选股等能力预留统一扩展入口。

## Current Status

| Module | Description | Auth Required | Status |
|---|---|:---:|:---:|
| `noah-stock-market` | 港股 / 美股市场数据查询（快照、K线、分时、摆盘、资金流向、基础信息） | Yes | Ready |
| `noah-stock-portfolio` | 持仓、资产、盈亏、仓位分布 | Yes | Planned |
| `noah-stock-trade` | 买入、卖出、下单、撤单、改单 | Yes | Planned |
| `noah-stock-screener` | 条件选股、财务筛选、技术筛选、形态筛选 | Yes | Planned |

## What This Repository Is

这是一个总 skill 仓库，而不是单一行情脚本目录。

当前：
- `noah-stock-market` 是已实现模块

后续：
- `noah-stock-portfolio`
- `noah-stock-trade`
- `noah-stock-screener`
- 其他金融接口能力

## Current Capabilities

当前 market 模块已支持：
- 股票快照 / 最新行情
- 市场状态
- 分时
- K线
- 摆盘
- 资金流向
- 基础信息

已补充的体验优化包括：
- 自然语言路由
- 股票名称解析
- 港股 / 美股歧义澄清
- detail mode（资金流向 / K线 / 分时）
- detail mode 默认展示最近 10 条
- 尾部 0 值资金流记录处理
- 更贴近最终用户的话术输出

## Requirements

使用前至少需要：
- Python 3
- `requests`
- 公司证券行情服务访问地址
- 公司证券行情服务 API key

## Configuration

安装后必须配置：
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

> 重要：这里必须使用**公司证券行情服务 API key**，不要使用 GitHub token、OpenClaw token 或其他平台凭证代替。

## Installation

请优先阅读：
- `SKILL.md`
- `MODULES.md`
- `INSTALL.md`
- `noah-stock-market/SKILL.md`

建议安装后先执行 smoke test，再进行自然语言查询验证。

## Quick Examples

示例问法：
- `看腾讯最近10根日K`
- `看腾讯资金流向`
- `看腾讯盘口`
- `看腾讯基础信息`
- `看腾讯市场状态`
- `查询阿里巴巴最近5条资金流向`

## Known Limitations

当前已知限制包括：
- 板块接口在当前环境未开放
- 期权接口在当前环境未开放或返回 404
- 美股 K线当前环境可能返回 404
- 后端实际返回条数不一定严格等于请求条数

更多已知边界见：
- `noah-stock-market/references/edge-cases.md`
- `noah-stock-market/references/known-limitations.md`

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
  noah-stock-portfolio/
    SKILL.md
  noah-stock-trade/
    SKILL.md
  noah-stock-screener/
    SKILL.md
```

## Roadmap

下一阶段优先方向：
1. 持续增强 market 模块的自然语言解析与输出体验
2. 接入 `noah-stock-portfolio`
3. 接入 `noah-stock-trade`
4. 接入 `noah-stock-screener`

## Notes

- 当前一期只承诺港股 / 美股只读市场数据能力
- 不提供投资建议
- 不应向最终用户暴露内部接口 URL、token 或脚本实现细节
