import json

from j_quants_api_mcp.client import get_raw_json
from j_quants_api_mcp.errors import format_error


def eq_master(code: str = "", date: str = "") -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if date:
            params["date"] = date
        payload = get_raw_json("/equities/master", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-master")


def eq_bars_daily(
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
        payload = get_raw_json("/equities/bars/daily", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-bars-daily")


def eq_bars_daily_am(code: str = "", pagination_key: str = "") -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/equities/bars/daily/am", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-bars-daily-am")


def eq_bars_minute(
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
        payload = get_raw_json("/equities/bars/minute", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-bars-minute")


def eq_earnings_cal(pagination_key: str = "") -> str:
    try:
        params = {}
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/equities/earnings-calendar", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-earnings-cal")


def eq_investor_types(
    section: str = "",
    from_: str = "",
    to_: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {}
        if section:
            params["section"] = section
        if from_:
            params["from"] = from_
        if to_:
            params["to"] = to_
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/equities/investor-types", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "eq-investor-types")
