import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import financial


class FinDividendContractTest(unittest.TestCase):
    def test_fin_dividend_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "15550"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.financial.get_raw_json", return_value=payload) as mock_get:
            result = financial.fin_dividend(
                code="15550",
                date="2024-01-04",
                from_="2024-01-01",
                to_="2024-01-31",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/fins/dividend",
            params={
                "code": "15550",
                "date": "2024-01-04",
                "from": "2024-01-01",
                "to": "2024-01-31",
                "pagination_key": "cursor-1",
            },
        )

    def test_fin_dividend_tool_schema_uses_official_query_names(self) -> None:
        schema = mcp._tool_manager._tools["fin-dividend"].parameters

        self.assertIn("date", schema["properties"])
        self.assertIn("from", schema["properties"])
        self.assertIn("to", schema["properties"])
        self.assertIn("pagination_key", schema["properties"])
        self.assertNotIn("from_", schema["properties"])
        self.assertNotIn("to_", schema["properties"])


if __name__ == "__main__":
    unittest.main()
