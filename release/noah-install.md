---
name: noah-stock-market
description: |
  Noah Agent Skills installation guide for AI clients.
  Capabilities: market snapshot, K-line, intraday, ticker, broker queue, order book,
  capital flow, basic info, trading days, market/global state, IPO list, rank, and US analysis.
metadata:
  author: noah
  version: "1.2.0"
  last_updated: "2026-04-14"
---

# Noah Skills Installation Guide

通过安装 Noah Skills，您可以在 AI 对话中直接查询港股 / 美股市场数据，包括快照、K 线、分时、逐笔、摆盘、资金流向、交易日历、IPO 列表、排行榜与美股分析，无需在多个系统之间来回切换。

---

## Feature Overview

当前 Noah Skills 对外默认提供 **Market Skills**：

| Capability | Description | Example |
|------------|-------------|---------|
| Snapshot / Latest Quote | 查询股票最新价格、涨跌、开高低 | `腾讯现在多少钱` |
| K-line | 查询日 K / 区间 K 线 | `看腾讯最近 10 根日 K` |
| Intraday / Ticker | 查看分时走势与逐笔成交 | `看腾讯分时` |
| Order Book / Broker Queue | 查看买卖盘和经纪队列 | `看腾讯盘口` |
| Capital Flow | 查询个股资金流向 | `看腾讯资金流向` |
| Basic Info | 查询个股基础信息 | `腾讯什么时候上市` |
| Trading Days | 查询交易日历 | `看港股本月交易日` |
| Market / Global State | 查询市场状态 | `港股现在开盘了吗` |
| IPO List | 查询港股 IPO 列表 | `看港股 IPO 列表` |
| Rank | 查询排行榜 | `看港股涨跌幅排行榜` |
| US Analysis | 查询美股分析师信息 | `看 AAPL 分析师评级` |

> 当前版本默认只安装 `noah-stock-market`。
> `stock_filter` 协议已纳入，但当前环境暂不对外暴露。

---

## Quick Start

推荐顺序：
1. 先让 AI 读取本安装指引
2. 再根据本指引下载 Noah 安装包并解压

下载 Noah 安装包并解压：

**[Download noah-agent-skills-installer.zip](./noah-agent-skills-installer.zip)**

```bash
unzip noah-agent-skills-installer.zip
cd noah-agent-skills-installer
bash install_openclaw_skills.sh
```

安装包结构：

```text
noah-agent-skills-installer/
+-- skills/
|   +-- noah-stock-market/
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

---

## Configure by Client

### OpenClaw

推荐先向 OpenClaw 发送下面这句话，让 AI 先读取安装指引：

```text
根据指引安装 Noah Skills：./noah-install.md
```

如果你使用的是公开页面，请把上面的地址替换成线上可访问的 `noah-install.md` 链接。

安装指引会再引用 zip 下载地址与安装步骤。也可以直接通过 ClawHub / OpenClaw Skills 安装：

```bash
openclaw skills install noah-stock-market
```

更新：

```bash
openclaw skills update noah-stock-market
```

### ClawHub CLI

安装：

```bash
clawhub install noah-stock-market
```

更新：

```bash
clawhub update noah-stock-market
```

当前已发布版本：

```text
noah-stock-market@1.2.0
```

### GitHub / ZIP 安装

```bash
git clone https://github.com/xuyun9160-lgtm/noah-agent-skills.git
cd noah-agent-skills
bash install_openclaw_skills.sh
```

或下载 zip 后解压，再执行：

```bash
bash install_openclaw_skills.sh
```

---

## Verify Installation

安装完成后，请先在配置文件中填入：

```bash
NOAH_MARKET_APIKEY=your_api_key_here
```

然后执行最小验证：

```bash
python3 noah-stock-market/scripts/run_query.py snapshot HK-00700
python3 noah-stock-market/scripts/run_query.py ipo_list HK market=HK
python3 noah-stock-market/scripts/run_query.py rank HK market_codes=HK rank_field=raisePercent page=1 page_size=10
```

如果可以返回数据，则说明安装成功。

---

## Notes

- 当前 market Base URL 已内置为：
  `https://securities-open-api.noahgroup.com`
- 只需提供 `NOAH_MARKET_APIKEY`，不需要额外配置 Base URL。
- 当前版本默认只安装 `noah-stock-market`。
- `noah-stock-trade` 保留在仓库继续完善，但当前版本暂不作为默认安装项。
- 所有 OpenAPI 枚举参数必须严格从 `enum.yaml` 取值，不应按语义猜测。

---

## FAQ

### 安装后 AI 说找不到 Noah 能力怎么办？

部分客户端需要新开会话或重新加载 Skills。确认安装完成后，建议重新开一个新对话测试。

### 为什么 skill 能看到，但调用失败？

通常是 `NOAH_MARKET_APIKEY` 缺失、失效或权限不匹配。skill 被发现不等于鉴权一定通过。

### 为什么没有开放 stock_filter？

因为当前环境尚未稳定支持，所以虽然协议文件已纳入 skill，但本版本不对外暴露。
