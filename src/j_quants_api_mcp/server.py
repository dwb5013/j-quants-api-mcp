from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from j_quants_api_mcp.tools import (
    bulk,
    classification,
    derivatives,
    equity,
    financial,
    index,
    market,
)

mcp = FastMCP("j-quants-api-mcp")

# ── Classification ──────────────────────────────────────────────────────────


@mcp.tool()
def get_market_segments() -> str:
    """Get the list of market segment classifications (e.g. Prime, Standard, Growth)."""
    return classification.get_market_segments()


@mcp.tool()
def get_17_sectors() -> str:
    """Get the 17-sector industry classification list used by JPX."""
    return classification.get_17_sectors()


@mcp.tool()
def get_33_sectors() -> str:
    """Get the 33-sector industry classification list used by JPX."""
    return classification.get_33_sectors()


# ── Equity ──────────────────────────────────────────────────────────────────


@mcp.tool(name="eq-master")
def eq_master(code: str = "", date: str = "") -> str:
    """Official V2 endpoint: listed company master data.

    Args:
        code: Stock code (e.g. "72030" or "7203"). 4-digit returns common shares only.
        date: Reference date (YYYYMMDD or YYYY-MM-DD).
    """
    return equity.eq_master(code=code, date=date)


@mcp.tool()
def get_list(code: str = "", date_yyyymmdd: str = "") -> str:
    """Get listed stock info with sector classification. Both params are optional — omit both to get all.

    Args:
        code: Stock code (e.g. "72030"). 4-digit returns common shares only.
        date_yyyymmdd: Date (YYYYMMDD or YYYY-MM-DD).
    """
    return equity.get_list(code=code, date_yyyymmdd=date_yyyymmdd)


