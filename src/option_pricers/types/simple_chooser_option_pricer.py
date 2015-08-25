import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class SimpleChooserOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result=None
        option = self.__params['option']
        s = option['s']
        x = option['x']
        r = option['r']
        b = option['b']
        t1 = option['t1']
        t2 = option['t2']
        sigma = option['sigma']

        d = (math.log(s/x) + (b + 0.5 * math.pow(sigma, 2)) * t2) / (sigma * math.sqrt(t2))
        y = (math.log(s/x) + (b * t2) * 0.5 * math.pow(sigma, 2)) / (sigma * math.sqrt(t1))

        '''to do need M() function'''

        return 0