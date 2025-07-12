import unittest
from katas.longest_common_prefix import longest_common_prefix  # שנה לפי הנתיב אצלך


class TestLongestCommonPrefix(unittest.TestCase):

    def test_common_prefix_exists(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(strs), "fl")

    def test_no_common_prefix(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(longest_common_prefix(strs), "")

    def test_full_match(self):
        strs = ["test", "test", "test"]
        self.assertEqual(longest_common_prefix(strs), "test")



    def test_prefix_of_one_letter(self):
        strs = ["apple", "apricot", "ape"]
        self.assertEqual(longest_common_prefix(strs), "ap")

    def test_one_string_only(self):
        strs = ["alone"]
        self.assertEqual(longest_common_prefix(strs), "alone")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_contains_empty_string(self):
        strs = ["prefix", ""]
        self.assertEqual(longest_common_prefix(strs), "")

    def test_all_empty_strings(self):
        strs = ["", "", ""]
        self.assertEqual(longest_common_prefix(strs), "")

    def test_mixed_case(self):
        strs = ["Case", "casing"]
        self.assertEqual(longest_common_prefix(strs), "")  # Case-sensitive