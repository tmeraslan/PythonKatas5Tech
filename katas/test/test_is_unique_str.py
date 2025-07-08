import unittest
from katas.is_unique_str import is_unique_str


class TestIsUnique(unittest.TestCase):
    def test_null_string(self):
        self.assertEqual(is_unique_str(''), True)
    
    def test_uniqe_string(self):
        self.assertEqual(is_unique_str('abcdef'), True)

    def test_not_uniqe_string(self):
        self.assertEqual(is_unique_str('abedb'), False)


