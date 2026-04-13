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
# Base URL is built in. Only fill in your market API key.
# Built-in default base URL: https://securities-open-api.noahgroup.com
NOAH_MARKET_APIKEY=
EOF
  log "已生成 market 配置模板：$MARKET_ENV"
else
  log "已存在 market 配置：$MARKET_ENV（保留不覆盖）"
fi

need_market_key="yes"
if grep -Eq '^NOAH_MARKET_APIKEY=.+' "$MARKET_ENV"; then
  need_market_key="no"
fi

echo
log "安装完成。"
if [ "$need_market_key" = "yes" ]; then
  log "继续使用前，请补充以下配置："
  log "- NOAH_MARKET_APIKEY -> $MARKET_ENV"
else
  log "检测到 market 必要配置已存在，可直接继续使用。"
fi
