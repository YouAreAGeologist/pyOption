from src.options.calculators.asset_or_nothing_option_calculator import *


class OptionCalculatorFactory:
    @staticmethod
    def get_calculator(params, greeks):
        calculator = None
        try:
            if 'option_type' in params:
                option_type = params['option_type']
            else:
                raise NameError('option_type parameter is not in params dictionary.')

            if option_type == 'asset_or_nothing':
                calculator = AssetOrNothingOptionCalculator(params, greeks)
        except Exception:
            '''log exception'''

        return calculator
