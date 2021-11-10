#%%
import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest
from celebrity_births.celebrities_births import Date
from celebrity_births.celebrities_births import Scraper

# %%
#  Include a class that checks that the Date class works fine. 
#  Add at least 3 unit tests (For example, check the `__lt__`, `date_valid`, and `from_string` methods return what they are expected to return). 
#  If you expect a date that is not valid, you can use 
#  [assertRaise](https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects) 
#  for example: `with self.assertRaises(ValueError) as err: Date(32, 5, 2020)`

class DateTest(unittest.TestCase):
    
    def test_lt(self):
        date_1 = Date(10, 10, 2021)
        date_2 = Date(1, 11, 2021)
        self.assertLess(date_1, date_2)
        
    def test_eq(self):
        date_1 = Date(10, 12, 2021)
        date_2 = Date(11, 12, 2021)
        date_3 = Date(10, 12, 2021)
        self.assertNotEqual(date_1, date_2)
        self.assertEqual(date_1, date_3)
    
    def test_from_string(self):
        date_1 = Date(10, 11, 2021)
        date_2 = Date.from_string('10-11-2021')
        self.assertEqual(date_1, date_2)
        
    def test_date_valid(self):
        with self.assertRaises(ValueError) as err:
           Date(40, 12, 1980)
           
    def test_to_wiki_format(self):
        self.assertEqual(Date(31, 7, 2010).to_wiki_format(), "July_31")
        
    
unittest.main(argv=[''], verbosity=2, exit=False)
# %%

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_get_celebrities_invalid_date(self):
        date = 'June_31'
        with self.assertRaises(ValueError) as err:
            self.scraper.get_celebrities(date)
    
    def test_get_celebrities_valid_date(self):
        date = 'January_1'
        self.assertEqual(type(self.scraper.get_celebrities(date)), list)    
      
    def test_get_birth_header(self):  
        header = self.scraper._get_birth_header('December_30').text
        # print(header)
        self.assertEqual(header, 'Births[edit]')
      
    def test_clean_li(self):
        cel_list = self.scraper._get_celebrity_list('December_30')
        for li in cel_list:
            name = self.scraper._clean_li(li)
            self.assertEqual(name.find(','), -1)


unittest.main(argv=[''], verbosity=2, exit=False)
# %%

class IntegrationTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.date = Date(27, 3, 2020)
        self.scraper = Scraper()
        
    def test_get_celebrities_by_date(self):
        self.assertIn("Quentin Tarantino", self.scraper.get_celebrities(self.date.to_wiki_format()))
        
unittest.main(argv=[''], verbosity=2, exit=False)

        
# %%
