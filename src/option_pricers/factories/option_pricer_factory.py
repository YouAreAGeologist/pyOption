from src.option_pricers.types.vanilla_european_option_pricer import VanillaEuropeanOptionPricer
from src.option_pricers.types.cash_or_nothing_option_pricer import CashOrNothingOptionPricer
from src.option_pricers.types.asset_or_nothing_option_pricer import AssetOrNothingOptionPricer
from src.option_pricers.types.binary_single_barrier_option_pricer import BinarySingleBarrierOptionPricer
from src.option_pricers.types.variable_purchase_option_pricer import VariablePurchaseOptionPricer
from src.option_pricers.types.executive_stock_option_pricer import ExecutiveStockOptionPricer
from src.option_pricers.types.standard_power_option_pricer import StandardPowerOptionPricer
from src.option_pricers.types.capped_power_option_pricer import CappedPowerOptionPricer
from src.option_pricers.types.powered_option_pricer import PoweredOptionPricer
from src.option_pricers.types.time_switch_option_pricer import TimeSwitchOptionPricer
from src.option_pricers.types.simple_chooser_option_pricer import SimpleChooserOptionPricer
from src.option_pricers.types.forward_start_option_pricer import ForwardStartOptionPricer
from src.option_pricers.types.binary_double_barrier_option_pricer import BinaryDoubleBarrierOptionPricer
from src.option_pricers.types.geometric_average_rate_option_pricer import GeometricAverageRateOptionPricer
from src.option_pricers.types.supershare_option_pricer import SupershareOptionPricer
from src.option_pricers.types.gap_option_pricer import GapOptionPricer
from src.option_pricers.types.single_barrier_option_pricer import SingleBarrierOptionPricer
from src.option_pricers.types.double_barrier_option_pricer import DoubleBarrierOptionPricer
from src.option_pricers.types.floating_strike_lookback_option_pricer import FloatingStrikeLookbackOptionPricer
from src.option_pricers.types.fixed_strike_lookback_option_pricer import FixedStrikeLookbackOptionPricer
from src.option_pricers.types.partial_time_floating_strike_option_pricer import PartialTimeFloatingStrikeLookbackOptionPricer
from src.option_pricers.types.partial_time_fixed_strike_lookback_option_pricer import PartialTimeFixedStrikeLookbackOptionPricer
from src.option_pricers.types.mirror_option_pricer import MirrorOptionPricer
from src.option_pricers.types.fade_in_option_pricer import FadeInOptionPricer


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
            elif option_type == 'variable_purchase':
                calculator = VariablePurchaseOptionPricer(params)
            elif option_type == 'executive_stock':
                calculator = ExecutiveStockOptionPricer(params)
            elif option_type == 'standard_power':
                calculator = StandardPowerOptionPricer(params)
            elif option_type == 'capped_power':
                calculator = CappedPowerOptionPricer(params)
            elif option_type == 'powered':
                calculator = PoweredOptionPricer(params)
            elif option_type == 'forward_start':
                calculator = ForwardStartOptionPricer(params)
            elif option_type == 'fade_in':
                calculator = FadeInOptionPricer(params)
            # elif option_type == 'reset_strike_1':
            #     calculator = None
            # elif option_type == 'reset_strike_2':
            #     calculator = None
            elif option_type == 'time-switch':
                calculator = TimeSwitchOptionPricer(params)
            elif option_type == 'simple_chooser':
                calculator = SimpleChooserOptionPricer(params)
            # elif option_type == 'complex_chooser':
            #     calculator = None
            elif option_type == 'floating_strike_lookback':
                calculator = FloatingStrikeLookbackOptionPricer(params)
            elif option_type == 'fixed_strike_lookback':
                calculator = FixedStrikeLookbackOptionPricer(params)
            elif option_type == 'partial_time_floating_strike':
                calculator = PartialTimeFloatingStrikeLookbackOptionPricer(params)
            elif option_type == 'partial_time_floating_strike':
                calculator = PartialTimeFixedStrikeLookbackOptionPricer(params)
            # elif option_type == 'extreme_spread':
            #     calculator = None
            elif option_type == 'mirror':
                calculator = MirrorOptionPricer(params)
            elif option_type == 'single_barrier':
                calculator = SingleBarrierOptionPricer(params)
            # elif option_type == 'single_american_barrier':
            #     calculator = None
            elif option_type == 'double_barrier':
                calculator = DoubleBarrierOptionPricer(params)
            # elif option_type == 'partial_time_single_asset_barrier':
            #     calculator = None
            # elif option_type == 'look_barrier':
            #     calculator = None
            # elif option_type == 'discrete_barrier':
            #     calculator = None
            # elif option_type == 'soft_barrier':
            #     calculator = None
            elif option_type == 'gap':
                calculator = GapOptionPricer(params)
            elif option_type == 'cash_or_nothing':
                calculator = CashOrNothingOptionPricer(params)
            elif option_type == 'asset_or_nothing':
                calculator = AssetOrNothingOptionPricer(params)
            elif option_type == 'supershare':
                calculator = SupershareOptionPricer(params)
            elif option_type == 'binary_single_barrier':
                calculator = BinarySingleBarrierOptionPricer(params)
            elif option_type == 'binary_double_barrier':
                calculator = BinaryDoubleBarrierOptionPricer(params)
            elif option_type == 'geometric_average_rate':
                calculator = GeometricAverageRateOptionPricer(params)
            else:
                '''exception!'''

        except Exception:
            '''log exception'''

        return calculator
