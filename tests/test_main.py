import unittest
from unittest.mock import patch
from flight_tracker.main import main

class TestMain(unittest.TestCase):

    @patch('flight_tracker.scraper.scrape_flight_prices')
    @patch('flight_tracker.notifier.send_discord_message')
    def test_main(self, mock_send_discord_message, mock_scrape_flight_prices):
        # Set up the mock data
        mock_scrape_flight_prices.return_value = [
            ('Flight 1', 100),
            ('Flight 2', 150)
        ]

        # Call the main function
        main()

        # Check if the send_discord_message function was called with the correct messages
        mock_send_discord_message.assert_any_call('Flight 1 is now available for $100.')
        mock_send_discord_message.assert_any_call('Flight 2 is now available for $150.')

if __name__ == '__main__':
    unittest.main()