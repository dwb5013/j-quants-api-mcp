import json

from j_quants_api_mcp.client import get_raw_json
from j_quants_api_mcp.errors import format_error


def mkt_cal(hol_div: str = "", from_: str = "", to_: str = "") -> str:
    try:
        params = {}
        if hol_div:
            params["hol_div"] = hol_div
        if from_:
            params["from"] = from_
        if to_:
            params["to"] = to_
        payload = get_raw_json("/markets/calendar", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-cal")


def mkt_margin_int(
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
        payload = get_raw_json("/markets/margin-interest", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-margin-int")


def mkt_short_ratio(
    s33: str = "",
    date: str = "",
    from_: str = "",
    to_: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {}
        if s33:
            params["s33"] = s33
        if date:
            params["date"] = date
        if from_:
            params["from"] = from_
        if to_:
            params["to"] = to_
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/markets/short-ratio", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-short-ratio")


def mkt_short_sale(
    code: str = "",
    disc_date: str = "",
    disc_date_from: str = "",
    disc_date_to: str = "",
    calc_date: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {}
        if code:
            params["code"] = code
        if disc_date:
            params["disc_date"] = disc_date
        if disc_date_from:
            params["disc_date_from"] = disc_date_from
        if disc_date_to:
            params["disc_date_to"] = disc_date_to
        if calc_date:
            params["calc_date"] = calc_date
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/markets/short-sale-report", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-short-sale")


def mkt_margin_alert(
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
        payload = get_raw_json("/markets/margin-alert", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-margin-alert")


def mkt_breakdown(
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
        payload = get_raw_json("/markets/breakdown", params=params or None)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "mkt-breakdown")
