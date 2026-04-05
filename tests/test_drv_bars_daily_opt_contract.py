import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import derivatives


class DrvBarsDailyOptContractTest(unittest.TestCase):
    def test_drv_bars_daily_opt_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "140014505"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.derivatives.get_raw_json", return_value=payload) as mock_get:
            result = derivatives.drv_bars_daily_opt(
                date="2024-01-04",
                category="TOPIXE",
                contract_flag="1",
                code="13010",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/derivatives/bars/daily/options",
            params={
                "date": "2024-01-04",
                "category": "TOPIXE",
                "contract_flag": "1",
                "code": "13010",
                "pagination_key": "cursor-1",
            },
        )

    def test_drv_bars_daily_opt_tool_is_registered_under_official_name(self) -> None:
        self.assertIn("drv-bars-daily-opt", mcp._tool_manager._tools)


if __name__ == "__main__":
    unittest.main()
