# RELEASE_WORKFLOW.md

## 目标

`export-noah-agent-skills` 的发布、打包、文档更新、环境区分和最终交付，统一按本文件执行。

本文件用于避免以下问题反复出现：
- 代码改了，但 README / INSTALL / release 页面 / 主安装文档没同步
- 测试环境和生产环境命名、目录、链接口径不一致
- ZIP 实际目录结构与对外文档承诺不一致
- 页面可见内容改了，但脚本报错、复制按钮失效
- 仓库已更新，但全局 skill 还是旧版

---

## 一、模块口径

当前 Noah Agent Skills 收口为两个主模块：

- `noah-stock-market`
  - 市场数据、行情、K线、分时、逐笔、经纪队列、资金流向、基础信息、交易日历、IPO、排行榜、财务、股东增减持等查询能力
- `noah-stock-trade`
  - 账户、持仓、资产、资金流水、订单、成交、订单详情、费用详情、可买可卖、最大可买、费用预估、推送数据查询等交易查询能力

写操作能力（如下单 / 改单 / 撤单）若未正式开放，必须明确标注为暂不开放。

---

## 二、鉴权规则

### 统一鉴权口径
- `market` 和 `trade` 共用一个通用 token
- token 不内置
- 用户安装 skill 后，需自行配置 `NOAH_MARKET_APIKEY`
- 不再使用“market 内置 token 可直接体验”的旧口径
- trade 不再以 `groupNo` 作为对外主鉴权口径

### 对用户说明必须包含
- 安装完成 skill 后，仍需提供通用 token
- “市场与查询”两类能力共用同一个 token
- 两种配置方式：
  1. 把 token 发给 AI，由 AI 帮忙配置
  2. 手动修改本地配置文件中的 `NOAH_MARKET_APIKEY`
     - 例如 OpenClaw 默认路径：`~/.openclaw/.secrets/noah-market.env`

---

## 三、环境规则

### 生产环境
- market：`https://securities-open-api.noahgroup.com`
- trade：`https://stock-open-api.noahgroup.com`

### 测试环境
- market：`https://securities-open-api.t2.test.noahgrouptest.com`
- trade：`https://stock-open-api.t2.test.noahgrouptest.com`

注意：
- market 与 trade 的域名是分开的
- 不能把 market 域名套到 trade 上
- 不能把 trade 域名套到 market 上

---

## 四、接口开发准则

- 必须严格按最新 openapi 文档实现
- 文档改了以后，要同步修改：
  - client
  - CLI
  - `SKILL.md`
  - references
  - README / INSTALL / release 文档
- enum / 枚举值必须严格来自协议文档或 enum 文件
- 不能按语义猜测枚举值
- 新参数规则必须实测验证，尤其是：
  - `market` 必填
  - 历史查询日期范围必填
  - push data 请求体参数变化

---

## 五、标准发布流程

固定顺序如下：

### 1. 修改代码
- 更新 skill 代码
- 更新协议 reference
- 更新 CLI / client / formatter / summary 逻辑

### 2. 更新文档
至少同步以下文件：
- `README.md`
- `INSTALL.md`
- `release/noah-install.md`
- `release/index.html`
- 各模块 `SKILL.md`
- `references/current-availability.md`
- `references/usage-guide.md`
- `references/auth-and-preflight.md`
- 其他与用户感知直接相关的 references

### 3. 联调验证
- 主干接口必须做实际调用验证
- 不只看文档是否存在
- 不只看代码是否能跑
- 页面展示示例优先使用真实测试数据，不要写空话

### 4. 生成双环境交付物
必须同时生成：
- 生产版
- 测试版

每套都必须有三层交付物：
- 页面 / index
- 主安装文档 / md
- ZIP 安装包

### 5. 检查最终交付物
不能只检查仓库源文件，必须检查用户实际会拿到的内容：
- 页面
- md
- zip

要求三者：
- 同版本
- 同口径
- 同目录结构
- 同环境链接

### 6. 发布
- git commit
- git push
- ClawHub publish
- 记录版本号

### 7. 如需要，同步全局 skill
同步目标：
- `~/.openclaw/skills/noah-stock-market`
- `~/.openclaw/skills/noah-stock-trade`

同步后做：
- 脚本编译检查
- 最小调用验证

---

## 六、生产环境交付规则

### 文件命名
- 页面：`index.html`
- 主安装文档：`noah-install.md`
- ZIP：`noah-agent-skills-installer.zip`

### ZIP 根目录结构
必须固定为：

```text
noah-agent-skills-installer/
+-- search-skills/
+-- release/
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

### ZIP 内 skill 目录
放在：

```text
noah-agent-skills-installer/search-skills/
```

当前正常应包含：
- `noah-stock-market/`
- `noah-stock-trade/`

### ZIP 内 release 目录
放在：

```text
noah-agent-skills-installer/release/
```

应包含：
- `index.html`
- `noah-install.md`

---

## 七、测试环境交付规则

### 文件命名
测试环境所有对外交付文件名统一带 `-test`：
- 页面：`index-test.html`
- 主安装文档：`noah-install-test.md`
- ZIP：`noah-agent-skills-installer-test.zip`

### ZIP 根目录结构
测试环境根目录也必须带 `-test`：

```text
noah-agent-skills-installer-test/
+-- search-skills/
+-- release/
+-- README.md
+-- INSTALL.md
+-- install_openclaw_skills.sh
+-- noah-market.env.example
```

### ZIP 内 release 目录
应包含：
- `index-test.html`
- `noah-install-test.md`

### 链接规则
测试环境 index 页面安装链接必须指向：
- `https://securities-open-api.t2.test.noahgrouptest.com/noah-install-test.md`

