#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${HOME}/.openclaw/skills"
SECRETS_DIR="${HOME}/.openclaw/.secrets"
MARKET_ENV="$SECRETS_DIR/noah-market.env"

log() {
  echo "[noah-installer] $*"
}

if [ -d "$SCRIPT_DIR/skills/noah-stock-market" ]; then
  SOURCE_ROOT="$SCRIPT_DIR/skills"
  SOURCE_MODE="installer"
elif [ -d "$SCRIPT_DIR/noah-stock-market" ]; then
  SOURCE_ROOT="$SCRIPT_DIR"
  SOURCE_MODE="repository"
else
  log "未找到可安装的 market skill 目录。"
  log "需要满足以下任一结构："
  log "1) 安装包结构：./skills/noah-stock-market"
  log "2) 仓库结构：./noah-stock-market"
  exit 1
fi

log "检测到安装来源：$SOURCE_MODE"
mkdir -p "$TARGET_DIR"
mkdir -p "$SECRETS_DIR"
log "技能目录：$TARGET_DIR"
log "配置目录：$SECRETS_DIR"

rm -rf "$TARGET_DIR/noah-stock-market"
cp -R "$SOURCE_ROOT/noah-stock-market" "$TARGET_DIR/noah-stock-market"
log "已安装 noah-stock-market"
log "当前版本暂不默认安装 noah-stock-trade"

if [ ! -f "$MARKET_ENV" ]; then
  cat > "$MARKET_ENV" <<'EOF'
# Noah market config
# Base URL is built in.
# Current release includes a default market API key for direct experience.
# Built-in default base URL: https://securities-open-api.noahgroup.com
NOAH_MARKET_APIKEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZWN1cml0aWVzLW9wZW4tYXBpIiwiZ3JvdXBfbm8iOiIxMDEwMTM1MjAiLCJvcGVuX2hrX3N0b2NrX3N0YXR1cyI6IjAiLCJvcGVuX3VzX3N0b2NrX3N0YXR1cyI6IjAifQ.cZEYiilI2nYwEbcBJmPG9oAIq6hYZhIwz9uEZsQ0cBM
EOF
  log "已生成 market 默认配置：$MARKET_ENV"
else
  log "已存在 market 配置：$MARKET_ENV（保留不覆盖）"
fi

echo
log "安装完成。"
log "当前版本已内置默认 market API key，可直接体验 market 能力。"
