# Install Noah Agent Skills

`noah-stock-market` 是一个面向港股 / 美股市场数据查询的只读技能。适用于股票快照、市场状态、分时、K线、摆盘、资金流向、基础信息等查询场景。

## Included Skill

| Skill | Description | Auth Required |
|---|---|:---:|
| `noah-stock-market` | 港股 / 美股只读市场数据查询与结构化摘要 | Yes |

## Requirements

- Python 3
- `requests`
- 公司证券行情服务可用的 API 配置：
  - `NOAH_API_BASE_URL`
  - `NOAH_MARKET_APIKEY`

安装依赖：

```bash
pip install requests
```

## Configure API Access

本 skill 依赖公司证券行情服务，安装后必须配置 API token，否则 skill 只能被加载，不能执行真实查询。

推荐配置文件：

```text
<repo-or-workspace-root>/.secrets/noah-market.env
```

示例：

```bash
NOAH_API_BASE_URL=https://securities-open-api.t2.test.noahgrouptest.com
NOAH_MARKET_APIKEY=your_token_here
```

## Verify Installation

在 `noah-stock-market/` 目录下运行：

```bash
python3 scripts/smoke_test.py
python3 scripts/nl_smoke_test.py
```

## Usage

精准调用：

```bash
python3 scripts/run_query.py snapshot HK-00700
python3 scripts/run_query.py kline HK-00700 num=10 ktype=K_DAY
python3 scripts/run_query.py capital_flow HK-00700 num=5
```

自然语言调用：

```bash
python3 scripts/route_query.py 看腾讯最近10根日K
python3 scripts/route_query.py 看腾讯资金流向
```

## Current Notes

- 当前港股主路径已验证较稳定
- 美股 K 线仍需继续排查
- 板块与期权能力当前环境不建议作为强承诺能力