测试环境 md 文档中的 ZIP 下载链接必须指向：
- `https://securities-open-api.t2.test.noahgrouptest.com/noah-agent-skills-installer-test.zip`

### unzip / cd 命令规则
测试环境 md 文档中的命令必须与 `-test` 目录匹配，例如：

```bash
unzip noah-agent-skills-installer-test.zip
cd noah-agent-skills-installer-test
```

不能出现：
- ZIP 文件名带 `-test`
- 但 `cd` 仍然进入 `noah-agent-skills-installer`

---

## 八、页面生成规则

### 页面收口原则
页面尽量只保留高层信息：
- 核心能力概览
- Skill 实例
- Token 配置说明
- 必要的安装入口

避免堆叠：
- 大段底层接口列表
- 冗余安装模块说明
- 与主安装文档重复的大块内容

### 文案统一规则
如不直接强调 `market + trade` 模块名，可以统一使用：
- `市场与查询`

### Skill 实例规则
- 市场能力示例 + 查询能力示例都要有
- 交易示例尽量使用真实测试数据
- 避免“已返回相关信息”这类空话

### Token 配置说明规则
页面中要明确写出：
- 安装完成 skill 后仍需提供通用 token
- 两类能力共用同一个 token
- 两种配置方式
- 配置文件路径示例（如 OpenClaw 的 `.secrets/noah-market.env`）

### 多币种资产展示规则
当页面、skill 或文档涉及持仓、证券资产、总资产展示时：
- 不对不同计价货币（如 HKD、USD、CNY）的金额直接加总
- 如用户问“总资产是多少”，默认按币种分别列出，并说明“以下为各货币资产，未做汇率换算”
- 如果接口本身返回换算后的汇总值，可原样展示，但必须注明“该汇总值由接口按当日汇率换算”
- 如果用户明确要求折算，必须说明需要汇率依据，并引导用户提供汇率口径，或使用行情数据作为换算依据

---

## 九、页面脚本规则

这是强制检查项。

### 1. 英文文案单引号转义
如果页面 JS 中使用单引号字符串，英文文案中的 `'` 必须转义为 `\'`。

否则会导致：
- 整段脚本 syntax error
- 按钮事件无法绑定
- 页面看起来正常但交互全部失效

### 2. 生成后必须校验 JS 语法
每次生成页面后，必须至少做一次脚本语法校验。

### 3. 复制按钮兼容性
复制按钮不能只依赖：
- `navigator.clipboard.writeText`

应有降级方案，例如：
- `document.execCommand('copy')`

因为本地 `file://` 打开或某些受限 WebView 环境下，clipboard API 可能受限制。

### 4. 不能只看视觉结果
页面“看起来对”不算完成。
必须确认：
- 脚本无语法错误
- 按钮事件可执行
- 交互逻辑可用

---

## 十、全局 skill 同步规则

如果本轮变更需要让本机立即可用，则除了仓库内容外，还要同步到：
- `~/.openclaw/skills/noah-stock-market`
- `~/.openclaw/skills/noah-stock-trade`

同步后必须至少执行：
- `python3 -m py_compile ...`
- 一个最小验证命令

避免出现：
- 仓库最新版已改
- 全局 skill 仍然是旧版本

---

## 十一、最终验收清单

每次发布前至少确认：

- [ ] 代码已更新
- [ ] README / INSTALL / SKILL / references 已同步
- [ ] 生产环境页面 / md / zip 已生成
- [ ] 测试环境页面 / md / zip 已生成
- [ ] ZIP 根目录结构符合标准
- [ ] 测试环境文件名与目录名带 `-test`
- [ ] 页面安装链接与 md 中 ZIP 链接正确
- [ ] market / trade base URL 环境口径正确
- [ ] token 说明正确，明确“不内置”
- [ ] 页面 JS 无语法错误
- [ ] 复制按钮或交互已验证
- [ ] git commit / push 完成
- [ ] ClawHub publish 完成
- [ ] 如需要，已同步全局 skill

---

## 十二、禁止事项

以下行为不要再发生：

- 用临时 ZIP 目录结构替代正式标准目录结构
- 测试环境文件名加了 `-test`，但目录名 / 命令 / 链接没一起改
- 文档说一套、ZIP 内容是另一套
- 页面说支持某能力，但示例里仍是旧能力或空话
- 页面 JS 因未转义单引号而报错
- 仓库更新了，但全局 skill 未同步
- 只看仓库文件，不检查用户实际打开的页面、md、zip

---

## 十三、推荐执行顺序（简版）

1. 改代码
2. 改文档
3. 联调接口
4. 出生产版三件套
5. 出测试版三件套
6. 校验页面 / md / zip
7. 校验页面 JS 与交互
8. git commit / push
9. ClawHub publish
10. 同步全局 skill（如需要）

---

## 备注

如未来再扩模块或改交付方式，应优先更新本文件，再改实现与发布流程。
