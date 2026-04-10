# Publishing Checklist

在把 `noah-agent-skills` 发布到 GitHub 前，确认：

- [ ] 不包含 workspace 私有文件
- [ ] 不包含 `.secrets/` 或 token
- [ ] 不包含测试图片、临时文件、运行状态文件
- [ ] `noah-stock-market/` 目录结构完整
- [ ] `SKILL.md`、`references/`、`scripts/` 均可用
- [ ] `INSTALL.md` 已说明依赖与 token 配置
- [ ] `known-limitations.md` 已说明当前环境限制
- [ ] smoke test 可跑通港股主路径

建议：最终公开仓库根目录只保留技能相关内容，而不是整个开发 workspace。
