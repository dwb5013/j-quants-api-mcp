import json

from j_quants_api_mcp.client import get_client, get_raw_json
from j_quants_api_mcp.convert import df_to_response
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


def get_mkt_short_ratio(
    sector_33_code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_short_ratio(
            sector_33_code=sector_33_code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_mkt_short_ratio")
    except Exception as e:
        return format_error(e, "get_mkt_short_ratio")


def get_mkt_short_ratio_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_mkt_short_ratio_range(**kwargs)
        return df_to_response(df, "get_mkt_short_ratio_range")
    except Exception as e:
        return format_error(e, "get_mkt_short_ratio_range")


def get_mkt_short_sale_report(
    code: str = "",
    disclosed_date: str = "",
    disclosed_date_from: str = "",
    disclosed_date_to: str = "",
    calculated_date: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_short_sale_report(
            code=code,
            disclosed_date=disclosed_date,
            disclosed_date_from=disclosed_date_from,
            disclosed_date_to=disclosed_date_to,
            calculated_date=calculated_date,
        )
        return df_to_response(df, "get_mkt_short_sale_report")
    except Exception as e:
        return format_error(e, "get_mkt_short_sale_report")


def get_mkt_short_sale_report_range(
    start_dt: str = "20131107",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_mkt_short_sale_report_range(**kwargs)
        return df_to_response(df, "get_mkt_short_sale_report_range")
    except Exception as e:
        return format_error(e, "get_mkt_short_sale_report_range")


def get_mkt_margin_interest(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_margin_interest(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_mkt_margin_interest")
    except Exception as e:
        return format_error(e, "get_mkt_margin_interest")


def get_mkt_margin_interest_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_mkt_margin_interest_range(**kwargs)
        return df_to_response(df, "get_mkt_margin_interest_range")
    except Exception as e:
        return format_error(e, "get_mkt_margin_interest_range")


def get_mkt_margin_alert(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_margin_alert(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_mkt_margin_alert")
    except Exception as e:
        return format_error(e, "get_mkt_margin_alert")


def get_mkt_margin_alert_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_mkt_margin_alert_range(**kwargs)
        return df_to_response(df, "get_mkt_margin_alert_range")
    except Exception as e:
        return format_error(e, "get_mkt_margin_alert_range")


def get_mkt_breakdown(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_breakdown(
            code=code,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
            date_yyyymmdd=date_yyyymmdd,
        )
        return df_to_response(df, "get_mkt_breakdown")
    except Exception as e:
        return format_error(e, "get_mkt_breakdown")


def get_mkt_breakdown_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    try:
        cli = get_client()
        kwargs = {"start_dt": start_dt}
        if end_dt:
            kwargs["end_dt"] = end_dt
        df = cli.get_mkt_breakdown_range(**kwargs)
        return df_to_response(df, "get_mkt_breakdown_range")
    except Exception as e:
        return format_error(e, "get_mkt_breakdown_range")


def get_mkt_calendar(
    holiday_division: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
) -> str:
    try:
        cli = get_client()
        df = cli.get_mkt_calendar(
            holiday_division=holiday_division,
            from_yyyymmdd=from_yyyymmdd,
            to_yyyymmdd=to_yyyymmdd,
        )
        return df_to_response(df, "get_mkt_calendar")
    except Exception as e:
        return format_error(e, "get_mkt_calendar")
