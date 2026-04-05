import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import financial


class FinSummaryContractTest(unittest.TestCase):
    def test_fin_summary_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "86970"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.financial.get_raw_json", return_value=payload) as mock_get:
            result = financial.fin_summary(
                code="86970",
                date="2024-01-04",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/fins/summary",
            params={
                "code": "86970",
                "date": "2024-01-04",
                "pagination_key": "cursor-1",
            },
        )

    def test_fin_summary_tool_is_registered_under_official_name(self) -> None:
        self.assertIn("fin-summary", mcp._tool_manager._tools)


if __name__ == "__main__":
    unittest.main()
