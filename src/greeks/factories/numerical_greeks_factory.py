from src.options.types.asset_or_nothing_option import *


class NumericalGreeksFactory:
    @staticmethod
    def get_calculator(type, params, greeks):
        option = None
        if type == 'AssetOrNothingOption': AssetOrNothingOption(params, greeks)
