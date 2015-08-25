from src.options.calculators.option_calculator import OptionCalculator

class Option:
    def __init__(self, params):
        self.__params = params
        self.calculator = OptionCalculator(params)

    def __repr__(self):
        description = '\nParameters\n'
        description += '--------------------\n'
        if self.calculator.results is not None:
            for k, v in self.calculator.results['params']['option'].items():
                description += k + ': ' + str(v) + '\n'
            description += '\nValue\n'
            description += '--------------------\n'
            description += 'price: ' + str(self.calculator.results['price']) + '\n'
            description += '\nGreeks\n'
            description += '--------------------\n'
            for k, v in self.calculator.results['greeks'].items():
                description += k + ': ' + str(v) + '\n'
        return description
