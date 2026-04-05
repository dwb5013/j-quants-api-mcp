from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from j_quants_api_mcp.tools import derivatives, equity, financial, index, market

mcp = FastMCP("j-quants-api-mcp")


@mcp.tool(name="eq-master")
def eq_master(code: str = "", date: str = "") -> str:
    """Official V2 endpoint: listed company master data."""
    return equity.eq_master(code=code, date=date)


@mcp.tool(name="eq-bars-daily")
def eq_bars_daily(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily stock price bars."""
    return equity.eq_bars_daily(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="eq-bars-daily-am")
def eq_bars_daily_am(code: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: morning-session stock price bars."""
    return equity.eq_bars_daily_am(code=code, pagination_key=pagination_key)


@mcp.tool(name="eq-bars-minute")
def eq_bars_minute(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: 1-minute stock price bars."""
    return equity.eq_bars_minute(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="eq-earnings-cal")
def eq_earnings_cal(pagination_key: str = "") -> str:
    """Official V2 endpoint: earnings announcement calendar."""
    return equity.eq_earnings_cal(pagination_key=pagination_key)


@mcp.tool(name="eq-investor-types")
def eq_investor_types(
    section: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: investor type trading data."""
    return equity.eq_investor_types(
        section=section,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="fin-summary")
def fin_summary(code: str = "", date: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: financial statement summary data."""
    return financial.fin_summary(code=code, date=date, pagination_key=pagination_key)


@mcp.tool(name="fin-details")
def fin_details(code: str = "", date: str = "", pagination_key: str = "") -> str:
    """Official V2 endpoint: financial statement detail data."""
    return financial.fin_details(code=code, date=date, pagination_key=pagination_key)


@mcp.tool(name="fin-dividend")
def fin_dividend(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: dividend information."""
    return financial.fin_dividend(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-short-ratio")
def mkt_short_ratio(
    s33: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: short-selling ratio by sector."""
    return market.mkt_short_ratio(
        s33=s33,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-short-sale")
def mkt_short_sale(
    code: str = "",
    disc_date: str = "",
    disc_date_from: str = "",
    disc_date_to: str = "",
    calc_date: str = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: short sale disclosure reports."""
    return market.mkt_short_sale(
        code=code,
        disc_date=disc_date,
        disc_date_from=disc_date_from,
        disc_date_to=disc_date_to,
        calc_date=calc_date,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-margin-int")
def mkt_margin_int(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: weekly margin interest balances."""
    return market.mkt_margin_int(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-margin-alert")
def mkt_margin_alert(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily margin alert data."""
    return market.mkt_margin_alert(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-breakdown")
def mkt_breakdown(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: trading breakdown data."""
    return market.mkt_breakdown(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="mkt-cal")
def mkt_cal(
    hol_div: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
) -> str:
    """Official V2 endpoint: market trading calendar."""
    return market.mkt_cal(hol_div=hol_div, from_=from_, to_=to_)


@mcp.tool(name="idx-bars-daily")
def idx_bars_daily(
    code: str = "",
    date: str = "",
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily index price bars."""
    return index.idx_bars_daily(
        code=code,
        date=date,
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="idx-bars-daily-topix")
def idx_bars_daily_topix(
    from_: Annotated[str, Field(validation_alias="from")] = "",
    to_: Annotated[str, Field(validation_alias="to")] = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: TOPIX daily price bars."""
    return index.idx_bars_daily_topix(
        from_=from_,
        to_=to_,
        pagination_key=pagination_key,
    )


@mcp.tool(name="drv-bars-daily-fut")
def drv_bars_daily_fut(
    date: str,
    category: str = "",
    contract_flag: str = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily futures price bars."""
    return derivatives.drv_bars_daily_fut(
        date=date,
        category=category,
        contract_flag=contract_flag,
        pagination_key=pagination_key,
    )


@mcp.tool(name="drv-bars-daily-opt")
def drv_bars_daily_opt(
    date: str,
    category: str = "",
    contract_flag: str = "",
    code: str = "",
    pagination_key: str = "",
) -> str:
    """Official V2 endpoint: daily options price bars."""
    return derivatives.drv_bars_daily_opt(
        date=date,
        category=category,
        contract_flag=contract_flag,
        code=code,
        pagination_key=pagination_key,
    )


@mcp.tool(name="drv-bars-daily-opt-225")
def drv_bars_daily_opt_225(date: str, pagination_key: str = "") -> str:
    """Official V2 endpoint: Nikkei 225 options daily bars."""
    return derivatives.drv_bars_daily_opt_225(date=date, pagination_key=pagination_key)
