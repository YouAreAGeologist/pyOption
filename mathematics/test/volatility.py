import unittest
from collections import namedtuple
from mathematics.src.volatility import *


class VolatilityTest(unittest.TestCase):

    def setUp(self):
        price = namedtuple('price', 'date close high low')
        self.__prices = []
        self.__prices.append(price('01.Oct.XX', 132.5, 132.5, 131.0))
        self.__prices.append(price('04.Oct.XX', 133.5, 134.0, 131.0))
        self.__prices.append(price('O5.Oct.XX', 135.0, 136.0, 134.0))
        self.__prices.append(price('O6.Oct.XX', 133.0, 137.0, 133.0))
        self.__prices.append(price('O7.Oct.XX', 133.0, 136.0, 133.0))
        self.__prices.append(price('O8.Oct.XX', 137.0, 137.0, 133.0))
        self.__prices.append(price('11.Oct.XX', 135.0, 136.5, 135.0))
        self.__prices.append(price('12.Oct.XX', 135.0, 136.0, 135.0))
        self.__prices.append(price('13.Oct.XX', 142.5, 143.5, 137.0))
        self.__prices.append(price('14.Oct.XX', 143.0, 145.0, 142.0))
        self.__prices.append(price('15.Oct.XX', 144.5, 147.0, 142.0))
        self.__prices.append(price('18.Oct.XX', 145.0, 147.5, 145.0))
        self.__prices.append(price('19.Oct.XX', 146.0, 147.0, 143.0))
        self.__prices.append(price('20.Oct.XX', 149.0, 150.0, 148.0))
        self.__prices.append(price('21.Oct.XX', 148.0, 149.0, 146.5))
        self.__prices.append(price('22.Oct.XX', 147.0, 149.5, 147.0))
        self.__prices.append(price('25.Oct.XX', 147.0, 147.5, 146.0))
        self.__prices.append(price('26.Oct.XX', 147.0, 149.0, 146.5))
        self.__prices.append(price('27.Oct.XX', 145.0, 147.5, 144.5))
        self.__prices.append(price('28.Oct.XX', 145.0, 145.0, 144.0))
        self.__prices.append(price('29.Oct.XX', 150.0, 150.0, 143.5))

    def test_get_historical_volatility_from_close_prices(self):
        self.assertEqual(round(get_historical_volatility_from_close_prices(self.__prices), 4), 0.0173)


    def test_get_high_low_volatility(self):
        self.assertEqual(round(get_high_low_volatility(self.__prices), 4), 0.0126)


    def test_get_high_low_close_volatility(self):
        self.assertEqual(round(get_high_low_close_volatility(self.__prices), 4), 0.2038)




