---
name: noah-stock-market
description: |
  Noah AI Skill installation guide.
  Capabilities: market snapshot, K-line, intraday, ticker, broker queue,
  capital flow, basic info, trading days, market/global state, IPO list, rank, and US analysis.
metadata:
  author: noah
  version: "1.2.3"
  last_updated: "2026-04-14"
---

# Noah Skill Installation Guide

By installing Noah Skills, you can query HK/US market data directly inside AI conversations, including snapshots, K-line, intraday trends, tick-by-tick trades, broker queue, capital flow, trading days, IPO lists, rank, and US analysis.

---

## Feature Overview

Current Noah Skills focus on **Search / Market Query Skills**.

| Capability | Description | Example |
|------------|-------------|---------|
| Snapshot / Latest Quote | Query latest price, open/high/low, and market snapshot | `What's Tencent's current price` |
| K-line Charts | Query daily K-line or date-range K-line data | `Tencent daily K-line for the last 10 bars` |
| Intraday / Ticker | View intraday trends and tick-by-tick data | `Show me Tencent intraday data` |
| Broker Queue | View broker queue data | `Show me Tencent broker queue` |
| Capital Flow | Query capital flow for a stock | `Tencent capital flow` |
| Basic Info | Query stock basic information | `When was Tencent listed` |
| Trading Days | Query trading calendar | `Show HK trading days this month` |
| Market / Global State | Query market status | `Is HK market open now` |
| IPO List | Query IPO list | `Show HK IPO list` |
| Rank | Query rank data | `Show HK top gainers rank` |
| US Analysis | Query analyst / target-price style info | `Show AAPL analyst view` |

> Current public release installs `noah-stock-market` by default.
> Finance HK/US and shareholder endpoints are present in the latest spec, but are still pending formal integration.

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
+-- search-skills/
|   +-- noah-stock-market/
+-- release/
|   +-- noah-install.md
|   +-- index.html
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

---

## Configure by Client

Choose the setup method for your AI client. This main install document supports multiple clients and keeps all install paths in one place.

| AI Client | Setup Method | Scope | Est. Time |
|-----------|-------------|-------|-----------|
| OpenClaw | Download ZIP, extract, and run installer script | Global / workspace | < 2 min |
| Claude Code CLI | Copy the skill folder into `~/.claude/skills/` | Global (all projects) | 2 min |
| Cursor / VS Code / JetBrains (with Claude Extension) | Reuse `~/.claude/skills/` | Global (all projects) | 2 min |
| Cursor (Built-in AI) | Copy `SKILL.md` into `~/.cursor/rules/` as a rule file | Global (all projects) | 2-3 min |
| Claude Desktop / Claude.ai | Paste a condensed version into Custom Instructions | Global (all conversations) | 3 min |
| AI tools that can read install guides | Send this guide or ZIP install instructions into the conversation | Depends on client | 1-3 min |

### Detailed Setup Steps

> 本文档是对外唯一主安装文档。OpenClaw、Claude Code、Cursor、Claude Desktop / Claude.ai 的安装方式统一收口在这里。

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

- install search / market query skills from the package
- create `~/.openclaw/.secrets/` if missing
- generate default market configuration if missing
- preserve existing configuration when possible
- allow immediate use with the built-in default market key in the current release

</details>

<details>
<summary><b>Claude Code CLI / Cursor / VS Code / JetBrains (with Claude Extension)</b> - Global Skills Directory</summary>

These tools can share the `~/.claude/skills/` directory. Install once and reuse across projects.

```bash
mkdir -p ~/.claude/skills
cp -R search-skills/noah-stock-market ~/.claude/skills/noah-stock-market
```

If you are installing from the ZIP package:

```bash
unzip noah-agent-skills-installer.zip
cd noah-agent-skills-installer
mkdir -p ~/.claude/skills
cp -R search-skills/noah-stock-market ~/.claude/skills/noah-stock-market
```

Because the current release includes a built-in default market key fallback, these clients can work even when they do not execute the OpenClaw installer script.

After copying, start a new conversation or reopen the client so the skill can be discovered.

</details>

<details>
<summary><b>Cursor (Built-in AI)</b> - Rules Directory</summary>

Copy `SKILL.md` into the Cursor rules directory as a standalone rule file.

```bash
mkdir -p ~/.cursor/rules
cp search-skills/noah-stock-market/SKILL.md ~/.cursor/rules/noah-stock-market.md
```

If you are installing from the ZIP package:

```bash
unzip noah-agent-skills-installer.zip
cd noah-agent-skills-installer
mkdir -p ~/.cursor/rules
cp search-skills/noah-stock-market/SKILL.md ~/.cursor/rules/noah-stock-market.md
```

The current release includes a built-in default market key fallback, so Cursor built-in AI can still use market queries without running the installer script first.

After copying, reopen Cursor or start a new conversation so the rules can take effect.

</details>

<details>
<summary><b>Claude Desktop / Claude.ai</b> - Custom Instructions</summary>

Open the Custom Instructions settings and paste a condensed version derived from Noah Stock Market instructions.

If the instruction box has strict limits, keep the capability summary, scope limits, and behavior rules from this main install document.

</details>

---

## Verify Installation

Current release includes a built-in market API key fallback for direct experience. After installation, you can verify immediately with:

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
- Current release includes a built-in default market API key fallback for direct experience.
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
<summary><b>The skill is visible, but market queries still fail</b></summary>

Check whether the client has reloaded rules / skills. In the current release, the built-in default market key fallback is enabled, so non-installer clients such as Cursor or Claude Code should also be able to run basic market queries.

</details>

<details>
<summary><b>ZIP file won't download or extract</b></summary>

- Check your network connection
- Re-download the ZIP file
- Confirm your extraction tool supports .zip files

</details>
