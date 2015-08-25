import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class CappedPowerOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result=None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        x = option['x']
        r = option['r']
        b = option['b']
        i = option['i']
        t = option['t']
        sigma = option['sigma']

        if flag == 'call':
            result = None
        elif flag == 'put':
            result = None
        return result