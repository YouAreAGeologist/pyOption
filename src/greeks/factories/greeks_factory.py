from src.greeks.calculators.numerical_greeks_calculator import NumericalGreeksCalculator


class GreeksFactory:
    @staticmethod
    def get_calculator(params, greeks):
        return NumericalGreeksCalculator(params, greeks)
