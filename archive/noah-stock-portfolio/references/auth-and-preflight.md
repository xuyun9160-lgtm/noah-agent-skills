# Auth and Preflight

## Current Access Assumption
当前交易侧 / portfolio 模块先按以下测试接入前提理解：
- Base URL：`https://stock-open-api.t2.test.noahgrouptest.com`
- Request Header：`groupNo: 100636524`

当前阶段：
- 暂不需要单独 token
- 通过请求头中的 `groupNo` 标识交易账户分组

## Recommended Local Config Names
为了和 market 模块隔离，建议本地统一使用：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

示例：

```bash
NOAH_TRADE_API_BASE_URL=https://stock-open-api.t2.test.noahgrouptest.com
NOAH_TRADE_GROUP_NO=100636524
```

## Preflight Checklist
1. 确认交易侧 Base URL 已配置。
2. 确认 `groupNo` 已配置，并放入请求头。
3. 确认当前调用的是交易 / 账户相关接口，而不是行情接口。
4. 确认证券代码格式使用交易侧约定：`MARKET.CODE`，例如 `HK.00700`、`US.AAPL`。
5. 若查询失败，优先区分：
   - Base URL 是否正确
   - `groupNo` 是否正确
   - 当前环境是否开放该接口

## Notes
- 这套接入前提与 market 模块不同，不应复用 `NOAH_MARKET_APIKEY`。
- 后续如交易侧正式要求 token，再补充新的鉴权规则。
