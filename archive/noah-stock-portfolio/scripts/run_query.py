#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, List

from quote_client import NoahTradeClient
from format_portfolio_text import format_account_info, format_positions, format_sec_asset, format_capital_flow

DETAIL_LIMIT = 10


def summarize_account_info(item: Dict[str, Any]) -> Dict[str, Any]:
    return item or {}


def summarize_positions(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    shown = items[:DETAIL_LIMIT]
    return {'count': len(items), 'items': shown, 'truncated': len(items) > DETAIL_LIMIT}


def summarize_sec_asset(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {'count': len(items), 'items': items[:DETAIL_LIMIT], 'truncated': len(items) > DETAIL_LIMIT}


def summarize_capital_flow(data: Dict[str, Any]) -> Dict[str, Any]:
    records = (data or {}).get('records') or []
    return {'count': len(records), 'items': records[:DETAIL_LIMIT], 'truncated': len(records) > DETAIL_LIMIT, 'last_update_time': (data or {}).get('last_update_time')}


def build_params(intent: str, symbol: str = '', **kwargs) -> Dict[str, Any]:
    if intent == 'account_info':
        return {}
    if intent == 'positions':
        return {'code': symbol} if symbol else {}
    if intent == 'sec_asset':
        return {}
    if intent == 'sec_capital_flow':
        params = {}
        for k in ['start_date', 'end_date', 'business_type', 'fund_direction', 'page', 'page_size', 'last_id', 'record_last_id', 'trade_code', 'unique_code']:
            if kwargs.get(k) not in (None, ''):
                params[k] = kwargs[k]
        return params
    raise ValueError(f'unsupported intent: {intent}')


def run(intent: str, symbol: str = '', **kwargs) -> Dict[str, Any]:
    client = NoahTradeClient()
    path_map = {
        'account_info': '/trade/get_account_info',
        'positions': '/trade/get_positions',
        'sec_asset': '/trade/get_sec_asset',
        'sec_capital_flow': '/trade/get_sec_capital_flow',
    }
    if intent not in path_map:
        return {'ok': False, 'message': f'unsupported intent: {intent}', 'symbol': symbol}
    params = build_params(intent, symbol, **kwargs)
    result = client.get(path_map[intent], params)
    out = {'ok': result['ok'], 'http_status': result['http_status'], 'message': result.get('message'), 'intent': intent, 'params': params}
    if not result['ok']:
        status = result.get('http_status')
        if status == 404:
            human = '当前环境下，未查询到匹配的账户或记录（接口返回 404）。'
        elif status in (401, 403):
            human = '当前交易接口访问失败，请检查本地配置与 groupNo。'
        else:
            human = f'查询失败：{result.get("message") or "未知错误"}'
        out['text'] = human
        return out
    data = result.get('data')
    if intent == 'account_info' and isinstance(data, dict):
        summary = summarize_account_info(data)
        out['summary'] = summary
        out['text'] = format_account_info(summary)
    elif intent == 'positions' and isinstance(data, list):
        summary = summarize_positions(data)
        out['summary'] = summary
        out['text'] = format_positions(summary)
    elif intent == 'sec_asset' and isinstance(data, list):
        summary = summarize_sec_asset(data)
        out['summary'] = summary
        out['text'] = format_sec_asset(summary)
    elif intent == 'sec_capital_flow' and isinstance(data, dict):
        summary = summarize_capital_flow(data)
        out['summary'] = summary
        out['text'] = format_capital_flow(summary)
    else:
        out['text'] = '查询成功，但当前没有可展示的数据。'
    return out


def parse_kwargs(argv) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {}
    for item in argv:
        if '=' in item:
            k, v = item.split('=', 1)
            kwargs[k] = v
    return kwargs


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: run_query.py <intent> [symbol] [key=value ...]', file=sys.stderr)
        sys.exit(2)
    intent = sys.argv[1]
    symbol = sys.argv[2] if len(sys.argv) >= 3 and '=' not in sys.argv[2] else ''
    extra = sys.argv[3:] if symbol else sys.argv[2:]
    kwargs = parse_kwargs(extra)
    result = run(intent, symbol, **kwargs)
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
