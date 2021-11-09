import unittest
from project import scraper

class ScraperTest(unittest.TestCase):
    
    def setUp(self) -> None:
       self.scrape = scraper.Scraper()

    def test_get_celebs(self):
        self.assertIn('Rebecca Black', self.scrape.get_celebrities('June_21'))

unittest.main(argv=[''], verbosity=2, exit=True)
