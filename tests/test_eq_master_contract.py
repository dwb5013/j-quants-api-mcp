import json
import unittest
from unittest.mock import Mock, patch

from j_quants_api_mcp import client
from j_quants_api_mcp.tools import equity


class GetRawJsonTest(unittest.TestCase):
    def test_get_raw_json_preserves_official_payload(self) -> None:
        payload = {"data": [{"Code": "86970"}]}
        response = Mock()
        response.json.return_value = payload

        fake_client = Mock()
        fake_client.JQUANTS_API_BASE = "https://api.jquants.com/v2"
        fake_client._get.return_value = response

        with patch("j_quants_api_mcp.client.get_client", return_value=fake_client):
            result = client.get_raw_json(
                "/equities/master",
                params={"code": "86970", "date": "2024-01-04"},
            )

        self.assertEqual(result, payload)
        fake_client._get.assert_called_once_with(
            "https://api.jquants.com/v2/equities/master",
            params={"code": "86970", "date": "2024-01-04"},
        )


class EqMasterContractTest(unittest.TestCase):
    def test_eq_master_uses_official_path_and_params(self) -> None:
        payload = {"data": [{"Code": "86970"}]}

        with patch("j_quants_api_mcp.tools.equity.get_raw_json", return_value=payload) as mock_get:
            result = equity.eq_master(code="86970", date="2024-01-04")

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with(
            "/equities/master",
            params={"code": "86970", "date": "2024-01-04"},
        )

    def test_eq_master_omits_empty_query_params(self) -> None:
        payload = {"data": []}

        with patch("j_quants_api_mcp.tools.equity.get_raw_json", return_value=payload) as mock_get:
            result = equity.eq_master()

        self.assertEqual(json.loads(result), payload)
        mock_get.assert_called_once_with("/equities/master", params=None)


if __name__ == "__main__":
    unittest.main()
