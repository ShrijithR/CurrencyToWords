import unittest

from CurrencyToWords import convert
from src.Support_Functions import CheckInput
from src.Support_Functions import Str_List

class TestConvert(unittest.TestCase):
    def test_Correct_A(self):
        self.assertEqual(
            convert(123456.78), 
            "Rs. One Lakh Twenty Three Thousand Four Hundred and Fifty Six 78/100 ONLY"
            )
    def test_Correct_B(self):
        self.assertTrue(
            CheckInput('90005.00')
            )
    def test_ToFloat(self):
        return_value = Str_List('2340')
        self.assertIsInstance(return_value[0], str)
        self.assertIsInstance(return_value[1], list)
        self.assertIsInstance(return_value[2], int) 
    def test_Zero(self):
        self.assertEqual(
            convert(0),
            "Rs. Zero"
        )
    def test_InvalidCharacter(self):
        self.assertEqual(
            CheckInput('sdd'),
            "Invalid input"
        )
    def test_NumberOfDots(self):
        self.assertEqual(
            convert('34.56.34'),
            "Invalid input"
        )
    def test_DecimalLimit(self):
        self.assertEqual(
            convert(234.5436),
            "Invalid input"
        )
    def test_StartWithDigit(self):
        self.assertEqual(
            convert('.05'),
            "Invalid input"
        )
    def test_EndWithDigit(self):
        self.assertEqual(
            convert('0.3a'),
            "Invalid input"
        )
    def test_caseA(self):
        self.assertEqual(
            convert(-2),
            "Number not within the limit"
        )
    def test_caseA(self):
        self.assertEqual(
            convert(9849576),
            "Number not within the limit"
        )

if __name__ == "__main__":
    unittest.main()
