import unittest
from flight_tracker.config import PRICE_THRESHOLD, FLIGHT_LIST, DISCORD_WEBHOOK_URL

class TestConfig(unittest.TestCase):

    def test_price_threshold(self):
        self.assertIsInstance(PRICE_THRESHOLD, (int, float))
        self.assertGreater(PRICE_THRESHOLD, 0)

    def test_flight_list(self):
        self.assertIsInstance(FLIGHT_LIST, list)
        for flight in FLIGHT_LIST:
            self.assertIsInstance(flight, str)

    def test_discord_webhook_url(self):
        self.assertIsInstance(DISCORD_WEBHOOK_URL, str)
        self.assertTrue(DISCORD_WEBHOOK_URL.startswith('https://'))

if __name__ == '__main__':
    unittest.main()