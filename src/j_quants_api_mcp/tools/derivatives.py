import json

from j_quants_api_mcp.client import get_client, get_raw_json
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


def drv_bars_daily_opt_225(date: str, pagination_key: str = "") -> str:
    try:
        params = {"date": date}
        if pagination_key:
            params["pagination_key"] = pagination_key
        payload = get_raw_json("/derivatives/bars/daily/options/225", params=params)
        return json.dumps(payload, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "drv-bars-daily-opt-225")


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


def get_drv_bars_daily_fut(
    date_yyyymmdd: str,
    category: str = "",
    contract_flag: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_fut(
            date_yyyymmdd=date_yyyymmdd,
            category=category,
            contract_flag=contract_flag,
        )
        return df_to_response(df, "get_drv_bars_daily_fut")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_fut")


def get_drv_bars_daily_fut_range(
    start_dt: str = "20170101",
    end_dt: str = "",
    category: str = "",
    contract_flag: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_fut_range(
            start_dt=start_dt,
            **({"end_dt": end_dt} if end_dt else {}),
            category=category,
            contract_flag=contract_flag,
        )
        return df_to_response(df, "get_drv_bars_daily_fut_range")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_fut_range")


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


def get_drv_bars_daily_opt(
    date_yyyymmdd: str,
    category: str = "",
    contract_flag: str = "",
    code: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_opt(
            date_yyyymmdd=date_yyyymmdd,
            category=category,
            contract_flag=contract_flag,
            code=code,
        )
        return df_to_response(df, "get_drv_bars_daily_opt")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_opt")


def get_drv_bars_daily_opt_range(
    start_dt: str = "20170101",
    end_dt: str = "",
    category: str = "",
    contract_flag: str = "",
    code: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_opt_range(
            start_dt=start_dt,
            **({"end_dt": end_dt} if end_dt else {}),
            category=category,
            contract_flag=contract_flag,
            code=code,
        )
        return df_to_response(df, "get_drv_bars_daily_opt_range")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_opt_range")


def get_drv_bars_daily_opt_225(date_yyyymmdd: str) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_opt_225(date_yyyymmdd=date_yyyymmdd)
        return df_to_response(df, "get_drv_bars_daily_opt_225")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_opt_225")


def get_drv_bars_daily_opt_225_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_drv_bars_daily_opt_225_range(
            start_dt=start_dt,
            **({"end_dt": end_dt} if end_dt else {}),
        )
        return df_to_response(df, "get_drv_bars_daily_opt_225_range")
    except Exception as e:
        return format_error(e, "get_drv_bars_daily_opt_225_range")
