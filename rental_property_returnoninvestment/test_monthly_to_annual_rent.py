import unittest

from rental_property_roi import monthly_to_annual_rent

class TestMonthlyToAnnualRent(unittest.TestCase):

    def test_1200(self):
        self.assertEqual(monthly_to_annual_rent(1200), 14400)

    def test_4000(self):
        self.assertEqual(monthly_to_annual_rent(4000), 48000)

    def test_2100(self):
        self.assertEqual(monthly_to_annual_rent(2100), 25200)
