# Final Release Check

## 1. 仓库边界
- [x] 当前发布单元应为 `noah-agent-skills/`
- [x] 不应发布整个 workspace

## 2. 目录结构
- [x] 根目录包含：`INSTALL.md`、`PUBLISHING-CHECKLIST.md`、`PUBLISHING-SUMMARY.md`、`REPO-STRUCTURE.md`
- [x] `noah-stock-market/` 包含：`SKILL.md`、`references/`、`scripts/`

## 3. 敏感信息
- [x] 未扫出真实 token
- [x] 未扫出本地绝对路径
- [ ] 仍存在 `__pycache__/` 与 `.pyc`，发布前应清理

## 4. 安装说明
- [x] 已说明 Python 3 与 `requests`
- [x] 已说明 `NOAH_API_BASE_URL` 与 `NOAH_MARKET_TOKEN`
- [x] 已说明 smoke test 用法

## 5. 一期已验证能力
- [x] 快照
- [x] 市场状态
- [x] 分时
- [x] K线（港股主路径）
- [x] 摆盘
- [x] 资金流向
- [x] 基础信息

## 6. 当前限制
- [x] 板块接口：生产环境暂不支持
- [x] 期权链/到期日：未验证通过
- [x] 美股 K 线：当前返回 404

## 7. 自然语言入口
- [x] 腾讯相关主路径可用
- [ ] 美股 K 线自然语言虽然能路由，但后端仍未打通

## Release Advice

发布前建议最后执行：

```bash
find noah-stock-market -type d -name '__pycache__' -prune -exec rm -rf {} +
find noah-stock-market -name '*.pyc' -delete
```

然后再次确认 `.secrets/` 未进入发布内容。
