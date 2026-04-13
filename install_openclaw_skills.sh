#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"
TARGET_DIR="${HOME}/.openclaw/skills"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "[noah] skills/ 目录不存在：$SKILLS_DIR"
  echo "[noah] 请确认你是在安装包根目录执行本脚本。"
  exit 1
fi

mkdir -p "$TARGET_DIR"

for skill in noah-stock-market noah-stock-trade; do
  if [ -d "$SKILLS_DIR/$skill" ]; then
    rm -rf "$TARGET_DIR/$skill"
    cp -R "$SKILLS_DIR/$skill" "$TARGET_DIR/$skill"
    echo "[noah] installed: $skill -> $TARGET_DIR/$skill"
  else
    echo "[noah] skip missing skill: $skill"
  fi
done

echo
echo "[noah] 安装完成。"
echo "[noah] 下一步请配置："
echo "  - NOAH_MARKET_APIKEY"
echo "  - NOAH_TRADE_GROUP_NO"
echo
echo "[noah] 可参考："
echo "  - examples/noah-market.env.example"
echo "  - examples/noah-trade.env.example"
