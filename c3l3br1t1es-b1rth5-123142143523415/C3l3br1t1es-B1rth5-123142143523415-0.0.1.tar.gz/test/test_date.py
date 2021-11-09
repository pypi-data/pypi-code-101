
import unittest
from project import date

class DateTests(unittest.TestCase):
    
    def setUp(self):
        self.new_date = date.Date(10, 10, 2021)

    def test_date_valid(self):
        self.assertRaises(ValueError)

    def test_lt(self):
        other_date = date.Date(30, 11, 1997)
        self.assertTrue(other_date < self.new_date)
        
    def test_leap_year(self):
        self.assertTrue(date.Date.is_leap_year(2021) == False)

t=(3)

unittest.main(argv=[''], verbosity=2, exit=True)
