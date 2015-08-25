from src.option_pricers.types.vanilla_european_option_pricer import VanillaEuropeanOptionPricer
from src.option_pricers.types.cash_or_nothing_option import CashOrNothingOptionPricer
from src.option_pricers.types.asset_or_nothing_option_pricer import AssetOrNothingOptionPricer


class OptionPricerFactory:
    @staticmethod
    def get_pricer(params):
        calculator = None
        try:
            if 'option_type' in params['option']:
                option_type = params['option']['option_type']
            else:
                raise NameError('option_type parameter is not in option dictionary.')

            if option_type == 'vanilla_european':
                calculator = VanillaEuropeanOptionPricer(params)
            if option_type == 'fx_european':
                calculator = None
            elif option_type == 'variable_purchase':
                calculator = None
            elif option_type == 'executive_stock':
                calculator = None
            elif option_type == 'moneyness':
                calculator = None
            elif option_type == 'power_contract':
                calculator = None
            elif option_type == 'standard_power':
                calculator = None
            elif option_type == 'capped-power':
                calculator = None
            elif option_type == 'powered':
                calculator = None
            elif option_type == 'log_s':
                calculator = None
            elif option_type == 'log':
                calculator = None
            elif option_type == 'forward_start':
                calculator = None
            elif option_type == 'fade_in':
                calculator = None
            elif option_type == 'ratchet':
                calculator = None
            elif option_type == 'reset_strike_1':
                calculator = None
            elif option_type == 'reset_strike_2':
                calculator = None
            elif option_type == 'time-switch':
                calculator = None
            elif option_type == 'simple_chooser':
                calculator = None
            elif option_type == 'complex_chooser':
                calculator = None
            elif option_type == 'floating_strike_lookback':
                calculator = None
            elif option_type == 'fixed_strike_lookback':
                calculator = None
            elif option_type == 'partial_time_floating_strike':
                calculator = None
            elif option_type == 'partial_time_floating_strike':
                calculator = None
            elif option_type == 'extreme_spread':
                calculator = None
            elif option_type == 'mirror':
                calculator = None
            elif option_type == 'single_barrier':
                calculator = None
            elif option_type == 'single_american_barrier':
                calculator = None
            elif option_type == 'double_barrier':
                calculator = None
            elif option_type == 'partial_time_single_asset_barrier':
                calculator = None
            elif option_type == 'look_barrier':
                calculator = None
            elif option_type == 'discrete_barrier':
                calculator = None
            elif option_type == 'soft_barrier':
                calculator = None
            elif option_type == 'gap':
                calculator = None
            elif option_type == 'cash_or_nothing':
                calculator = CashOrNothingOptionPricer(params)
            elif option_type == 'asset_or_nothing':
                calculator = AssetOrNothingOptionPricer(params)
            elif option_type == 'supershare':
                calculator = None
            elif option_type == 'binary_single_barrier':
                calculator = None
            elif option_type == 'binary_double_barrier':
                calculator = None
            elif option_type == 'geometric_average_rate':
                calculator = None
            elif option_type == 'arithmetic_average_rate':
                calculator = None
            elif option_type == 'discrete_arithmetic_average_rate':
                calculator = None


        except Exception:
            '''log exception'''

        return calculator
