from src.option_pricers.types.vanilla_european_option_pricer import VanillaEuropeanOptionPricer
from src.option_pricers.types.asset_or_nothing_option_pricer import AssetOrNothingOptionPricer


class OptionPricerFactory:
    @staticmethod
    def get_pricer(params, greeks):
        calculator = None
        try:
            if 'option_type' in params:
                option_type = params['option_type']
            else:
                raise NameError('option_type parameter is not in params dictionary.')

            if option_type == 'asset_or_nothing':
                calculator = AssetOrNothingOptionPricer(params)
            elif option_type == 'vanilla_european':
                calculator = VanillaEuropeanOptionPricer(params)
        except Exception:
            '''log exception'''

        return calculator
