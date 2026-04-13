# noah-agent-skills Repository Structure

目标：让别人拿到仓库地址后，能直接定位并安装 skill，而不需要理解开发用 workspace。

## Recommended Published Layout

```text
repo-root/
  SKILL.md
  MODULES.md
  ARCHITECTURE.md
  INSTALL.md
  README.md
  FINAL-STATUS.md
  noah-stock-market/
    SKILL.md
    references/
    scripts/
  noah-stock-trade/
    SKILL.md
    references/
    scripts/
  archive/
    noah-stock-portfolio/
    noah-stock-screener/
```

## Publishing Direction

建议对外长期主结构收敛为：
- `noah-stock-market`
- `noah-stock-trade`

其中：
- `archive/noah-stock-portfolio/` 为已归档旧模块
- `archive/noah-stock-screener/` 为已归档旧模块

## Current Development Layout

当前开发目录位于：

```text
workspace-root/
  export-noah-agent-skills/
    noah-stock-market/
    noah-stock-trade/
    archive/
```

发布到 GitHub 时，建议让仓库根目录直接承载 skill 集合，而不是把整个 workspace 上传。

## Publishing Principle

- 只发布 `export-noah-agent-skills/` 下的技能内容
- 不发布 workspace 私有文件
- 不发布本地 secrets
- 不发布无关测试产物
