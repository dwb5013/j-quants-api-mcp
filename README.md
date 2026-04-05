# j-quants-api-mcp

MCP server for executing J-Quants API calls. Wraps [jquants-api-client-python](https://github.com/J-Quants/jquants-api-client-python) (ClientV2) to let AI tools query Japanese stock market data.

## Architecture

```
AI (Claude/ChatGPT/Gemini)
    |
    +-- j-quants-doc-mcp    → Discovers which API to call
    +-- j-quants-api-mcp    → Executes the API call, returns data (this project)
```

## Setup

1. Get an API key from [J-Quants](https://application.jpx-jquants.com/)

2. Install:
```bash
uv tool install git+https://github.com/<your-org>/j-quants-api-mcp.git
```

3. Configure Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "j-quants-api-mcp": {
      "command": "uvx",
      "args": ["j-quants-api-mcp"],
      "env": {
        "JQUANTS_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Or for Claude Code (`.claude/settings.json`):
```json
{
  "mcpServers": {
    "j-quants-api-mcp": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/<your-org>/j-quants-api-mcp.git", "j-quants-api-mcp"],
      "env": {
        "JQUANTS_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Available Tools (39 total)

### Classification (3)
- `get_market_segments` - Market segment list
- `get_17_sectors` - 17-sector classification
- `get_33_sectors` - 33-sector classification

### Equity (10)
- `get_eq_master` - Listed company master data
- `get_list` - Stock list with sectors
- `get_eq_bars_daily` / `get_eq_bars_daily_range` - Daily OHLCV
- `get_eq_bars_daily_am` - Morning session prices (Premium)
- `get_eq_bars_minute` / `get_eq_bars_5minute` / `get_eq_bars_15minute` - Intraday bars (Minute addon)
- `get_eq_earnings_cal` - Earnings calendar
- `get_eq_investor_types` - Investor type trading (Premium)

### Financial (5)
- `get_fin_summary` / `get_fin_summary_range` - Earnings summaries
- `get_fin_details` / `get_fin_details_range` - Full statements (Premium)
- `get_fin_dividend` - Dividends (Premium)

### Market (11)
- `get_mkt_short_ratio` / `_range` - Short selling ratio (Standard+)
- `get_mkt_short_sale_report` / `_range` - Short sale reports (Standard+)
- `get_mkt_margin_interest` / `_range` - Weekly margin balance (Standard+)
- `get_mkt_margin_alert` / `_range` - Daily margin alerts (Standard+)
- `get_mkt_breakdown` / `_range` - Trading breakdown (Premium)
- `get_mkt_calendar` - Trading calendar (Light+)

### Index (2)
- `get_idx_bars_daily` - Index prices (Light+)
- `get_idx_bars_daily_topix` - TOPIX prices (Light+)

### Derivatives (6)
- `get_drv_bars_daily_fut` / `_range` - Futures (Standard+)
- `get_drv_bars_daily_opt` / `_range` - Options (Standard+)
- `get_drv_bars_daily_opt_225` / `_range` - Nikkei 225 options (Standard+)

### Bulk (2)
- `get_bulk_list` - List bulk data files (Light+)
- `get_bulk` - Get download URL (Light+)

## Response Format

All tools return JSON:
```json
{
  "data": [{"Date": "2024-01-04", "Open": 2510.0, ...}],
  "total_rows": 245,
  "returned_rows": 245,
  "truncated": false,
  "columns": ["Date", "Open", "High", "Low", "Close", "Volume"],
  "method": "get_eq_bars_daily"
}
```

Large results (>500 rows) are automatically truncated with `"truncated": true`.

## License

MIT
