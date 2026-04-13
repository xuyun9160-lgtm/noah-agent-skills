#!/usr/bin/env python3
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urljoin

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None


WORKSPACE = Path(__file__).resolve().parents[3]
SECRETS_FILE = WORKSPACE / '.secrets' / 'noah-trade.env'


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file(SECRETS_FILE)


class NoahTradeClient:
    def __init__(self, base_url: Optional[str] = None, group_no: Optional[str] = None, timeout: int = 15):
        self.base_url = (base_url or os.getenv('NOAH_TRADE_API_BASE_URL', '')).rstrip('/') + '/'
        self.group_no = group_no or os.getenv('NOAH_TRADE_GROUP_NO', '')
        self.timeout = timeout
        if not self.base_url:
            raise ValueError('NOAH_TRADE_API_BASE_URL is missing')
        if not self.group_no:
            raise ValueError('NOAH_TRADE_GROUP_NO is missing')
        if requests is None:
            raise RuntimeError('requests is required')

    def _headers(self) -> Dict[str, str]:
        return {
            'groupNo': self.group_no,
            'Accept': 'application/json',
        }

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = urljoin(self.base_url, path.lstrip('/'))
        resp = requests.get(url, headers=self._headers(), params=params or {}, timeout=self.timeout)
        return self._normalize_response(resp)

    def _normalize_response(self, resp) -> Dict[str, Any]:
        try:
            body = resp.json()
        except Exception:
            return {'ok': False, 'http_status': resp.status_code, 'message': resp.text[:500], 'data': None}
        success = body.get('success', False)
        return {
            'ok': bool(success) and resp.ok,
            'http_status': resp.status_code,
            'code': body.get('code'),
            'message': body.get('msg', ''),
            'data': body.get('data'),
            'raw': body,
        }


if __name__ == '__main__':
    client = NoahTradeClient()
    print(json.dumps({'base_url': client.base_url, 'group_no_loaded': bool(client.group_no)}, ensure_ascii=False))
