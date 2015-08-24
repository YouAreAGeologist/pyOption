from src.options.calculators.option_calculator import OptionCalculator

class Option:
    def __init__(self, params, greeks):
        self.__params = params
        self.__greeks = greeks
        self.calculator = OptionCalculator(params, greeks)