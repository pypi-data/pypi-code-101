#%%
import sys
sys.path.insert(0, '..//celebrities_births./')
import unittest
from scraper import Scraper

class ScraperTest(unittest.TestCase):
    
    def setUp(self):
        self.list1 = Scraper()
        self.list2 = Scraper()

    def test_get_birth_header(self):
        self.assertTrue(self.list2._get_birth_header('February_2').find_all(id='Births'))

    def test_get_celebrities(self):
        with self.assertRaises(ValueError):
            self.list1._get_birth_header('February_30')


    def tearDown(self):
        del self.list1
        del self.list2
#%%
# unittest.main(argv=[''], verbosity=2, exit=False) 