@mcp.tool(name="eq-bars-daily")
def eq_bars_daily(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily stock price bars.

    Args:
        code: Stock code (e.g. "72030"). Empty = all stocks on the given date.
        date: Specific date (YYYYMMDD or YYYY-MM-DD).
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return equity.eq_bars_daily(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool()
def get_eq_bars_daily_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get daily stock prices for ALL stocks in a date range. Warning: very large dataset.

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return equity.get_eq_bars_daily_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool(name="eq-bars-daily-am")
def eq_bars_daily_am(code: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: morning-session stock price bars.

    Args:
        code: Stock code (e.g. "72030"). Empty for all.
        pagination_key: Pagination cursor returned by the previous call.
    """
    return equity.eq_bars_daily_am(code=code, pagination_key=pagination_key)


@mcp.tool(name="eq-bars-minute")
def eq_bars_minute(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: 1-minute stock price bars.

    Args:
        code: Stock code (e.g. "72030").
        date: Specific date (YYYYMMDD or YYYY-MM-DD).
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return equity.eq_bars_minute(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool()
def get_eq_bars_5minute(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get 5-minute OHLCV bars (requires Minute addon). Requires code OR date.

    Args:
        code: Stock code (e.g. "72030").
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return equity.get_eq_bars_5minute(
        code=code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool()
def get_eq_bars_15minute(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get 15-minute OHLCV bars (requires Minute addon). Requires code OR date.

    Args:
        code: Stock code (e.g. "72030").
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return equity.get_eq_bars_15minute(
        code=code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool(name="eq-earnings-cal")
def eq_earnings_cal(pagination_key: str = "") -> str:
    """Official V2 endpoint: earnings announcement calendar."""
    return equity.eq_earnings_cal(pagination_key=pagination_key)


@mcp.tool(name="eq-investor-types")
def eq_investor_types(
    section: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: investor type trading data.

    Args:
        section: Market section filter.
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return equity.eq_investor_types(
        section=section,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


# ── Financial ───────────────────────────────────────────────────────────────


@mcp.tool(name="fin-summary")
def fin_summary(code: str = "", date: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: financial statement summary data.

    Args:
        code: Stock code (e.g. "72030").
        date: Disclosure date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return financial.fin_summary(code=code, date=date, pagination_key=pagination_key)


@mcp.tool()
def get_fin_summary_range(
    start_dt: str = "20080707",
    end_dt: str = "",
) -> str:
    """Get financial summaries for ALL companies in a date range. Warning: very large.

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20080707 (data available from).
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return financial.get_fin_summary_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool(name="fin-details")
def fin_details(code: str = "", date: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: financial statement detail data.

    Args:
        code: Stock code (e.g. "72030").
        date: Disclosure date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return financial.fin_details(code=code, date=date, pagination_key=pagination_key)


@mcp.tool()
def get_fin_details_range(
    start_dt: str = "20080707",
    end_dt: str = "",
) -> str:
    """Get detailed financial statements for ALL companies in a date range (Premium plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20080707.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return financial.get_fin_details_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool(name="fin-dividend")
def fin_dividend(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: dividend information.

    Args:
        code: Stock code (e.g. "72030").
        date: Notice date (YYYYMMDD or YYYY-MM-DD).
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return financial.fin_dividend(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


# ── Market ──────────────────────────────────────────────────────────────────


@mcp.tool()
def get_mkt_short_ratio(
    sector_33_code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get short selling ratio by sector (Standard+ plan). Requires sector_33_code OR date.

    Args:
        sector_33_code: 33-sector code (e.g. "0050"). Use get_33_sectors to look up codes.
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return market.get_mkt_short_ratio(
        sector_33_code=sector_33_code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool()
def get_mkt_short_ratio_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get short selling ratios for ALL sectors in a date range (Standard+ plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return market.get_mkt_short_ratio_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool()
def get_mkt_short_sale_report(
    code: str = "",
    disclosed_date: str = "",
    disclosed_date_from: str = "",
    disclosed_date_to: str = "",
    calculated_date: str = "",
) -> str:
    """Get short sale disclosure reports (Standard+ plan).

    Args:
        code: Stock code filter.
        disclosed_date: Disclosure date (YYYYMMDD).
        disclosed_date_from: Disclosure start date (YYYYMMDD).
        disclosed_date_to: Disclosure end date (YYYYMMDD).
        calculated_date: Calculation date (YYYYMMDD).
    """
    return market.get_mkt_short_sale_report(
        code=code,
        disclosed_date=disclosed_date,
        disclosed_date_from=disclosed_date_from,
        disclosed_date_to=disclosed_date_to,
        calculated_date=calculated_date,
    )


@mcp.tool()
def get_mkt_short_sale_report_range(
    start_dt: str = "20131107",
    end_dt: str = "",
) -> str:
    """Get short sale reports for a date range (Standard+ plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20131107.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return market.get_mkt_short_sale_report_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool()
def get_mkt_margin_interest(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get weekly margin trading balance (Standard+ plan). Requires code OR date.
    Note: No data for weeks with 2 or fewer business days (e.g. year-end holidays).

    Args:
        code: Stock code filter.
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return market.get_mkt_margin_interest(
        code=code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool()
def get_mkt_margin_interest_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get weekly margin trading balance for a date range (Standard+ plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return market.get_mkt_margin_interest_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool()
def get_mkt_margin_alert(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get daily margin trading alert data (Standard+ plan). Requires code OR date.
    Note: Correction records include both old and new values. ETF ratios shown as "*". Previous day value shown as "-" when unpublished.

    Args:
        code: Stock code filter.
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return market.get_mkt_margin_alert(
        code=code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool()
def get_mkt_margin_alert_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get daily margin trading alerts for a date range (Standard+ plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return market.get_mkt_margin_alert_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool()
def get_mkt_breakdown(
    code: str = "",
    from_yyyymmdd: str = "",
    to_yyyymmdd: str = "",
    date_yyyymmdd: str = "",
) -> str:
    """Get trading breakdown data by investor type (Premium plan). Requires code OR date.
    Note: 2020/10/01 has no data due to TSE system outage.

    Args:
        code: Stock code filter.
        from_yyyymmdd: Start date (YYYYMMDD).
        to_yyyymmdd: End date (YYYYMMDD).
        date_yyyymmdd: Specific date (YYYYMMDD).
    """
    return market.get_mkt_breakdown(
        code=code,
        from_yyyymmdd=from_yyyymmdd,
        to_yyyymmdd=to_yyyymmdd,
        date_yyyymmdd=date_yyyymmdd,
    )


@mcp.tool()
def get_mkt_breakdown_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get trading breakdown data for a date range (Premium plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return market.get_mkt_breakdown_range(start_dt=start_dt, end_dt=end_dt)


@mcp.tool(name="mkt-cal")
def mkt_cal(
    hol_div: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
) -> str:
    """Official V2 endpoint: market trading calendar.

    Args:
        hol_div: Holiday division filter.
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
    """
    return market.mkt_cal(hol_div=hol_div, from_=from_, to_=to_)


# ── Index ───────────────────────────────────────────────────────────────────


@mcp.tool(name="idx-bars-daily")
def idx_bars_daily(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily index price bars.

    Args:
        code: Index code.
        date: Specific date (YYYYMMDD or YYYY-MM-DD).
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return index.idx_bars_daily(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="idx-bars-daily-topix")
def idx_bars_daily_topix(
    from_: Annotated[str, Field(alias="from")] = "",
    to_: Annotated[str, Field(alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: TOPIX daily price bars.

    Args:
        from_: Start date (YYYYMMDD or YYYY-MM-DD).
        to_: End date (YYYYMMDD or YYYY-MM-DD).
        pagination_key: Pagination cursor returned by the previous call.
    """
    return index.idx_bars_daily_topix(from_=from_, to_=to_, pagination_key=pagination_key)


# ── Derivatives ─────────────────────────────────────────────────────────────


@mcp.tool()
def get_drv_bars_daily_fut(
    date_yyyymmdd: str,
    category: str = "",
    contract_flag: str = "",
) -> str:
    """Get daily futures price bars (Premium plan). date_yyyymmdd is REQUIRED.

    Args:
        date_yyyymmdd: Trade date (YYYYMMDD). REQUIRED - no code alternative for this endpoint.
        category: Futures category filter.
        contract_flag: Contract type filter.
    """
    return derivatives.get_drv_bars_daily_fut(
        date_yyyymmdd=date_yyyymmdd,
        category=category,
        contract_flag=contract_flag,
    )


@mcp.tool()
def get_drv_bars_daily_fut_range(
    start_dt: str = "20170101",
    end_dt: str = "",
    category: str = "",
    contract_flag: str = "",
) -> str:
    """Get daily futures prices for a date range (Premium plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
        category: Futures category filter.
        contract_flag: Contract type filter.
    """
    return derivatives.get_drv_bars_daily_fut_range(
        start_dt=start_dt,
        end_dt=end_dt,
        category=category,
        contract_flag=contract_flag,
    )


@mcp.tool()
def get_drv_bars_daily_opt(
    date_yyyymmdd: str,
    category: str = "",
    contract_flag: str = "",
    code: str = "",
) -> str:
    """Get daily options price bars (Premium plan). date_yyyymmdd is REQUIRED.

    Args:
        date_yyyymmdd: Trade date (YYYYMMDD). REQUIRED.
        category: Options category filter.
        contract_flag: Contract type filter.
        code: Option code filter.
    """
    return derivatives.get_drv_bars_daily_opt(
        date_yyyymmdd=date_yyyymmdd,
        category=category,
        contract_flag=contract_flag,
        code=code,
    )


@mcp.tool()
def get_drv_bars_daily_opt_range(
    start_dt: str = "20170101",
    end_dt: str = "",
    category: str = "",
    contract_flag: str = "",
    code: str = "",
) -> str:
    """Get daily options prices for a date range (Premium plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
        category: Options category filter.
        contract_flag: Contract type filter.
        code: Option code filter.
    """
    return derivatives.get_drv_bars_daily_opt_range(
        start_dt=start_dt,
        end_dt=end_dt,
        category=category,
        contract_flag=contract_flag,
        code=code,
    )


@mcp.tool(name="drv-bars-daily-opt-225")
def drv_bars_daily_opt_225(date: str, pagination_key: str = "") -> str:
    """Official V2 endpoint: Nikkei 225 options daily bars.

    Args:
        date: Trade date (YYYYMMDD or YYYY-MM-DD). REQUIRED.
        pagination_key: Pagination cursor returned by the previous call.
    """
    return derivatives.drv_bars_daily_opt_225(date=date, pagination_key=pagination_key)


@mcp.tool()
def get_drv_bars_daily_opt_225_range(
    start_dt: str = "20170101",
    end_dt: str = "",
) -> str:
    """Get Nikkei 225 options for a date range (Standard+ plan).

    Args:
        start_dt: Start date (YYYYMMDD or YYYY-MM-DD). Default: 20170101.
        end_dt: End date (YYYYMMDD or YYYY-MM-DD). Default: today.
    """
    return derivatives.get_drv_bars_daily_opt_225_range(
        start_dt=start_dt,
        end_dt=end_dt,
    )


# ── Bulk ────────────────────────────────────────────────────────────────────


@mcp.tool()
def get_bulk_list(endpoint: str) -> str:
    """List available bulk data files for an endpoint (Light+ plan). endpoint is REQUIRED.

    Args:
        endpoint: API endpoint path. REQUIRED. Examples: "/equities/master", "/equities/bars/daily",
                  "/financials/summary", "/markets/calendar", "/markets/margin-alert".
    """
    return bulk.get_bulk_list(endpoint=endpoint)


@mcp.tool()
def get_bulk(key: str) -> str:
    """Get a signed download URL for a bulk data file (Light+ plan). URL valid for 5 minutes.

    Args:
        key: File key from get_bulk_list results. REQUIRED.
    """
    return bulk.get_bulk(key=key)
