import unittest

from cider_ws import commands


class CommandTests(unittest.TestCase):
    def test_playpause(self) -> None:
        self.assertEqual(commands.playpause(), {"action": "playpause"})

    def test_search_payload(self) -> None:
        payload = commands.search("Daft Punk", limit=5)
        self.assertEqual(payload["action"], "search")
        self.assertEqual(payload["term"], "Daft Punk")
        self.assertEqual(payload["limit"], 5)

    def test_library_change_payload(self) -> None:
        payload = commands.change_library("songs", "123", True)
        self.assertEqual(
            payload,
            {
                "action": "change-library",
                "type": "songs",
                "id": "123",
                "add": True,
            },
        )


if __name__ == "__main__":
    unittest.main()
