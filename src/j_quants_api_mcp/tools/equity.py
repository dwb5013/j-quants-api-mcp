import json

from j_quants_api_mcp.client import get_client, get_raw_json
from j_quants_api_mcp.convert import df_to_response
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


def get_eq_master(code: str = "", date: str = "") -> str:
    try:
        cli = get_client()
        df = cli.get_eq_master(code=code, date=date)
        return df_to_response(df, "get_eq_master")
    except Exception as e:
        return format_error(e, "get_eq_master")


def get_list(code: str = "", date_yyyymmdd: str = "") -> str:
    try:
        cli = get_client()
        df = cli.get_list(code=code, date_yyyymmdd=date_yyyymmdd)
        return df_to_response(df, "get_list")
    except Exception as e:
        return format_error(e, "get_list")


def get_eq_bars_daily(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_eq_bars_daily(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_eq_bars_daily")
    except Exception as e:
        return format_error(e, "get_eq_bars_daily")


def get_eq_bars_daily_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_eq_bars_daily_range(**kwargs)
        return df_to_response(df, "get_eq_bars_daily_range")
    except Exception as e:
        return format_error(e, "get_eq_bars_daily_range")


def get_eq_bars_daily_am(code: str = "") -> str:
    try:
        cli = get_client()
        df = cli.get_eq_bars_daily_am(code=code)
        return df_to_response(df, "get_eq_bars_daily_am")
    except Exception as e:
        return format_error(e, "get_eq_bars_daily_am")


def get_eq_bars_minute(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_eq_bars_minute(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_eq_bars_minute")
    except Exception as e:
        return format_error(e, "get_eq_bars_minute")


def get_eq_bars_5minute(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_eq_bars_5minute(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_eq_bars_5minute")
    except Exception as e:
        return format_error(e, "get_eq_bars_5minute")


def get_eq_bars_15minute(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_eq_bars_15minute(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_eq_bars_15minute")
    except Exception as e:
        return format_error(e, "get_eq_bars_15minute")


def get_eq_earnings_cal() -> str:
    try:
        cli = get_client()
        df = cli.get_eq_earnings_cal()
        return df_to_response(df, "get_eq_earnings_cal")
    except Exception as e:
        return format_error(e, "get_eq_earnings_cal")


def get_eq_investor_types(
    section: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_eq_investor_types(
            section=section,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
        )
        return df_to_response(df, "get_eq_investor_types")
    except Exception as e:
        return format_error(e, "get_eq_investor_types")
