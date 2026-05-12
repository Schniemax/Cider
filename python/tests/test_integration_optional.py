import asyncio
import os
import unittest

from cider_ws.client import CiderWsClient


@unittest.skipUnless(os.getenv("CIDER_WS_INTEGRATION") == "1", "Set CIDER_WS_INTEGRATION=1 to run")
class IntegrationTests(unittest.TestCase):
    def test_status_roundtrip(self) -> None:
        async def _run() -> None:
            async with CiderWsClient() as client:
                event = await client.status()
                self.assertIsNotNone(event.message)

        asyncio.run(_run())


if __name__ == "__main__":
    unittest.main()
