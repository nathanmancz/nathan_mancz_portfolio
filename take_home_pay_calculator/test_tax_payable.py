import unittest

from take_home_pay_calculator import tax_payable 

class TestTaxPayable(unittest.TestCase):

    def test_27000(self):
        self.assertEqual(tax_payable(27000), 2616)
    
    def test_65000(self):
        self.assertEqual(tax_payable(65000), 12132)

    def test_10000(self):
        self.assertEqual(tax_payable(10000), 0)


if __name__ == "__main__":
    unittest.main()