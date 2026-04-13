# Usage Guide

## 1. What This Module Is For
`noah-stock-trade` 当前用于：
- 账户信息查询
- 持仓查询
- 证券资产查询
- 证券资金流水查询
- 当日未完成订单查询
- 当日成交查询
- 历史成交查询
- 订单详情查询
- 订单费用查询
- 下单前费用预估
- 可买可卖数量查询
- 融资最大可买数量查询

当前阶段**不用于**：
- 真实下单
- 改单
- 撤单

## 2. Access Prerequisites
当前测试口径下，需要：
- `NOAH_TRADE_API_BASE_URL`
- `NOAH_TRADE_GROUP_NO`

当前交易侧测试前提：
- Base URL：`https://stock-open-api.t2.test.noahgrouptest.com`
- Header：`groupNo: 100636524`

## 3. Suitable Query Scenarios
适合的场景包括：
- 看账户信息
- 查当前持仓
- 看证券资产
- 查资金流水
- 看今天的未完成订单
- 看今天的成交
- 查历史成交
- 看某笔订单详情
- 看某笔订单费用
- 查询某只股票可买可卖数量
- 查询某只股票融资最大可买数量
- 查询某笔拟下单的预估费用

## 4. Recommended CLI Commands
### 账户 / 持仓 / 资产
```bash
python3 scripts/noah_trade_cli.py account-info
python3 scripts/noah_trade_cli.py positions
python3 scripts/noah_trade_cli.py positions --symbol HK.00700
python3 scripts/noah_trade_cli.py sec-asset
python3 scripts/noah_trade_cli.py sec-capital-flow --start-date 20260401 --end-date 20260413
```

### 订单 / 成交 / 费用 / 可交易能力
```bash
python3 scripts/noah_trade_cli.py unfinished-orders
python3 scripts/noah_trade_cli.py today-deals
python3 scripts/noah_trade_cli.py history-deals --start-date 20260401 --end-date 20260413
python3 scripts/noah_trade_cli.py fee-estimate --symbol HK.00700 --side BUY --order-type LIMIT --price 320 --qty 100
python3 scripts/noah_trade_cli.py stock-amount --symbol HK.00700 --order-type LO
python3 scripts/noah_trade_cli.py max-enable-buy-amt --symbol HK.00700 --order-type LO
```

> 注意：当前 `max-enable-buy-amt` 实际联调时还需要额外价格参数，后续脚本将继续对齐到服务端要求。

## 5. Symbol Format Note
交易接口当前使用的证券代码格式是：
- `HK.00700`
- `US.AAPL`

这与 market 模块常用的：
- `HK-00700`
- `US-AAPL`

不同，脚本层已开始做统一转换，但用户态展示仍可继续优化。

## 6. Order Status Note
订单查询结果中可能同时包含：
- OpenAPI 统一状态
- sec-trade 原始状态码

建议优先向最终用户展示统一状态；如需补充解释，再结合：
- `references/order-status-mapping.md`

## 7. Current Limitations
当前已知限制包括：
- 写操作接口（下单 / 改单 / 撤单）当前不对外承诺
- `/trade/get_order_list` 与 `/trade/get_finished_order_list` 在当前测试环境中的行为与 OpenAPI 文档不一致
- `/trade/get_order_detail` 与 `/trade/get_order_fee_detail` 当前测试环境会返回服务端 500
- `max_enable_buy_amt` 当前服务端要求的参数比已有文档/初始理解更严格，至少需要 `entrust_price`

## 8. Relationship with Other Modules
- 行情 / K线 / 分时 / 摆盘 → `noah-stock-market`
- 条件选股 → 后续可并入 `noah-stock-market` 或单独保留
- 原 `noah-stock-portfolio` 能力已逐步合并到本模块
