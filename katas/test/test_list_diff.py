import unittest
from katas.list_diff import find_difference


class TestIsUnique(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_single_element(self):
        self.assertEqual(find_difference([7]), 0)

    def test_all_same_elements(self):
        self.assertEqual(find_difference([4, 4, 4, 4]), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_difference([-10, -5, -3, -20]), 17)

    def test_mixed_positive_negative(self):
        self.assertEqual(find_difference([-100, 0, 100]), 200)

    def test_two_elements(self):
        self.assertEqual(find_difference([8, 3]), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):  # min/max will raise ValueError on empty list
            find_difference([]) 
        
    
