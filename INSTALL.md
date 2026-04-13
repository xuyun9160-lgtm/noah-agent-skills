# Install Noah Agent Skills

`noah-agent-skills` 当前正在收敛为两个主模块：
- `noah-stock-market`
- `noah-stock-trade`

其中：
- `noah-stock-market` 面向港股 / 美股市场数据查询
- `noah-stock-trade` 面向账户、持仓、资产、资金流水、订单、成交、费用与交易前评估

## Current Modules

| Module | Description | Auth Required |
|---|---|:---:|
| `noah-stock-market` | 港股 / 美股只读市场数据查询与结构化摘要 | Yes |
| `noah-stock-trade` | 账户、持仓、证券资产、资金流水、成交、未完成订单、费用预估、可买可卖、最大可买 | Yes |

## Requirements

- Python 3
- `requests`

安装依赖：

```bash
pip install requests
```

## Configure API Access

### Market module
推荐配置文件：

```text
<repo-or-workspace-root>/.secrets/noah-market.env
```

当前市场服务 Base URL 已内置，安装后只需配置：

```bash
NOAH_MARKET_APIKEY=your_api_key_here
```

### Trade module
推荐配置文件：

```text
<repo-or-workspace-root>/.secrets/noah-trade.env
```

当前交易服务 Base URL 已内置，安装后只需配置：

```bash
NOAH_TRADE_GROUP_NO=100636524
```

说明：
- 当前交易侧通过请求头中的 `groupNo` 访问账户分组
- 当前测试口径下暂不需要单独 token
- 如需高级配置，可再补 `NOAH_TRADE_ENV`、`NOAH_TRADE_READ_ONLY`、`NOAH_TRADE_TIMEOUT`

## One-click Install

### Install from GitHub repository
在仓库根目录执行：

```bash
bash install_openclaw_skills.sh
```

脚本会：
- 将 `skills/noah-stock-market` 安装到 `~/.openclaw/skills/`
- 将 `skills/noah-stock-trade` 安装到 `~/.openclaw/skills/`
- 提示下一步需要配置 `NOAH_MARKET_APIKEY` 与 `NOAH_TRADE_GROUP_NO`

> 如果你当前使用的是仓库源码目录而不是安装包，请先确保仓库根目录下存在 `skills/` 目录结构，或在发布包中执行该脚本。

## Verify Installation

### Verify market
在 `noah-stock-market/` 目录下运行：

```bash
python3 scripts/smoke_test.py
python3 scripts/nl_smoke_test.py
```

### Verify trade
在 `noah-stock-trade/` 目录下可优先运行：

```bash
python3 scripts/noah_trade_cli.py account-info
python3 scripts/noah_trade_cli.py positions
python3 scripts/noah_trade_cli.py sec-asset
python3 scripts/noah_trade_cli.py sec-capital-flow --start-date 20260401 --end-date 20260413
python3 scripts/noah_trade_cli.py today-deals
python3 scripts/noah_trade_cli.py history-deals --start-date 20260401 --end-date 20260413
python3 scripts/noah_trade_cli.py fee-estimate --symbol HK.00700 --side BUY --order-type LIMIT --price 320 --qty 100
python3 scripts/noah_trade_cli.py stock-amount --symbol HK.00700 --order-type LO
python3 scripts/noah_trade_cli.py max-enable-buy-amt --symbol HK.00700 --order-type LO --entrust-price 320
```

## Usage

### Market examples
```bash
python3 noah-stock-market/scripts/run_query.py snapshot HK-00700
python3 noah-stock-market/scripts/run_query.py kline HK-00700 num=10 ktype=K_DAY
python3 noah-stock-market/scripts/run_query.py capital_flow HK-00700 num=5
```

### Trade examples
```bash
python3 noah-stock-trade/scripts/noah_trade_cli.py account-info
python3 noah-stock-trade/scripts/noah_trade_cli.py positions
python3 noah-stock-trade/scripts/noah_trade_cli.py unfinished-orders
python3 noah-stock-trade/scripts/noah_trade_cli.py fee-estimate --symbol HK.00700 --side BUY --order-type LIMIT --price 320 --qty 100
```

## Current Notes

- 当前 `market` 模块已相对成熟
- 当前 `trade` 模块主干能力已能联调成功，但部分订单详情类接口仍属于已知问题
- 已知异常请查看：
  - `noah-stock-trade/references/api-issues.md`
