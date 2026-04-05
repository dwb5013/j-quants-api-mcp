import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import financial


class FinDetailsContractTest(unittest.TestCase):
    def test_fin_details_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "86970", "FS": {}}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.financial.get_raw_json", return_value=payload) as mock_get:
            result = financial.fin_details(
                code="86970",
                date="2024-01-04",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/fins/details",
            params={
                "code": "86970",
                "date": "2024-01-04",
                "pagination_key": "cursor-1",
            },
        )

    def test_fin_details_tool_is_registered_under_official_name(self) -> None:
        self.assertIn("fin-details", mcp._tool_manager._tools)


if __name__ == "__main__":
    unittest.main()
