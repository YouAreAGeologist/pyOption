from src.options.european.vanilla_european_option import VanillaEuropeanOption
from src.greeks.calculators.numerical_greeks_calculator import NumericalGreeksCalculator


option = VanillaEuropeanOption('call', 100.0, 95.0, 0.1, 0.05, 0.5, 0.2)
print(option.get_value())

greeks = NumericalGreeksCalculator(option)
greeks.get_values(('delta', 'gamma'))