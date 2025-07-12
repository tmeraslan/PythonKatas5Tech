import unittest
from unittest.mock import Mock
from katas.do_n_times import do_n_times


class TestDoNTimes(unittest.TestCase):

    def test_func_called_n_times(self):
        mock_func = Mock()  # פונקציה מזויפת (mock)
        do_n_times(mock_func, 4)
        self.assertEqual(mock_func.call_count, 4)

    def test_func_not_called_when_n_is_zero(self):
        mock_func = Mock()
        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 0)

    def test_func_not_called_when_n_is_negative(self):
        mock_func = Mock()
        do_n_times(mock_func, -5)
        self.assertEqual(mock_func.call_count, 0)



