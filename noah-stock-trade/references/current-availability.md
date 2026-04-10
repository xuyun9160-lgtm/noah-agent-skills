# Current Availability

## Trade Module Capability Status

| Capability | Status | Notes |
|---|---|---|
| Stock Amount (Buy/Sell Availability) | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_stock_amount` 接口定义，但脚本尚未接入 |
| Margin Max Buy Amount | Ready in OpenAPI / Not yet scripted | 已有 `/trade/max_enable_buy_amt` 接口定义，但脚本尚未接入 |
| Today Order List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_order_list` 接口定义，但脚本尚未接入 |
| Unfinished Order List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_today_order_list` 接口定义，但脚本尚未接入 |
| History Order List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_history_order_list` 接口定义，但脚本尚未接入 |
| Today Deal List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_today_deal_list` 接口定义，但脚本尚未接入 |
| History Deal List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_history_deal_list` 接口定义，但脚本尚未接入 |
| Finished Order List | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_finished_order_list` 接口定义，但脚本尚未接入 |
| Order Detail | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_order_detail` 接口定义，但脚本尚未接入 |
| Order Fee Detail | Ready in OpenAPI / Not yet scripted | 已有 `/trade/get_order_fee_detail` 接口定义，但脚本尚未接入 |
| Order Fee Query | Ready in OpenAPI / Not yet scripted | 已有 `/trade/order_fee_query` 接口定义，但脚本尚未接入 |
| Push Data Query | Ready in OpenAPI / Not yet scripted | 已有 `/trade/query_push_data` 接口定义，但脚本尚未接入 |
| Place Order | Deferred / TEMP DISABLED | 当前 OpenAPI 中仍为 TEMP DISABLED，不纳入一期主承诺 |
| Modify Order | Deferred / TEMP DISABLED | 当前 OpenAPI 中仍为 TEMP DISABLED，不纳入一期主承诺 |
| Cancel Order | Deferred / TEMP DISABLED | 当前 OpenAPI 中仍为 TEMP DISABLED，不纳入一期主承诺 |

## Access Prerequisites

当前测试口径下，trade 模块使用：
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
- 当前一期先聚焦只读交易查询与交易前评估能力。
- 当前写操作（下单 / 改单 / 撤单）不应对外承诺。
- 交易模块使用的证券代码格式为 `MARKET.CODE`，例如 `HK.00700`、`US.AAPL`。
- 后续需要补充与 market 模块代码格式（`HK-00700` / `US-AAPL`）之间的统一转换。
