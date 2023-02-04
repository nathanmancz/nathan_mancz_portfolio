import unittest

from rental_property_roi import return_on_investment

class TestReturnOnInvestment(unittest.TestCase):

    def test_18k_250k(self):
        self.assertEqual(return_on_investment(18000, 250000), 0.072)

    def test_48k_750k(self):
        self.assertEqual(return_on_investment(48000, 750000), 0.064)
