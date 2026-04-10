#!/usr/bin/env python3
import json
import re
import sys

from run_query import run
from normalize_symbol import normalize_symbol


def infer_intent(text: str) -> str:
    s = text.lower()
    if any(x in text for x in ['资金流向', '主力资金']) or 'flow' in s:
        return 'capital_flow'
    if any(x in text for x in ['摆盘', '盘口', '买卖盘']) or 'orderbook' in s:
        return 'orderbook'
    if any(x in text for x in ['市场状态', '开盘', '收盘', '交易状态']) or 'state' in s:
        return 'market_state'
    if any(x in text.lower() for x in ['日k', '周k', '月k', '分钟k', 'k线', '5分钟k', '15分钟k', '30分钟k', '60分钟k']) or 'kline' in s:
        return 'kline'
    if '分时' in text or ('走势' in text and 'k' not in s):
        return 'intraday'
    if any(x in text for x in ['基础信息', '上市日期', '每手', '退市']) or 'basic' in s:
        return 'basicinfo'
    if any(x in text for x in ['价格', '多少钱', '最新价', '行情']) or 'price' in s or 'quote' in s:
        return 'snapshot'
    return 'snapshot'


def infer_symbol(text: str) -> str:
    candidates = re.findall(r'(HK-\d{5}|US-[A-Z][A-Z0-9.-]{0,9}|\b\d{5}\b|\b[A-Z]{1,5}\b)', text.upper())
    if candidates:
        return normalize_symbol(candidates[0]) or candidates[0]
    for name in ['腾讯控股', '腾讯', '苹果', '英伟达', '特斯拉']:
        if name in text:
            return normalize_symbol(name) or name
    return text.strip()


def infer_kwargs(text: str):
    kwargs = {}
    if '日k' in text.lower():
        kwargs['ktype'] = 'K_DAY'
    elif '周k' in text.lower():
        kwargs['ktype'] = 'K_WEEK'
    elif '月k' in text.lower():
        kwargs['ktype'] = 'K_MON'
    elif '5分钟' in text or '5分k' in text.lower():
        kwargs['ktype'] = 'K_5_M'
    elif '15分钟' in text or '15分k' in text.lower():
        kwargs['ktype'] = 'K_15_M'
    elif '30分钟' in text or '30分k' in text.lower():
        kwargs['ktype'] = 'K_30_M'
    elif '60分钟' in text or '60分k' in text.lower():
        kwargs['ktype'] = 'K_60_M'

    m = re.search(r'最近\s*(\d+)\s*根', text)
    if m:
        kwargs['num'] = int(m.group(1))
    else:
        m2 = re.search(r'(\d+)\s*根', text)
        if m2:
            kwargs['num'] = int(m2.group(1))
    return kwargs


def main(text: str):
    intent = infer_intent(text)
    symbol = infer_symbol(text)
    kwargs = infer_kwargs(text)
    result = run(intent, symbol, **kwargs)
    return {
        'intent': intent,
        'symbol': symbol,
        'kwargs': kwargs,
        'result': result,
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: route_query.py <free text>', file=sys.stderr)
        sys.exit(2)
    text = ' '.join(sys.argv[1:])
    print(json.dumps(main(text), ensure_ascii=False, indent=2, default=str))
