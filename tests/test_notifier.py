import unittest
from unittest.mock import patch
from flight_tracker.notifier import send_discord_message

class TestNotifier(unittest.TestCase):

    @patch('flight_tracker.notifier.requests.post')
    def test_send_discord_message(self, mock_post):
        message = "Test message"
        send_discord_message(message)

        # Check if requests.post was called with the correct parameters
        mock_post.assert_called_once()
        headers = {"Content-Type": "application/json"}
        data = {"content": message}
        mock_post.assert_called_with('your_discord_webhook_url', headers=headers, data=data)

if __name__ == '__main__':
    unittest.main()