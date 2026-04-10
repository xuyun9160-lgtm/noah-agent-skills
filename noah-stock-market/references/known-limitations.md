# Known Limitations

基于当前真实 smoke test，以下情况已确认：

## 已验证可用
- `/quotes/get_market_snapshot`
- `/infos/get_market_state`
- `/quotes/get_cur_kline`
- `/quotes/get_rt_data`
- `/quotes/get_order_book`
- `/infos/get_capital_flow`
- `/quote/get_stock_basicinfo`

## 当前环境暂不支持或未验证通过
- `/quote/get_plate_list`
  - 返回：HTTP 200
  - 业务结果：`success=false`
  - message：`生产环境暂不支持`

- `/derivatives/get_option_chain`
  - 返回：HTTP 200
  - 业务结果：`success=false`
  - message：`生产环境暂不支持`

- `/derivatives/get_option_expiration_date`
  - 返回：HTTP 404
  - 业务返回 message 不可靠，当前调用方式未验证通过
  - 文档描述显示该接口更偏向衍生权证 / uCode 场景，未必适合直接传正股代码

- 美股 K 线（如 `US-AAPL`, `US-NVDA`）
  - 自然语言路由已能正确识别为 `kline`
  - 但当前接口调用返回 HTTP 404
  - 初步判断：问题更可能在后端环境、代码格式或市场支持范围，而不是前端路由逻辑

## Implementation Guidance

- 对未验证通过的能力，不要在主路径里强承诺。
- 如果用户问到这些能力，可以尝试调用；若失败，直接说明当前环境暂不支持，而不是误导成“没有数据”。
- 对 404 场景，优先解释为“当前环境下该标的或该参数暂不可用”，不要直接把原始 message 当成用户提示。
- 后续如环境开放或拿到正确入参规范，再升级这些能力为正式支持。
