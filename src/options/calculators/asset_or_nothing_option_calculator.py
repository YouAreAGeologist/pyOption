import math
from src.options.calculators.config import required_paremeters
from src.greeks.factories.greeks_factory import GreeksFactory
from src.mathematics.distributions.cumulative_normal_distribution import N


class AssetOrNothingOptionCalculator:
    def __init__(self, params, greeks):
        if all(params.keys() in required_paremeters['asset_or_nothing']):
            self.__params = params
            self.__greeks = greeks
            self.__greeksCalculator = GreeksFactory.get_calculator(params, greeks)

    def get_values(self):
        results = dict()
        results['price'] = self.__get_price()
        results['greeks'] = self.__get_greeks()
        return results

    def __get_price(self):
        result = None
        params = self.__params
        flag, s, x, r, b, t, sigma = params['flag'], params['s'], params['x'], params['r'], params['b'], params['t'], params['sigma']
        d = 1
        if flag == 'call':
            result = s * math.exp((b - r) * t) * N(d)
        elif flag == 'put':
            result = s * math.exp((b - r) * t) * N(-d)
        return result

    def __get_greeks(self):
        result = {}
        return result


