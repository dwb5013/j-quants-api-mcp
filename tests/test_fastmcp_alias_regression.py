import asyncio
import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp


class FastMcpAliasRegressionTest(unittest.TestCase):
    def test_eq_bars_daily_accepts_official_from_to_params_at_runtime(self) -> None:
        payload = {"data": [{"Code": "72030"}], "pagination_key": "next"}
        tool = mcp._tool_manager._tools["eq-bars-daily"]

        with patch("j_quants_api_mcp.tools.equity.eq_bars_daily", return_value=json.dumps(payload)) as mock_call:
            result = asyncio.run(
                tool.run(
                    {
                        "code": "72030",
                        "date": "2024-01-04",
                        "from": "2024-01-01",
                        "to": "2024-01-31",
                        "pagination_key": "cursor-1",
                    }
                )
            )

        self.assertEqual(json.loads(result), payload)
        mock_call.assert_called_once_with(
            code="72030",
            date="2024-01-04",
            from_="2024-01-01",
            to_="2024-01-31",
            pagination_key="cursor-1",
        )


if __name__ == "__main__":
    unittest.main()
