import math

from src.mathematics.distributions.cumulative_normal_distribution import N
from src.options.types.option_base import OptionBase


class AssetOrNothingOption(OptionBase):
    def __init__(self, params, greeks=None):
        self.__flag = params['flag']
        self.__s = params['s']
        self.__x = params['x']
        self.__r = params['r']
        self.__b = params['b']
        self.__t = params['t']
        self.__sigma = params['sigma']
        self.__d = (math.log(self.s / self.x) + (self.b + math.pow(self.__sigma, 2)/2) * self.__t) / (self.__sigma * math.sqrt(self.__t))

        -- get pricer for optiontype

        -- get greeks calculator for option type

        if greeks:
            self.__greeksCalculator = NumericalGreeks(type(self))

    def get_values(self):
        results = {}

        if self.__flag == 'c':
            price = self.__s * math.exp((self.__b - self.__r) * self.__t) * N(self.__d)
        elif self.__flag == 'p':
            price = self.__s * math.exp((self.__b - self.__r) * self.__t) * N(-self.__d)

        results['price'] = price
        results['greeks'] = greeks --dictionary of greeks inside current dictionary

        return results

    def get_analytic_price(self):
        result = None
        if self.__flag == 'c':
            price = self.__s * math.exp((self.__b - self.__r) * self.__t) * N(self.__d)
        elif self.__flag == 'p':
            price = self.__s * math.exp((self.__b - self.__r) * self.__t) * N(-self.__d)
        return result


