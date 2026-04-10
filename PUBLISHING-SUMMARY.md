# Publishing Summary

## What a public consumer should see

公开仓库中的阅读顺序建议：

1. `SKILL.md`（总 skill 入口）
2. `MODULES.md`
3. `INSTALL.md`
4. `noah-stock-market/SKILL.md`
5. `noah-stock-market/references/usage-guide.md`
6. `noah-stock-market/references/known-limitations.md`

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
- references 与 scripts
- 发布前检查说明

当前仍建议注意：
- 公开仓库中不要包含 `.secrets/`
- 不要把整个 workspace 上传
- 如果最终对外公开，建议再次人工检查 scripts 中是否还有过于内部的描述
