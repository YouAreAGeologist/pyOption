from src.greeks.factories.numerical_greeks_factory import NumericalGreeksFactory
from src.options.enums.option_type import OptionType


class OptionBase(object):
    def __init__(self, params, greeks):
        self.__params = params
        self.__greeks = greeks
        self.__optionCalculator = None
        self.__greeksCalculator = NumericalGreeksFactory.get_calculator(OptionType, params, greeks)