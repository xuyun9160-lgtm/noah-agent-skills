#!/usr/bin/env python3
from typing import Any, Dict, List, Optional


MARKET_STATE_MAP = {
    'AUCTION': '盘前竞价',
    'WAITING_OPEN': '等待开盘',
    'MORNING': '早盘交易中',
    'REST': '午间休市',
    'AFTERNOON': '午盘交易中',
    'CLOSED': '已收盘',
    'PRE_MARKET_BEGIN': '美股盘前交易中',
    'PRE_MARKET_END': '美股盘前结束',
    'AFTER_HOURS_BEGIN': '美股盘后交易中',
    'AFTER_HOURS_END': '美股盘后结束',
    'OVERNIGHT': '夜盘交易中',
    'HK_CAS': '港股盘后竞价',
}


def normalize_symbol(code: Optional[str]) -> Optional[str]:
    if not code:
        return code
    if code.startswith('HK-') or code.startswith('US-'):
        return code
    if code.isdigit() and len(code) == 5:
        return f'HK-{code}'
    if code.replace('.', '').replace('-', '').isalnum() and not code.isdigit():
        return f'US-{code.replace("US-", "").replace("US.", "")}' if not code.startswith('US') else code.replace('US.', 'US-')
    return code


def _pct(last_price, prev_close):
    try:
        if prev_close in (None, 0):
            return None
        return (float(last_price) - float(prev_close)) / float(prev_close) * 100
    except Exception:
        return None


def _delta(last_price, prev_close):
    try:
        if last_price is None or prev_close is None:
            return None
        return float(last_price) - float(prev_close)
    except Exception:
        return None


def summarize_snapshot(item: Dict[str, Any]) -> Dict[str, Any]:
    last_price = item.get('last_price')
    prev_close = item.get('prev_close_price')
    pct = _pct(last_price, prev_close)
    delta = _delta(last_price, prev_close)
    return {
        'symbol': normalize_symbol(item.get('code')),
        'name': item.get('name'),
        'last_price': last_price,
        'change_value': round(delta, 2) if delta is not None else None,
        'change_pct': round(pct, 2) if pct is not None else None,
        'open_price': item.get('open_price'),
        'high_price': item.get('high_price'),
        'low_price': item.get('low_price'),
        'volume': item.get('volume'),
        'turnover': item.get('turnover'),
        'update_time': item.get('data_time') or item.get('update_time'),
        'suspension': item.get('suspension'),
    }


def summarize_market_state(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            'symbol': normalize_symbol(x.get('code')),
            'name': x.get('stock_name') or x.get('name'),
            'market_state': x.get('market_state'),
            'market_state_text': MARKET_STATE_MAP.get(x.get('market_state'), x.get('market_state')),
        }
        for x in items
    ]


def summarize_kline(items: List[Dict[str, Any]], detail: bool = False) -> Dict[str, Any]:
    if not items:
        return {'count': 0, 'latest': None, 'highest': None, 'lowest': None, 'items': []}
    closes = [x.get('close') for x in items if x.get('close') is not None]
    normalized_items = []
    for x in items:
        row = dict(x)
        row['code'] = normalize_symbol(row.get('code'))
        normalized_items.append(row)
    latest = normalized_items[0]
    result = {
        'count': len(normalized_items),
        'latest': latest,
        'highest': max(closes) if closes else None,
        'lowest': min(closes) if closes else None,
    }
    result['items'] = normalized_items if detail else []
    return result


def summarize_intraday(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not items:
        return {'count': 0, 'latest': None}
    latest = dict(items[-1])
    latest['code'] = normalize_symbol(latest.get('code'))
    return {
        'count': len(items),
        'latest': latest,
        'avg_price': latest.get('avg_price'),
        'last_close': latest.get('last_close'),
        'volume': latest.get('volume'),
        'turnover': latest.get('turnover'),
    }


def summarize_orderbook(item: Dict[str, Any]) -> Dict[str, Any]:
    bid = (item.get('bid') or [])
    ask = (item.get('ask') or [])
    best_bid = bid[0] if bid else None
    best_ask = ask[0] if ask else None
    return {
        'symbol': normalize_symbol(item.get('code')),
        'name': item.get('name'),
        'best_bid': best_bid,
        'best_ask': best_ask,
        'bid_levels': len(bid),
        'ask_levels': len(ask),
        'recv_time_bid': item.get('svr_recv_time_bid'),
        'recv_time_ask': item.get('svr_recv_time_ask'),
    }


def summarize_capital_flow(items: List[Dict[str, Any]], detail: bool = False) -> Dict[str, Any]:
    if not items:
        return {'count': 0, 'latest': None, 'items': []}

    def _is_zero_row(x: Dict[str, Any]) -> bool:
        vals = [x.get('in_flow'), x.get('super_in_flow'), x.get('big_in_flow'), x.get('mid_in_flow'), x.get('sml_in_flow')]
        cleaned = [0 if v is None else float(v) for v in vals]
        return all(v == 0 for v in cleaned)

    trimmed = list(items)
    while trimmed and _is_zero_row(trimmed[-1]):
        trimmed.pop()

    effective = trimmed if trimmed else items
    latest = effective[-1]
    result = {
        'count': len(effective),
        'raw_count': len(items),
        'latest': {
            'in_flow': latest.get('in_flow'),
            'main_in_flow': latest.get('main_in_flow'),
            'super_in_flow': latest.get('super_in_flow'),
            'big_in_flow': latest.get('big_in_flow'),
            'mid_in_flow': latest.get('mid_in_flow'),
            'sml_in_flow': latest.get('sml_in_flow'),
            'time': latest.get('capital_flow_item_time'),
            'last_valid_time': latest.get('last_valid_time'),
        },
        'has_trimmed_zero_tail': len(effective) != len(items),
    }
    if detail:
        result['items'] = [
            {
                'in_flow': x.get('in_flow'),
                'super_in_flow': x.get('super_in_flow'),
                'big_in_flow': x.get('big_in_flow'),
                'mid_in_flow': x.get('mid_in_flow'),
                'sml_in_flow': x.get('sml_in_flow'),
                'time': x.get('capital_flow_item_time'),
                'last_valid_time': x.get('last_valid_time'),
            }
            for x in effective
        ]
    else:
        result['items'] = []
    return result


def summarize_basicinfo(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out = []
    for x in items:
        out.append({
            'symbol': normalize_symbol(x.get('code')),
            'name': x.get('name'),
            'lot_size': x.get('lot_size'),
            'listing_date': x.get('listing_date'),
            'stock_id': x.get('stock_id'),
            'delisting': x.get('delisting'),
        })
    return out


def summarize_plate_list(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            'code': x.get('code'),
            'plate_name': x.get('plate_name'),
            'plate_id': x.get('plate_id'),
        }
        for x in items
    ]


def summarize_plate_stock(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        'count': len(items),
        'items': [
            {
                'symbol': normalize_symbol(x.get('code')),
                'stock_name': x.get('stock_name'),
                'lot_size': x.get('lot_size'),
                'list_time': x.get('list_time'),
            }
            for x in items[:10]
        ],
    }


def summarize_option_expirations(items: List[Dict[str, Any]]) -> List[str]:
    return [x.get('expiration_date') for x in items if x.get('expiration_date')]


def summarize_option_chain(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        'count': len(items),
        'items': [
            {
                'code': x.get('code'),
                'name': x.get('name'),
                'stock_owner': normalize_symbol(x.get('stock_owner')),
                'strike_time': x.get('strike_time'),
                'strike_price': x.get('strike_price'),
                'option_type': x.get('option_type'),
            }
            for x in items[:10]
        ],
    }
