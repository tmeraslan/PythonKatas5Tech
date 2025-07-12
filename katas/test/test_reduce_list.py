import unittest
from katas.reduce_list import reduce_array  # מניח שהפונקציה בקובץ main.py


class TestReduceArray(unittest.TestCase):

    def test_regular_list(self):
        numbers = [10, 15, 7, 20, 25]
        reduce_array(numbers)
        self.assertEqual(numbers, [10, 5, -8, 13, 5])

    def test_empty_list(self):
        numbers = []
        reduce_array(numbers)
        self.assertEqual(numbers, [])

    def test_single_element(self):
        numbers = [42]
        reduce_array(numbers)
        self.assertEqual(numbers, [42])


    def test_all_same_elements(self):
        numbers = [7, 7, 7, 7]
        reduce_array(numbers)
        self.assertEqual(numbers, [7, 0, 0, 0])



