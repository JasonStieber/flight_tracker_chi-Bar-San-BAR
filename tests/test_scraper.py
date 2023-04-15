import unittest
from flight_tracker.scraper import scrape_flight_prices

class TestScraper(unittest.TestCase):

    def test_scrape_flight_prices(self):
        # Modify this test according to your specific flight search website and flight details
        flight_data = scrape_flight_prices()
        
        # Test if flight_data is a list
        self.assertIsInstance(flight_data, list)

        # Test if each item in flight_data is a tuple containing flight name and price
        for item in flight_data:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], float)

if __name__ == '__main__':
    unittest.main()