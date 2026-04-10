#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, Optional

from quote_client import NoahQuoteClient
from normalize_symbol import normalize_symbol
from summarize_market import (
    summarize_basicinfo,
    summarize_capital_flow,
    summarize_intraday,
    summarize_kline,
    summarize_market_state,
    summarize_orderbook,
    summarize_snapshot,
)
from format_market_text import (
    format_basicinfo,
    format_capital_flow,
    format_intraday,
    format_kline,
    format_market_state,
    format_orderbook,
    format_snapshot,
)


def build_params(intent: str, symbol: str, **kwargs) -> Dict[str, Any]:
    if intent == 'snapshot':
        return {'code_list': symbol}
    if intent == 'market_state':
        return {'code_list': symbol}
    if intent == 'intraday':
        return {'code': symbol}
    if intent == 'kline':
        return {
            'code': symbol,
            'num': int(kwargs.get('num', 5)),
            'ktype': kwargs.get('ktype', 'K_DAY'),
            'autype': kwargs.get('autype', 'NONE'),
        }
    if intent == 'orderbook':
        return {'code': symbol, 'num': int(kwargs.get('num', 5))}
    if intent == 'capital_flow':
        return {'stock_code': symbol, 'num': int(kwargs.get('num', 5))}
    if intent == 'basicinfo':
        return {'market': symbol.split('-')[0], 'code_list': symbol}
    raise ValueError(f'unsupported intent: {intent}')


def run(intent: str, raw_symbol: str, **kwargs) -> Dict[str, Any]:
    symbol = normalize_symbol(raw_symbol) or raw_symbol
    client = NoahQuoteClient()
    supported = {'snapshot', 'market_state', 'intraday', 'kline', 'orderbook', 'capital_flow', 'basicinfo'}
    if intent not in supported:
        return {'ok': False, 'message': f'unsupported intent: {intent}', 'symbol': symbol}

    path_map = {
        'snapshot': '/quotes/get_market_snapshot',
        'market_state': '/infos/get_market_state',
        'intraday': '/quotes/get_rt_data',
        'kline': '/quotes/get_cur_kline',
        'orderbook': '/quotes/get_order_book',
        'capital_flow': '/infos/get_capital_flow',
        'basicinfo': '/quote/get_stock_basicinfo',
    }

    params = build_params(intent, symbol, **kwargs)
    result = client.get(path_map[intent], params)
    out = {
        'ok': result['ok'],
        'http_status': result['http_status'],
        'message': result.get('message'),
        'symbol': symbol,
        'intent': intent,
        'params': params,
    }

    if not result['ok']:
        msg = result.get('message') or '未知错误'
        status = result.get('http_status')
        if status == 404:
            human = '当前环境下，该标的或该查询参数暂不可用（接口返回 404）。'
        elif status in (401, 403):
            human = '鉴权失败或权限不足，请检查本地 token 配置。'
        elif msg == '生产环境暂不支持':
            human = '这个能力接口已定义，但当前环境暂不支持。'
        else:
            human = f'查询失败：{msg}'
        out['text'] = human
        out['error_hint'] = human
        return out

    data = result.get('data')
    if intent == 'snapshot' and isinstance(data, list) and data:
        summary = summarize_snapshot(data[0])
        out['summary'] = summary
        out['text'] = format_snapshot(summary)
    elif intent == 'market_state' and isinstance(data, list):
        summary = summarize_market_state(data)
        out['summary'] = summary
        out['text'] = format_market_state(summary)
    elif intent == 'intraday' and isinstance(data, list):
        summary = summarize_intraday(data)
        out['summary'] = summary
        out['text'] = format_intraday(summary)
    elif intent == 'kline' and isinstance(data, list):
        summary = summarize_kline(data)
        out['summary'] = summary
        out['text'] = format_kline(summary)
    elif intent == 'orderbook' and isinstance(data, dict):
        summary = summarize_orderbook(data)
        out['summary'] = summary
        out['text'] = format_orderbook(summary)
    elif intent == 'capital_flow' and isinstance(data, list):
        detail = str(kwargs.get('detail', 'false')).lower() in ('1','true','yes','y')
        summary = summarize_capital_flow(data, detail=detail)
        out['summary'] = summary
        out['text'] = format_capital_flow(summary, detail=detail)
    elif intent == 'basicinfo' and isinstance(data, list):
        summary = summarize_basicinfo(data)
        out['summary'] = summary
        out['text'] = format_basicinfo(summary)
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
    if len(sys.argv) < 3:
        print('Usage: run_query.py <intent> <symbol> [key=value ...]', file=sys.stderr)
        sys.exit(2)
    kwargs = parse_kwargs(sys.argv[3:])
    result = run(sys.argv[1], sys.argv[2], **kwargs)
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
