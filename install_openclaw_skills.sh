#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${HOME}/.openclaw/skills"

if [ -d "$SCRIPT_DIR/skills/noah-stock-market" ] && [ -d "$SCRIPT_DIR/skills/noah-stock-trade" ]; then
  SOURCE_ROOT="$SCRIPT_DIR/skills"
elif [ -d "$SCRIPT_DIR/noah-stock-market" ] && [ -d "$SCRIPT_DIR/noah-stock-trade" ]; then
  SOURCE_ROOT="$SCRIPT_DIR"
else
  echo "[noah] 未找到可安装的 skill 目录。"
  echo "[noah] 需要满足以下任一结构："
  echo "  1) 安装包结构：./skills/noah-stock-market 和 ./skills/noah-stock-trade"
  echo "  2) 仓库结构：./noah-stock-market 和 ./noah-stock-trade"
  exit 1
fi

mkdir -p "$TARGET_DIR"

for skill in noah-stock-market noah-stock-trade; do
  if [ -d "$SOURCE_ROOT/$skill" ]; then
    rm -rf "$TARGET_DIR/$skill"
    cp -R "$SOURCE_ROOT/$skill" "$TARGET_DIR/$skill"
    echo "[noah] installed: $skill -> $TARGET_DIR/$skill"
  else
    echo "[noah] skip missing skill: $skill"
  fi
done

echo
echo "[noah] 安装完成。"
echo "[noah] 下一步只需配置："
echo "  - NOAH_MARKET_APIKEY"
echo "  - NOAH_TRADE_GROUP_NO"
echo
echo "[noah] 可参考："
if [ -d "$SCRIPT_DIR/examples" ]; then
  echo "  - examples/noah-market.env.example"
  echo "  - examples/noah-trade.env.example"
else
  echo "  - noah-market.env.example"
  echo "  - noah-trade.env.example"
fi
