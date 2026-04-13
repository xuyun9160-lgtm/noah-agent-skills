# Publishing Summary

## What a public consumer should see

公开仓库中的阅读顺序建议：

1. `SKILL.md`（总 skill 入口）
2. `MODULES.md`
3. `INSTALL.md`
4. `noah-stock-market/SKILL.md`
5. `noah-stock-market/references/usage-guide.md`
6. `noah-stock-trade/SKILL.md`
7. `noah-stock-trade/references/current-availability.md`
8. `noah-stock-trade/references/api-issues.md`

## What a public consumer should NOT need to know

最终用户不应关心：
- 开发用 workspace 名称
- 你的本地路径
- 内部调试过程
- token 在哪里生成
- 接口调试细节

## Current publishability assessment

当前 `noah-agent-skills/` 已具备：
- 基础安装说明
- skill 本体
- market / trade 两条主线的文档与脚本骨架
- trade 模块的已成功能力说明
- trade 模块的异常接口清单
- 发布前检查说明

当前仍建议注意：
- 公开仓库中不要包含 `.secrets/`
- 不要把整个 workspace 上传
- 如果最终对外公开，建议再次人工检查 scripts 中是否还有过于内部的描述
- 在正式发布前，可考虑删除或归档 `noah-stock-portfolio` 与 `noah-stock-screener`，避免与最终两模块结构冲突

## Recommended public shape

建议对外呈现的最终结构逐步收敛为：
- `noah-stock-market`
- `noah-stock-trade`

其中：
- 原 `noah-stock-portfolio` 能力并入 `trade`
- 原 `noah-stock-screener` 能力并入 `market` 或直接下线

这样更适合后续按 Futu 风格做成可安装的 Noah Agent Skills 套件。
