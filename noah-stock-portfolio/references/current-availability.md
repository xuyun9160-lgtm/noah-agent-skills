# Current Availability

## Portfolio Module Capability Status

| Capability | Status | Notes |
|---|---|---|
| Account Info | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_account_info` 接口定义，但脚本尚未接入 |
| Positions | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_positions` 接口定义，但脚本尚未接入 |
| Securities Asset | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_sec_asset` 接口定义，但脚本尚未接入 |
| Securities Capital Flow | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_sec_capital_flow` 接口定义，但脚本尚未接入 |
| Portfolio Summary | Planned | 后续由账户、持仓、资产接口组合生成 |
| PnL / Allocation Summary | Planned | 后续基于持仓与资产结果做进一步整理 |

## Access Prerequisites

当前测试口径下，portfolio 模块使用：
- Base URL：`https://stock-open-api.t2.test.noahgrouptest.com`
- Header：`groupNo: 100636524`

推荐本地变量名：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

## Notes

- 当前状态中的“Ready in OpenAPI / Not yet scripted”表示：
  - 接口已经存在于交易 OpenAPI 中
  - 模块边界已明确
  - 但本仓库中尚未完成对应脚本接入与用户态输出
- Portfolio 模块当前只面向只读账户 / 持仓 / 资产 / 资金流水场景。
- Portfolio 模块使用的证券代码格式为 `MARKET.CODE`，例如 `HK.00700`、`US.AAPL`。
- 后续需要补充与 market 模块代码格式（`HK-00700` / `US-AAPL`）之间的统一转换。
