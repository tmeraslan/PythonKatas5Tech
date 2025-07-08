import unittest
from katas.is_unique import is_unique


class TestIsUnique(unittest.TestCase):
    def test_null_string(self):
        self.assertEqual(is_unique(''), True)
    
    def test_uniqe_string(self):
        self.assertEqual(is_unique('abcdef'), True)

    def test_not_uniqe_string(self):
        self.assertEqual(is_unique('abedb'), False)


