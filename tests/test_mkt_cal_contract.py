import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import market


class MktCalContractTest(unittest.TestCase):
    def test_mkt_cal_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Date": "2024-01-04", "HolDiv": "1"}]}

        with patch("j_quants_api_mcp.tools.market.get_raw_json", return_value=payload) as mock_get:
            result = market.mkt_cal(
                hol_div="1",
                from_="2024-01-01",
                to_="2024-01-31",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/markets/calendar",
            params={
                "hol_div": "1",
                "from": "2024-01-01",
                "to": "2024-01-31",
            },
        )

    def test_mkt_cal_tool_schema_uses_official_query_names(self) -> None:
        schema = mcp._tool_manager._tools["mkt-cal"].parameters

        self.assertIn("hol_div", schema["properties"])
        self.assertIn("from", schema["properties"])
        self.assertIn("to", schema["properties"])
        self.assertNotIn("from_", schema["properties"])
        self.assertNotIn("to_", schema["properties"])


if __name__ == "__main__":
    unittest.main()
