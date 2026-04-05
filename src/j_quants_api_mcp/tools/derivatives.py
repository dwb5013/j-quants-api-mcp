import json

from j_quants_api_mcp.client import get_raw_json
from j_quants_api_mcp.errors import format_error


def drv_bars_daily_fut(
    date: str,
    category: str = "",
    contract_flag: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {"date": date}
        if category:
            params["category"] = category
        if contract_flag:
            params["contract_flag"] = contract_flag
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/derivatives/bars/daily/futures", params=params)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "drv-bars-daily-fut")


def drv_bars_daily_opt(
    date: str,
    category: str = "",
    contract_flag: str = "",
    code: str = "",
    pagination_key: str = "",
) -> str:
    try:
        params = {"date": date}
        if category:
            params["category"] = category
        if contract_flag:
            params["contract_flag"] = contract_flag
        if code:
            params["code"] = code
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/derivatives/bars/daily/options", params=params)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "drv-bars-daily-opt")


def drv_bars_daily_opt_225(date: str, pagination_key: str = "") -> str:
    try:
        params = {"date": date}
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/derivatives/bars/daily/options/225", params=params)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "drv-bars-daily-opt-225")
