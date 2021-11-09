import sys
sys.path.insert(0, '..//celebrities_births./')
import unittest
from ..celebrities_births.date import Date
from ..celebrities_births.scraper import Scraper

class Test(unittest.TestCase):
    def test_tarantino(self):
        self.date = Date(27, 3, 1968)
        date_wiki = self.date.to_wiki_format()
        self.scraper = Scraper()
        celebrities = self.scraper.get_celebrities(date_wiki)
        self.assertIn('Quentin Tarantino', celebrities)