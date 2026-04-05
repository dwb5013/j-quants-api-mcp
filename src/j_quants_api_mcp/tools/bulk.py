import json

from j_quants_api_mcp.client import get_client
from j_quants_api_mcp.convert import df_to_response
from j_quants_api_mcp.errors import format_error


def get_bulk_list(endpoint: str) -> str:
    try:
        cli = get_client()
        df = cli.get_bulk_list(endpoint=endpoint)
        return df_to_response(df, "get_bulk_list")
    except Exception as e:
        return format_error(e, "get_bulk_list")


def get_bulk(key: str) -> str:
    try:
        cli = get_client()
        result = cli.get_bulk(key=key)
        return json.dumps({
            "download_url": result,
            "method": "get_bulk",
            "note": "URL is valid for 5 minutes. Use it to download the gzip-compressed data file.",
        }, ensure_ascii=False)
    except Exception as e:
        return format_error(e, "get_bulk")
