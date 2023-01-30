import unittest

from postcode_lookup import get_area_name

class TestPostCodeLookup(unittest.TestCase):

    def test_GU32_3DE(self):
        self.assertEqual(get_area_name("GU32 3DE"), "Guildford")
    
    def test_PO19_1BF(self):
        self.assertEqual(get_area_name("PO19 1BF"), "Portsmouth")

    def test_SE16_2BT(self):
        self.assertEqual(get_area_name("SE16 2BT"), "South-East London")

    def test_L1_0PH(self):
        self.assertEqual(get_area_name("L1 0PH"), "Liverpool")

    def test_ZZ99_9ZZ(self):
        self.assertEqual(get_area_name("ZZ99 9ZZ"), "Postcode not found")

if __name__ == "__main__":
    unittest.main()