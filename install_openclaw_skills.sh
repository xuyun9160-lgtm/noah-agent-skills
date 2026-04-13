#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${HOME}/.openclaw/skills"
SECRETS_DIR="${HOME}/.openclaw/.secrets"
MARKET_ENV="$SECRETS_DIR/noah-market.env"
TRADE_ENV="$SECRETS_DIR/noah-trade.env"

log() {
  echo "[noah-installer] $*"
}

if [ -d "$SCRIPT_DIR/skills/noah-stock-market" ] && [ -d "$SCRIPT_DIR/skills/noah-stock-trade" ]; then
  SOURCE_ROOT="$SCRIPT_DIR/skills"
  SOURCE_MODE="installer"
elif [ -d "$SCRIPT_DIR/noah-stock-market" ] && [ -d "$SCRIPT_DIR/noah-stock-trade" ]; then
  SOURCE_ROOT="$SCRIPT_DIR"
  SOURCE_MODE="repository"
else
  log "未找到可安装的 skill 目录。"
  log "需要满足以下任一结构："
  log "1) 安装包结构：./skills/noah-stock-market 和 ./skills/noah-stock-trade"
  log "2) 仓库结构：./noah-stock-market 和 ./noah-stock-trade"
  exit 1
fi

log "检测到安装来源：$SOURCE_MODE"
mkdir -p "$TARGET_DIR"
mkdir -p "$SECRETS_DIR"
log "技能目录：$TARGET_DIR"
log "配置目录：$SECRETS_DIR"

for skill in noah-stock-market noah-stock-trade; do
  if [ -d "$SOURCE_ROOT/$skill" ]; then
    rm -rf "$TARGET_DIR/$skill"
    cp -R "$SOURCE_ROOT/$skill" "$TARGET_DIR/$skill"
    log "已安装 $skill"
  else
    log "跳过缺失模块：$skill"
  fi
done

if [ ! -f "$MARKET_ENV" ]; then
  cat > "$MARKET_ENV" <<'EOF'
# Noah market config
# Base URL is built in. Only fill in your market API key.
NOAH_MARKET_APIKEY=
EOF
  log "已生成 market 配置模板：$MARKET_ENV"
else
  log "已存在 market 配置：$MARKET_ENV（保留不覆盖）"
fi

if [ ! -f "$TRADE_ENV" ]; then
  cat > "$TRADE_ENV" <<'EOF'
# Noah trade config
# Base URL is built in. Only fill in your trade group number.
NOAH_TRADE_GROUP_NO=
# Optional
# NOAH_TRADE_ENV=test
# NOAH_TRADE_READ_ONLY=true
# NOAH_TRADE_TIMEOUT=15
EOF
  log "已生成 trade 配置模板：$TRADE_ENV"
else
  log "已存在 trade 配置：$TRADE_ENV（保留不覆盖）"
fi

need_market_key="yes"
need_trade_group="yes"
if grep -Eq '^NOAH_MARKET_APIKEY=.+' "$MARKET_ENV"; then
  need_market_key="no"
fi
if grep -Eq '^NOAH_TRADE_GROUP_NO=.+' "$TRADE_ENV"; then
  need_trade_group="no"
fi

echo
log "安装完成。"
if [ "$need_market_key" = "yes" ] || [ "$need_trade_group" = "yes" ]; then
  log "继续使用前，请补充以下配置："
  if [ "$need_market_key" = "yes" ]; then
    log "- NOAH_MARKET_APIKEY -> $MARKET_ENV"
  fi
  if [ "$need_trade_group" = "yes" ]; then
    log "- NOAH_TRADE_GROUP_NO -> $TRADE_ENV"
  fi
else
  log "检测到必要配置已存在，可直接继续使用。"
fi
