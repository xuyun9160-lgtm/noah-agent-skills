#!/usr/bin/env python3
from typing import Any, Dict, List


def _safe(v):
    return '-' if v is None else v


def _num(v):
    if v is None:
        return '-'
    try:
        if isinstance(v, int):
            return f'{v:,}'
        fv = float(v)
        if abs(fv) >= 1000:
            return f'{fv:,.2f}'.rstrip('0').rstrip('.')
        return f'{fv:.2f}'.rstrip('0').rstrip('.')
    except Exception:
        return v


def format_snapshot(summary: Dict[str, Any]) -> str:
    lines = []
    symbol = summary.get('symbol') or '-'
    name = summary.get('name') or '-'
    lines.append(f'标的：{name}（{symbol}）')
    lines.append(f'最新价：{_num(summary.get("last_price"))}')
    if summary.get('change_value') is not None or summary.get('change_pct') is not None:
        lines.append(f'涨跌额/涨跌幅：{_num(summary.get("change_value"))} / {_num(summary.get("change_pct"))}%')
    lines.append(f'今开/最高/最低：{_num(summary.get("open_price"))} / {_num(summary.get("high_price"))} / {_num(summary.get("low_price"))}')
    if summary.get('volume') is not None or summary.get('turnover') is not None:
        lines.append(f'成交量/成交额：{_num(summary.get("volume"))} / {_num(summary.get("turnover"))}')
    if summary.get('last_price') is not None and summary.get('open_price') is not None:
        try:
            if float(summary['last_price']) >= float(summary['open_price']):
                lines.append('观察：当前价格不弱于今开，盘中相对偏强。')
            else:
                lines.append('观察：当前价格低于今开，盘中相对偏弱。')
        except Exception:
            pass
    return '\n'.join(lines)


def format_market_state(summary_list: List[Dict[str, Any]]) -> str:
    if not summary_list:
        return '暂无市场状态数据'
    x = summary_list[0]
    return f'标的：{x.get("name") or "-"}（{x.get("symbol") or "-"}）\n当前状态：{x.get("market_state_text") or x.get("market_state")}'


def format_intraday(summary: Dict[str, Any]) -> str:
    latest = summary.get('latest') or {}
    lines = [
        f'标的：{latest.get("name") or "-"}（{latest.get("code") or "-"}）',
        f'当前价：{_num(latest.get("cur_price"))}',
        f'均价：{_num(summary.get("avg_price"))}',
        f'昨收：{_num(summary.get("last_close"))}',
        f'成交量：{_num(summary.get("volume"))}',
    ]
    try:
        cur = latest.get('cur_price')
        avg = summary.get('avg_price')
        if cur is not None and avg is not None:
            lines.append('观察：现价高于均价，分时相对偏强。' if float(cur) >= float(avg) else '观察：现价低于均价，分时相对偏弱。')
    except Exception:
        pass
    return '\n'.join(lines)


def format_kline(summary: Dict[str, Any]) -> str:
    latest = summary.get('latest') or {}
    lines = [
        f'标的：{latest.get("name") or "-"}（{latest.get("code") or "-"}）',
        f'最新K线：开{_num(latest.get("open"))} / 高{_num(latest.get("high"))} / 低{_num(latest.get("low"))} / 收{_num(latest.get("close"))}',
        f'成交量/成交额：{_num(latest.get("volume"))} / {_num(latest.get("turnover"))}',
    ]
    try:
        o = latest.get('open')
        c = latest.get('close')
        if o is not None and c is not None:
            lines.append('观察：这根K线收涨。' if float(c) >= float(o) else '观察：这根K线收跌。')
    except Exception:
        pass
    return '\n'.join(lines)


def format_orderbook(summary: Dict[str, Any]) -> str:
    bid = summary.get('best_bid') or {}
    ask = summary.get('best_ask') or {}
    lines = [
        f'标的：{summary.get("name") or "-"}（{summary.get("symbol") or "-"}）',
        f'买一：{_num(bid.get("price"))} / {_num(bid.get("quantity"))}',
        f'卖一：{_num(ask.get("price"))} / {_num(ask.get("quantity"))}',
        f'档位：买{_safe(summary.get("bid_levels"))}档 / 卖{_safe(summary.get("ask_levels"))}档',
    ]
    try:
        bq = bid.get('quantity')
        aq = ask.get('quantity')
        if bq is not None and aq is not None:
            lines.append('观察：买一量不弱于卖一量。' if float(bq) >= float(aq) else '观察：卖一量高于买一量，上方抛压更明显。')
    except Exception:
        pass
    return '\n'.join(lines)


def format_clarification(name: str, choices: list[dict]) -> str:
    lines = [f'“{name}”同时存在港股和美股，请先确认你要查哪个市场：']
    for idx, item in enumerate(choices, 1):
        lines.append(f'{idx}. {item.get("label")}（{item.get("symbol")}）')
    lines.append('你直接回复“港股”或“美股”就行。')
    return '\n'.join(lines)


def format_capital_flow(summary: Dict[str, Any], detail: bool = False) -> str:
    latest = summary.get('latest') or {}
    if detail and summary.get('items'):
        lines = ['资金流向（逐条）：']
        for i, x in enumerate(summary.get('items', []), 1):
            lines.extend([
                f'{i}）净流入：{_num(x.get("in_flow"))}',
                f'  - 特大单：{_num(x.get("super_in_flow"))}',
                f'  - 大单：{_num(x.get("big_in_flow"))}',
                f'  - 中单：{_num(x.get("mid_in_flow"))}',
                f'  - 小单：{_num(x.get("sml_in_flow"))}',
            ])
        if summary.get('has_trimmed_zero_tail'):
            lines.append('说明：已自动忽略尾部 0 值占位记录。')
        return '\n'.join(lines)

    lines = [
        '资金流向：',
        f'整体净流入：{_num(latest.get("in_flow"))}',
        f'特大单净流入：{_num(latest.get("super_in_flow"))}',
        f'大单净流入：{_num(latest.get("big_in_flow"))}',
        f'中单净流入：{_num(latest.get("mid_in_flow"))}',
        f'小单净流入：{_num(latest.get("sml_in_flow"))}',
    ]
    try:
        total = latest.get('in_flow')
        if total is not None:
            lines.append('观察：整体呈净流入。' if float(total) >= 0 else '观察：整体呈净流出。')
    except Exception:
        pass
    if summary.get('has_trimmed_zero_tail'):
        lines.append('说明：已自动忽略尾部 0 值占位记录。')
    return '\n'.join(lines)


def format_basicinfo(summary_list: List[Dict[str, Any]]) -> str:
    if not summary_list:
        return '暂无基础信息'
    x = summary_list[0]
    return '\n'.join([
        f'标的：{x.get("name") or "-"}（{x.get("symbol") or "-"}）',
        f'上市日期：{_safe(x.get("listing_date"))}',
        f'每手股数：{_safe(x.get("lot_size"))}',
        f'是否退市：{_safe(x.get("delisting"))}',
    ])
