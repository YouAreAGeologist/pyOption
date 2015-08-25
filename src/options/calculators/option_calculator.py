from src.option_pricers.factories.option_pricer_factory import OptionPricerFactory
from src.greeks.factories.greeks_factory import GreeksFactory


class OptionCalculator:
    def __init__(self, params):
        self.__params = params
        self.__option_pricer = OptionPricerFactory.get_pricer(params)
        self.__greeks_calculator = GreeksFactory.get_calculator(params)

    def get_price(self):
        return self.__option_pricer.get_price()

    def get_values(self):
        results = dict()
        results['params'] = self.__params
        results['price'] = self.__option_pricer.get_price()
        results['greeks'] = self.__greeks_calculator.get_values()
        self.results = results

