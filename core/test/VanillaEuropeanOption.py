import unittest
import math
from core.src.VanillaEuropeanOption import VanillaEuropeanOption
from mathematics.src.distribution import ndf, cnd

class VanillaEuropeanOptionTest(unittest.TestCase):


    def test_get_price_put(self):
        option = VanillaEuropeanOption('p', 100, 95, 0.1, 0.05, 0.5, 0.2)
        self.assertEqual(round(option.get_price(), 4), 2.4648)


    def test_get_delta_call(self):
        option = VanillaEuropeanOption('c', 105, 100, 0.1, 0, 0.5, 0.36)
        self.assertEqual(round(option.get_delta(), 4), 0.5946)


    def test_get_delta_put(self):
        option = VanillaEuropeanOption('p', 105, 100, 0.1, 0, 0.5, 0.36)
        self.assertEqual(round(option.get_delta(), 4), -0.3566)


    def test_get_gamma(self):
        option = VanillaEuropeanOption('c', 55, 60, 0.1, 0.1, 0.75, 0.3)
        self.assertEqual(round(option.get_gamma(), 4), 0.0278)
