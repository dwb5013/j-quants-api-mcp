import json

from j_quants_api_mcp.client import get_client, get_raw_json
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


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


def get_idx_bars_daily(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_idx_bars_daily(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_idx_bars_daily")
    except Exception as e:
        return format_error(e, "get_idx_bars_daily")


def get_idx_bars_daily_topix(
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_idx_bars_daily_topix(
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
        )
        return df_to_response(df, "get_idx_bars_daily_topix")
    except Exception as e:
        return format_error(e, "get_idx_bars_daily_topix")
