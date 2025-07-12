import unittest
from katas.sum_of_digits import sum_of_digits  # נניח שהפונקציה בקובץ בשם main.py


class TestSumOfDigits(unittest.TestCase):
    def test_mixed_characters(self):
        self.assertEqual(sum_of_digits("abc123"), 6)

    def test_text_with_spaces_and_digits(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_only_digits(self):
        self.assertEqual(sum_of_digits("9876543210"), 45)


    def test_special_characters(self):
        self.assertEqual(sum_of_digits("a!@3#b$2%"), 5)