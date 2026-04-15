---
name: noah-module-skill-builder
description: Build new Noah internal skills from API documents and apply the full Noah delivery workflow. Use when a new module/API domain needs to become a new skill, or when an existing module must be regenerated/refactored from updated OpenAPI/API docs. Triggers when the user provides new API documentation and asks to create, bootstrap, update, package, or publish a Noah skill with production/test environments, release pages, install docs, ZIP packaging, and ClawHub publishing.
---

# Noah Module Skill Builder

## Overview

Use this skill when a new Noah module needs to be turned into a working skill package from API documentation.

The goal is not only to write code, but to complete the entire Noah workflow:
- build the new skill directory
- implement client / CLI / docs
- align production and test environments
- generate release artifacts
- package ZIPs with the standard directory structure
- publish and sync global skills when needed

This skill is the standard bootstrapper for future Noah modules.

## Core Workflow

When the user provides API documentation for a new module, execute the workflow in this order.

### 1. Read and understand the API document

First identify:
- module scope and name
- whether it belongs to market, trade, or a new category
- authentication method
- production and test base URLs
- required parameters and enums
- read-only vs write operations
- output structures in `data`

Extract concrete differences if this is an updated version of an existing API.

Always identify and explicitly note:
- auth requirements
- base URL split between market/trade or other modules
- parameter changes such as required fields or renamed fields
- environment differences between prod and test

### 2. Create or update the skill directory

Default target pattern inside `export-noah-agent-skills/`:

```text
<module-skill>/
+-- SKILL.md
+-- references/
+-- scripts/
```

Use a concise hyphen-case name.
Examples:
- `noah-stock-market`
- `noah-stock-trade`
- future modules should follow the same naming style

Minimum required structure for a new skill:
- `SKILL.md`
- `references/openapi.yaml`
- `references/current-availability.md`
- `references/usage-guide.md`
- `references/auth-and-preflight.md`
- `scripts/` implementation files

### 3. Implement the skill from the API document

At minimum, build:
- a config loader
- an HTTP client
- a CLI entry or equivalent deterministic script entry
- summary / formatter logic for user-facing output
- `SKILL.md` capability scope and user trigger language

Implementation rules:
- follow the latest API doc exactly
- never guess enum values if docs define them
- treat required params as required in CLI and docs
- if prod/test base URLs differ, preserve both in the release workflow
- if a capability is not officially open, state it explicitly

### 4. Write user-facing skill behavior

The resulting skill must answer two different layers well:

#### A. Actual query/use behavior
- return useful structured summaries
- avoid exposing internal implementation details to end users
- prefer concise business language
- when possible, use real tested data patterns in examples, not empty placeholders

#### B. “What can this skill do?” behavior
If users ask what the skill supports, add a standard capability answer directly into the skill.
The standard answer should:
- list supported capabilities clearly
- distinguish unavailable write actions if needed
- include realistic example prompts

### 5. Update shared repository docs

Every new or updated module must be reflected in repository-level docs.
At minimum review and update as needed:
- `README.md`
- `INSTALL.md`
- `release/noah-install.md`
- `release/index.html`
- module `SKILL.md`
- relevant references files

Do not stop at the module folder if the user-facing delivery surface also changes.

## Noah Release Workflow (Mandatory)

For every new or updated module, follow `export-noah-agent-skills/RELEASE_WORKFLOW.md`.

Read that file before final packaging/publishing work.

Apply these rules as mandatory, not optional.

### Key rules to inherit from RELEASE_WORKFLOW.md

#### Auth rule
- market and trade currently share one common token when applicable
- token is not built in
- users configure `NOAH_MARKET_APIKEY` themselves after installation

#### Environment rule
Always distinguish production vs test:
- production URLs
- test URLs
- matching release docs and ZIP links

#### Dual-environment release rule
Always generate both:
- production artifacts
- test artifacts

Each environment must include:
- page / index
- main install doc / md
- ZIP package

#### Packaging structure rule
Production ZIP root must be:

```text
noah-agent-skills-installer/
+-- search-skills/
+-- release/
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

Test ZIP root must be:

```text
noah-agent-skills-installer-test/
+-- search-skills/
+-- release/
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

#### Test naming rule
All outward-facing test artifacts must use `-test` consistently:
- `index-test.html`
- `noah-install-test.md`
- `noah-agent-skills-installer-test.zip`
- ZIP root directory must also include `-test`

#### Page generation rule
After generating pages:
- check JS syntax
- escape apostrophes in JS string literals
- verify interactive controls such as copy buttons
- do not assume visual correctness means script correctness

## Standard Release Sequence

Use this exact sequence whenever the user asks to fully deliver a module.

### Step 1: modify code
- update module code
- update references
- update client / CLI / formatter logic

### Step 2: update docs
- module docs
- repo docs
- release docs

### Step 3: test critical APIs
- run real API checks when possible
- validate changed parameters and required fields
- confirm example scenarios using real responses when possible

### Step 4: generate production artifacts
Generate:
- `release/index.html`
- `release/noah-install.md`
- `release/noah-agent-skills-installer.zip`

### Step 5: generate test artifacts
Generate:
- `release-test/index-test.html`
- `release-test/noah-install-test.md`
- `release-test/noah-agent-skills-installer-test.zip`

### Step 6: validate actual deliverables
Check the files users will actually open/download:
- page
- md
- zip

Do not validate only the source tree.

### Step 7: publish
When requested, perform:
- git commit
- git push
- ClawHub publish

### Step 8: sync global skills if needed
If the user wants immediate local usability, sync to:
- `~/.openclaw/skills/...`

Then run:
- `python3 -m py_compile ...`
- a minimal runtime check if possible

## Output Standards

When generating examples for pages or docs:
- prefer real tested responses
- do not use vague filler like “already returned relevant data” if actual values are known
- reflect currently supported capability scope accurately
- when assets/positions involve multiple currencies, do not directly cross-sum HKD/USD/CNY amounts without exchange-rate basis
- if total assets must be described without FX basis, list them by currency and state that no FX conversion was applied

When documenting token setup:
- say token is not built in
- explain that users configure it after installation
- if the surface is OpenClaw-specific, include path example:
  - `~/.openclaw/.secrets/noah-market.env`

## What not to do

Do not:
- mix production and test naming
- keep stale ZIP root structures
- claim support without syncing page/md/zip together
- rely on temporary packaging layouts as formal delivery format
- leave JS pages with unescaped apostrophes in single-quoted strings
- update the repo but forget global skill sync when the user asked for local availability

## Resources

### references/
- Read `../RELEASE_WORKFLOW.md` whenever you are packaging or publishing
- Store incoming API specs in `references/` for the module being built
- Keep environment/auth notes in module references files

## Quick Start for Future Runs

When the user says they have a new API document and want a new skill:
1. read the API document
2. determine module name and scope
3. scaffold or update the module skill
4. implement client/CLI/docs
5. run tests on critical endpoints
6. update release docs
7. generate production + test artifacts
8. publish if requested

This skill should be treated as the default bootstrap workflow for all future Noah module additions.
