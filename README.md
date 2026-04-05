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

## Available Tools (20 total)

This MCP exposes only the official J-Quants V2 data endpoints. Tool names and parameters follow the doc MCP contract.

### Equity (6)
- `eq-master` - Listed company master data
- `eq-bars-daily` - Daily OHLCV
- `eq-bars-daily-am` - Morning session prices
- `eq-bars-minute` - 1-minute bars
- `eq-earnings-cal` - Earnings calendar
- `eq-investor-types` - Investor type trading

### Financial (3)
- `fin-summary` - Earnings summaries
- `fin-details` - Full statements
- `fin-dividend` - Dividends

### Market (6)
- `mkt-short-ratio` - Short selling ratio
- `mkt-short-sale` - Short sale reports
- `mkt-margin-int` - Weekly margin balance
- `mkt-margin-alert` - Daily margin alerts
- `mkt-breakdown` - Trading breakdown
- `mkt-cal` - Trading calendar

### Index (2)
- `idx-bars-daily` - Index prices
- `idx-bars-daily-topix` - TOPIX prices

### Derivatives (3)
- `drv-bars-daily-fut` - Futures
- `drv-bars-daily-opt` - Options
- `drv-bars-daily-opt-225` - Nikkei 225 options

## Response Format

All tools return the official J-Quants V2 JSON payload without DataFrame wrapping or custom truncation:
```json
{
  "data": [
    {
      "Date": "2024-01-04",
      "...": "official endpoint fields"
    }
  ],
  "pagination_key": "value1.value2."
}
```

## License

MIT
