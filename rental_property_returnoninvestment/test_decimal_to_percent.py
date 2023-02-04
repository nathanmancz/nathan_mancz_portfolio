import unittest

from rental_property_roi import decimal_to_percent

class TestRentalPropertyRoi(unittest.TestCase):

    def test_21_percent(self):
        self.assertEqual(decimal_to_percent(0.21), "21.00%")

    def test_3_percent(self):
        self.assertEqual(decimal_to_percent(0.03), "3.00%")