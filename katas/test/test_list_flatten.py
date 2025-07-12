import unittest
from katas.list_flatten import flatten_list  


class TestFlattenList(unittest.TestCase):

    def test_flatten_regular_nested_list(self):
        nested = [1, [2, 3], [4, [5, 6]], 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_flatten_no_nesting(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_flatten_deeply_nested_list(self):
        self.assertEqual(flatten_list([[[[[1]]]]]), [1])

    def test_flatten_nested_with_empty_lists(self):
        nested = [[], [1, [], [2, []]], 3]
        expected = [1, 2, 3]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_only_empty_lists(self):
        nested = [[], [[]], [[[]]]]
        expected = []
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_list_with_multiple_data_types(self):
        nested = [1, ["a", [2]], [3]]
        expected = [1, "a", 2, 3]
        self.assertEqual(flatten_list(nested), expected)


