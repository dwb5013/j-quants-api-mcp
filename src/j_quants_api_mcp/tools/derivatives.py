from j_quants_api_mcp.client import get_client
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


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
