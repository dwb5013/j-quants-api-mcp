import json

from j_quants_api_mcp.client import get_raw_json
from j_quants_api_mcp.errors import format_error


def idx_bars_daily(
    code: str = "",
    date: str = "",
    from_: str = "",
    to_: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if date:
            params["date"] = date
        if from_:
            params["from"] = from_
        if to_:
            params["to"] = to_
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/indices/bars/daily", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "idx-bars-daily")


def idx_bars_daily_topix(
    from_: str = "",
    to_: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {}
        if from_:
            params["from"] = from_
        if to_:
            params["to"] = to_
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/indices/bars/daily/topix", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "idx-bars-daily-topix")
