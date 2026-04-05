from j_quants_api_mcp.client import get_client
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


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
