import unittest
import math
from core.src.vanilla_european_option_numerical_greeks import VanillaEuropeanOptionNumbericalGreeks


class VanillaEuropeanOptionNumbericalGreeksTest(unittest.TestCase):
    def setUp(self):
        self.__test_greeks = dict[
                             'delta': 0.5031,
                             'gamma': 0.0268,
                             'theta': -0.0371,
                             'vega': 0.1930,
                             'rho': 0.1097,
                             'rho_futures': -0.0121,
                             'rho_2': -0.1233,
                             'rho_carry': 0.1233
                             ]

        option = VanillaEuropeanOptionNumbericalGreeks('c', 98.0, 100.0, 0.1, 0.05, 0.25, 0.3, self.__test__greeks)
        self.__calculated_greeks = option.get_greeks()
        self.__calculated_greeks_keys = self.__calculated_greeks.keys()

    def test_delta(self):
        self.assertTrue('delta' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['delta'], round(self.__calculated_greeks['delta'], 4))

    def test_gamma(self):
        self.assertTrue('gamma' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['gamma'], round(self.__calculated_greeks['gamma'], 4))

    def test_theta(self):
        self.assertTrue('theta' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['theta'], round( self.__calculated_greeks['theta'], 4))

    def test_vega(self):
        self.assertTrue('vega' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['vega'], round(self.__calculated_greeks['vega'], 4))

    def test_rho(self):
        self.assertTrue('rho' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['rho'], round(self.__calculated_greeks['rho'], 4))

    def test_rho_futures(self):
        self.assertTrue('rho_futures' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['rho_futures'], round(self.__calculated_greeks['rho_futures'], 4))

    def test_rho_2(self):
        self.assertTrue('rho_2' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['rho_2'], round(self.__calculated_greeks['rho_2'], 4))

    def test_rho_carry(self):
        self.assertTrue('rho_carry' in self.__calculated_greeks_keys)
        self.assertEqual(self.__test_greeks['rho_carry'], round(self.__calculated_greeks['rho_carry'], 4))
