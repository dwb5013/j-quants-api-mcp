import json

from j_quants_api_mcp.client import get_client, get_raw_json
from j_quants_api_mcp.convert import df_to_response
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


def get_fin_summary(code: str = "", date_yyyymmdd: str = "") -> str:
    try:
        cli = get_client()
        df = cli.get_fin_summary(code=code, date_yyyymmdd=date_yyyymmdd)
        return df_to_response(df, "get_fin_summary")
    except Exception as e:
        return format_error(e, "get_fin_summary")


def get_fin_summary_range(
    start_dt: str = "20080707",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_fin_summary_range(**kwargs)
        return df_to_response(df, "get_fin_summary_range")
    except Exception as e:
        return format_error(e, "get_fin_summary_range")


def get_fin_details(code: str = "", date_yyyymmdd: str = "") -> str:
    try:
        cli = get_client()
        df = cli.get_fin_details(code=code, date_yyyymmdd=date_yyyymmdd)
        return df_to_response(df, "get_fin_details")
    except Exception as e:
        return format_error(e, "get_fin_details")


def get_fin_details_range(
    start_dt: str = "20080707",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_fin_details_range(**kwargs)
        return df_to_response(df, "get_fin_details_range")
    except Exception as e:
        return format_error(e, "get_fin_details_range")


def get_fin_dividend(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_fin_dividend(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_fin_dividend")
    except Exception as e:
        return format_error(e, "get_fin_dividend")
