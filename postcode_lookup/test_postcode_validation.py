import unittest

from postcode_lookup import is_valid

class TestPostCodeValidation(unittest.TestCase):

    def test_AA9A_9AA(self):
        self.assertTrue(is_valid("AA9A 9AA"))
    
    def test_A9A_9AA(self):
        self.assertTrue(is_valid("A9A 9AA"))
    
    def test_A9_9AA(self):
        self.assertTrue(is_valid("A9 9AA"))
    
    def test_A99_9AA(self):
        self.assertTrue(is_valid("A99 9AA"))
    
    def test_AA9A9_9AA(self):
        self.assertTrue(is_valid("AA9A9 9AA"))

    def test_lowercase(self):
        self.assertTrue(is_valid("aa9a 9aa"))

    def test_invalid(self):
        self.assertFalse(is_valid("XXX"))

if __name__ == "__main__":
    unittest.main()
    