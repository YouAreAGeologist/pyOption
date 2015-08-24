from abc import ABCMeta, abstractmethod
from src.options.factories.option_calculator_factory import OptionCalculatorFactory

class Option:
    def __init__(self, params, greeks):
        self.__params = params
        self.__greeks = greeks
        self.calculator = OptionCalculatorFactory.get_calculator(params, greeks)