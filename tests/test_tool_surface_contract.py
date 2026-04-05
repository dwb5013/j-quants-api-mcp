import unittest

from j_quants_api_mcp.server import mcp


class ToolSurfaceContractTest(unittest.TestCase):
    def test_only_official_v2_endpoints_are_exposed(self) -> None:
        expected = {
            "drv-bars-daily-fut",
            "drv-bars-daily-opt",
            "drv-bars-daily-opt-225",
            "eq-bars-daily",
            "eq-bars-daily-am",
            "eq-bars-minute",
            "eq-earnings-cal",
            "eq-investor-types",
            "eq-master",
            "fin-details",
            "fin-dividend",
            "fin-summary",
            "idx-bars-daily",
            "idx-bars-daily-topix",
            "mkt-breakdown",
            "mkt-cal",
            "mkt-margin-alert",
            "mkt-margin-int",
            "mkt-short-ratio",
            "mkt-short-sale",
        }

        self.assertEqual(set(mcp._tool_manager._tools), expected)


if __name__ == "__main__":
    unittest.main()
