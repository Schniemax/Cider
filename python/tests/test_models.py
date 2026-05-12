import unittest

from cider_ws.models import CiderEvent


class ModelTests(unittest.TestCase):
    def test_event_parsing(self) -> None:
        event = CiderEvent.from_raw(
            {
                "status": 0,
                "message": "OK",
                "data": {"foo": "bar"},
                "type": "playbackStateUpdate",
            }
        )
        self.assertEqual(event.status, 0)
        self.assertEqual(event.message, "OK")
        self.assertEqual(event.data, {"foo": "bar"})
        self.assertEqual(event.type, "playbackStateUpdate")
        self.assertTrue(event.is_playback_update)

    def test_default_type(self) -> None:
        event = CiderEvent.from_raw({"status": 0})
        self.assertEqual(event.type, "generic")


if __name__ == "__main__":
    unittest.main()
