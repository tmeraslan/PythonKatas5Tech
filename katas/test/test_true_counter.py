
import unittest

from katas.true_counter import count_true_values

class TestCountTrueValues(unittest.TestCase):

    def test_mixed_values(self):
        self.assertEqual(count_true_values([True,False,True,False]),2)

    def test_all_true(self):
        self.assertEqual(count_true_values([True,True,True,True]),4)

    def test_all_false(self):
        self.assertEqual(count_true_values([False,False,False,False]),0)

    def test_non_boolean_values(self):
        self.assertEqual(count_true_values([1,0,None,True,False]),1)