import json
import unittest
from unittest.mock import patch

from j_quants_api_mcp.server import mcp
from j_quants_api_mcp.tools import market


class MktShortSaleContractTest(unittest.TestCase):
    def test_mkt_short_sale_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "13660"}], "pagination_key": "next"}

        with patch("j_quants_api_mcp.tools.market.get_raw_json", return_value=payload) as mock_get:
            result = market.mkt_short_sale(
                code="13660",
                disc_date="2024-08-01",
                disc_date_from="2024-08-01",
                disc_date_to="2024-08-31",
                calc_date="2024-07-31",
                pagination_key="cursor-1",
            )

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/markets/short-sale-report",
            params={
                "code": "13660",
                "disc_date": "2024-08-01",
                "disc_date_from": "2024-08-01",
                "disc_date_to": "2024-08-31",
                "calc_date": "2024-07-31",
                "pagination_key": "cursor-1",
            },
        )

    def test_mkt_short_sale_tool_is_registered_under_official_name(self) -> None:
        tool = mcp._tool_manager._tools["mkt-short-sale"]
        properties = tool.parameters["properties"]

        self.assertIn("disc_date", properties)
        self.assertIn("disc_date_from", properties)
        self.assertIn("disc_date_to", properties)
        self.assertIn("calc_date", properties)
        self.assertIn("pagination_key", properties)


if __name__ == "__main__":
    unittest.main()
