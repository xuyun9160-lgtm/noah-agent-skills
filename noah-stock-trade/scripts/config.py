from dataclasses import dataclass
import os
from pathlib import Path

from errors import ConfigError


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


@dataclass
class TradeConfig:
    base_url: str
    group_no: str
    env: str = "test"
    read_only: bool = True
    timeout_seconds: int = 15


def load_trade_config() -> TradeConfig:
    base_url = os.getenv("NOAH_TRADE_API_BASE_URL", "").strip()
    group_no = os.getenv("NOAH_TRADE_GROUP_NO", "").strip()
    env = os.getenv("NOAH_TRADE_ENV", "test").strip() or "test"
    read_only = os.getenv("NOAH_TRADE_READ_ONLY", "true").lower() != "false"
    timeout_seconds = int(os.getenv("NOAH_TRADE_TIMEOUT", "15"))

    if not base_url:
        raise ConfigError("NOAH_TRADE_API_BASE_URL is missing", hint="请先配置交易 API Base URL")
    if not group_no:
        raise ConfigError("NOAH_TRADE_GROUP_NO is missing", hint="请先配置交易账户分组 groupNo")

    return TradeConfig(
        base_url=base_url.rstrip("/"),
        group_no=group_no,
        env=env,
        read_only=read_only,
        timeout_seconds=timeout_seconds,
    )
