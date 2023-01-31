import unittest

from take_home_pay_calculator import pension_payable

class TestPensionPayable(unittest.TestCase):

    def test27000_5_percent(self):
        self.assertEqual(pension_payable(27000, "Y", 5), 1350)

    def test65000_3_percent(self):
        self.assertEqual(pension_payable(65000, "Y", 3), 1950)

    def test10000_no_pension(self):
        self.assertEqual(pension_payable(10000, "N", 0), 0)


if __name__ == "__main__":
    unittest.main()