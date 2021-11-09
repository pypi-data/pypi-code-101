#%%
import sys
sys.path.insert(0, '../celebrities_births/')
import unittest
from date import Date


class DateTest(unittest.TestCase):
    
    def setUp(self):
        self.date1 = Date(2, 2, 2020)
        self.date2 = Date(4, 5, 2021)

    def test__eq__(self):
        self.assertEqual(self.date1, self.date1)
        self.assertNotEqual(self.date1, self.date2)

    def test__lt__(self):
        self.assertTrue(self.date1 < self.date2)

    def test_from_string(self):
        self.assertEqual(self.date1, Date.from_string('2-2-2020'))

    def test_date_valid(self):
        self.assertTrue(self.date1.is_date_valid(self.date1.day, self.date1.month, self.date1.year))

    def tearDown(self):
        del self.date1
        del self.date2
#%%
# unittest.main(argv=[''], verbosity=2, exit=False) 
