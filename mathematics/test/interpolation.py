import unittest
import math
from mathematics.src.interpolation import *


class InterpolationTest(unittest.TestCase):


    def test_get_linear_interpolation(self):
        self.assertEqual(round(get_linear_interpolation(3.0, 4.0, 3.5, 0.063, 0.072), 4), 0.0675)


    def test_get_log_linear_interpolation(self):
        self.assertEqual(round(get_log_linear_interpolation(3.0, 4.0, 3.5, 0.063, 0.072), 4), 0.0674)


    def test_get_exponential_interpolation(self):
        self.assertEqual(round(get_exponential_interpolation(3.0, 4.0, 3.5, 0.063, 0.072), 4), 0.7959)


    def test_get_cubic_lagrange_interpolation(self):
        self.assertEqual(round(get_cubic_lagrange_interpolation(2.0, 3.0, 4.0, 5.0, 3.5, 0.064, 0.063, 0.072, 0.08), 4), 0.0694)

