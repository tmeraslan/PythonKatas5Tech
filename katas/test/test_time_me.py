import unittest
import time
from katas.time_me import measure_execution_time

def sample_function():
       time.sleep(0.5)


def quick_function():
       print("Quick task done!")

def fun():
       time.sleep(1.5)

class TestMeasureExecutionTimeSimple(unittest.TestCase):

    def test_function_greater500(self):
        self.assertEqual(measure_execution_time(sample_function), 500 )

    def test_function_smaller_1(self):
        self.assertEqual(measure_execution_time(quick_function), 1 )




