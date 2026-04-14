---
name: noah-stock-market
description: |
  Noah AI Skill installation guide.
  Capabilities: market snapshot, K-line, intraday, ticker, broker queue, order book,
  capital flow, basic info, trading days, market/global state, IPO list, rank, and US analysis.
metadata:
  author: noah
  version: "1.2.0"
  last_updated: "2026-04-14"
---

# Noah Skill Installation Guide

By installing Noah Skills, you can query HK/US market data directly inside AI conversations, including snapshots, K-line, intraday trends, tick-by-tick trades, broker queue, order book, capital flow, trading days, IPO lists, rank, and US analysis.

---

## Feature Overview

Current Noah Skills focus on **Market Skills**.

| Capability | Description | Example |
|------------|-------------|---------|
| Snapshot / Latest Quote | Query latest price, open/high/low, and market snapshot | `What's Tencent's current price` |
| K-line Charts | Query daily K-line or date-range K-line data | `Tencent daily K-line for the last 10 bars` |
| Intraday / Ticker | View intraday trends and tick-by-tick data | `Show me Tencent intraday data` |
| Order Book / Broker Queue | View order book and broker queue | `Show me Tencent's order book` |
| Capital Flow | Query capital flow for a stock | `Tencent capital flow` |
| Basic Info | Query stock basic information | `When was Tencent listed` |
| Trading Days | Query trading calendar | `Show HK trading days this month` |
| Market / Global State | Query market status | `Is HK market open now` |
| IPO List | Query IPO list | `Show HK IPO list` |
| Rank | Query rank data | `Show HK top gainers rank` |
| US Analysis | Query analyst / target-price style info | `Show AAPL analyst view` |

> Current public release installs `noah-stock-market` by default.
> `stock_filter` is currently not exposed in the active environment.

---

## Quick Start

Download the installation package, extract it, and install Noah Skills.

**[Download noah-agent-skills-installer.zip](https://securities-open-api.t2.test.noahgrouptest.com/noah-agent-skills-installer.zip)**

After downloading, extract and install:

```bash
unzip noah-agent-skills-installer.zip
cd noah-agent-skills-installer
bash install_openclaw_skills.sh
```

Extracted directory structure:

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

Choose the setup method for your AI client. This guide currently focuses on the ZIP installation path.

| AI Client | Setup Method | Scope | Est. Time |
|-----------|-------------|-------|-----------|
| OpenClaw | Download ZIP, extract, and run installer script | Global / workspace | < 2 min |
| AI tools that can read install guides | Send this guide or ZIP install instructions into the conversation | Depends on client | 1-3 min |

### Detailed Setup Steps

<details>
<summary><b>OpenClaw</b> - ZIP install</summary>

Download the ZIP package:

```text
https://securities-open-api.t2.test.noahgrouptest.com/noah-agent-skills-installer.zip
```

Then run:

```bash
unzip noah-agent-skills-installer.zip
cd noah-agent-skills-installer
bash install_openclaw_skills.sh
```

The installer will automatically:

- install `noah-stock-market`
- create `~/.openclaw/.secrets/` if missing
- generate default market configuration if missing
- preserve existing configuration when possible

</details>

---

## Verify Installation

Current release includes a built-in market API key for direct experience. After installation, you can verify immediately with:

```bash
python3 noah-stock-market/scripts/run_query.py snapshot HK-00700
python3 noah-stock-market/scripts/run_query.py ipo_list HK market=HK
python3 noah-stock-market/scripts/run_query.py rank HK market_codes=HK rank_field=raisePercent page=1 page_size=10
```

If these commands return data successfully, the installation is ready.

---

## Notes

- The market Base URL is built in:
  `https://securities-open-api.noahgroup.com`
- Current release includes a default market API key for direct experience.
- Current release installs `noah-stock-market` by default.
- `noah-stock-trade` remains in the repository for ongoing development, but is not the default install target in this release.
- All OpenAPI enum parameters must be taken from `enum.yaml`, not guessed semantically.

---

## FAQ

<details>
<summary><b>The conversation says it can't find Noah capabilities</b></summary>

Some clients require starting a new conversation or reloading skills after installation. If needed, start a fresh session and retry.

</details>

<details>
<summary><b>ZIP file won't download or extract</b></summary>

- Check your network connection
- Re-download the ZIP file
- Confirm your extraction tool supports .zip files

</details>
