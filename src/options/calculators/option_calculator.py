import math
from src.option_pricers.factories.option_pricer_factory import OptionPricerFactory
from src.greeks.factories.greeks_factory import GreeksFactory
from src.mathematics.distributions.cumulative_normal_distribution import N


class OptionCalculator:
    def __init__(self, params, greeks):
        self.__params = params
        self.__greeks = greeks
        self.__option_pricer = OptionPricerFactory.get_pricer(params, greeks)
        self.__greeks_calculator = GreeksFactory.get_calculator(params, greeks)

    def get_price(self):
        return self.__option_pricer.get_price()

    def get_values(self):
        results = dict()
        results['price'] = self.__option_pricer.get_price()
        results['greeks'] = self.__greeks_calculator.get_values()
        return results

