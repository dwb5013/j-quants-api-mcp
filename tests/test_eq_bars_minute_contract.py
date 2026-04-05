import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import equity


class EqBarsMinuteContractTest(unittest.TestCase):
    def test_eq_bars_minute_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "86970", "Time": "09:00"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.equity.get_raw_json", return_value=payload) as mock_get:
            result = equity.eq_bars_minute(
                code="86970",
                date="2024-01-04",
                from_="2024-01-01",
                to_="2024-01-31",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/equities/bars/minute",
            params={
                "code": "86970",
                "date": "2024-01-04",
                "from": "2024-01-01",
                "to": "2024-01-31",
                "pagination_key": "cursor-1",
            },
        )

    def test_eq_bars_minute_tool_schema_uses_official_query_names(self) -> None:
        schema = mcp._tool_manager._tools["eq-bars-minute"].parameters

        self.assertIn("date", schema["properties"])
        self.assertIn("from", schema["properties"])
        self.assertIn("to", schema["properties"])
        self.assertIn("pagination_key", schema["properties"])
        self.assertNotIn("from_", schema["properties"])
        self.assertNotIn("to_", schema["properties"])


if __name__ == "__main__":
    unittest.main()
