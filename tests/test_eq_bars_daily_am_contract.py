import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import equity


class EqBarsDailyAmContractTest(unittest.TestCase):
    def test_eq_bars_daily_am_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "39400"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.equity.get_raw_json", return_value=payload) as mock_get:
            result = equity.eq_bars_daily_am(code="39400", pagination_key="cursor-1")

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/equities/bars/daily/am",
            params={"code": "39400", "pagination_key": "cursor-1"},
        )

    def test_eq_bars_daily_am_tool_is_registered_under_official_name(self) -> None:
        self.assertIn("eq-bars-daily-am", mcp._tool_manager._tools)


if __name__ == "__main__":
    unittest.main()
