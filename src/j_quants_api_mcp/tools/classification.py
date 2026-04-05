from j_quants_api_mcp.client import get_client
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


def get_market_segments() -> str:
    try:
        cli = get_client()
        df = cli.get_market_segments()
        return df_to_response(df, "get_market_segments")
    except Exception as e:
        return format_error(e, "get_market_segments")


def get_17_sectors() -> str:
    try:
        cli = get_client()
        df = cli.get_17_sectors()
        return df_to_response(df, "get_17_sectors")
    except Exception as e:
        return format_error(e, "get_17_sectors")


def get_33_sectors() -> str:
    try:
        cli = get_client()
        df = cli.get_33_sectors()
        return df_to_response(df, "get_33_sectors")
    except Exception as e:
        return format_error(e, "get_33_sectors")
