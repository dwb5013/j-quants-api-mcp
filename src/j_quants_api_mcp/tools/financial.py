import json

from j_quants_api_mcp.client import get_raw_json
from j_quants_api_mcp.errors import format_error


def fin_summary(code: str = "", date: str = "", pagination_key: str = "") -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if date:
            params["date"] = date
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/fins/summary", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "fin-summary")


def fin_details(code: str = "", date: str = "", pagination_key: str = "") -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if date:
            params["date"] = date
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/fins/details", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "fin-details")


def fin_dividend(
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
        payload = get_raw_json("/fins/dividend", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "fin-dividend")
