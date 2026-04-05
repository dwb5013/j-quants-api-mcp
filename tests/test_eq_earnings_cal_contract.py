import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import equity


class EqEarningsCalContractTest(unittest.TestCase):
    def test_eq_earnings_cal_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "43760"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.equity.get_raw_json", return_value=payload) as mock_get:
            result = equity.eq_earnings_cal(pagination_key="cursor-1")

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/equities/earnings-calendar",
            params={"pagination_key": "cursor-1"},
        )

    def test_eq_earnings_cal_tool_is_registered_under_official_name(self) -> None:
        self.assertIn("eq-earnings-cal", mcp._tool_manager._tools)


if __name__ == "__main__":
    unittest.main()
