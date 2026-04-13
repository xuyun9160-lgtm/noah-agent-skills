# Current Availability

## Trade Module Capability Status

| Capability | Status | Notes |
|---|---|---|
| Account Info | Scripted / Verified | 已并入 `noah-stock-trade`，CLI `account-info` 已联调成功 |
| Positions | Scripted / Verified | 已并入 `noah-stock-trade`，CLI `positions` 已联调成功 |
| Securities Asset | Scripted / Verified | 已并入 `noah-stock-trade`，CLI `sec-asset` 已联调成功 |
| Securities Capital Flow | Scripted / Verified | 已并入 `noah-stock-trade`，CLI `sec-capital-flow` 已联调成功；需日期范围时更稳定 |
| Stock Amount (Buy/Sell Availability) | Scripted / Verified | CLI `stock-amount` 已联调成功；需 `code` + `order_type` |
| Margin Max Buy Amount | Scripted / Verified | CLI `max-enable-buy-amt` 已联调成功；需 `code` + `order_type` + `entrust_price` |
| Today Deal List | Scripted / Verified | CLI `today-deals` 已联调成功 |
| History Deal List | Scripted / Verified | CLI `history-deals` 已联调成功；需 `start_date` + `end_date` |
| Today Unfinished Order List | Scripted / Verified | 对应 `/trade/get_today_order_list`，CLI `unfinished-orders` 已联调成功 |
| Today Order List | Routed but inconsistent | `/trade/get_order_list` 当前测试环境返回与 OpenAPI 文档不一致 |
| Finished Order List | Routed but inconsistent | `/trade/get_finished_order_list` 当前测试环境返回与 OpenAPI 文档不一致 |
| Order Detail | Routed but server-side error | `/trade/get_order_detail` 当前传入测试参数会返回服务端 500 |
| Order Fee Detail | Routed but server-side error | `/trade/get_order_fee_detail` 当前传入测试参数会返回服务端 500 |
| Order Fee Query | Scripted / Verified | CLI `fee-estimate` 已联调成功；需 POST + JSON body |
| Push Data Query | Ready in OpenAPI / Not yet scripted | 文档已定义，尚未正式接入 |
| Place Order | Deferred / Not enabled | 当前阶段不对外承诺写操作 |
| Modify Order | Deferred / Not enabled | 当前阶段不对外承诺写操作 |
| Cancel Order | Deferred / Not enabled | 当前阶段不对外承诺写操作 |

## Access Prerequisites

当前测试口径下，trade 模块使用：
- Base URL：`https://stock-open-api.t2.test.noahgrouptest.com`
- Header：`groupNo: 100636524`

推荐本地变量名：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

## Notes

- 当前 `noah-stock-trade` 已吸收原 `noah-stock-portfolio` 的账户、持仓、资产、资金流水能力。
- 当前状态中的 `Scripted / Verified` 表示：
  - 脚本入口已存在
  - 已在当前测试环境完成至少一轮实际联调
- `Routed but inconsistent` 表示：
  - OpenAPI 文档已有定义
  - CLI / client 已接入
  - 但当前测试环境返回行为与文档不一致
- `Routed but server-side error` 表示：
  - 路由和参数链路已打到目标接口
  - 但当前测试环境返回服务端异常，仍需后端或接口实现侧确认
- 交易模块使用的证券代码格式为 `MARKET.CODE`，例如 `HK.00700`、`US.AAPL`。
- 后续可继续补充与 market 模块代码格式（`HK-00700` / `US-AAPL`）之间的统一展示转换。
