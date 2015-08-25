import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class AssetOrNothingOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        x = option['x']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        d = (math.log(s / x) + (b + math.pow(sigma, 2)/2) * t) / (sigma * math.sqrt(t))

        if flag == 'call':
            result = s * math.exp((b - r) * t) * N(d)
        elif flag == 'put':
            result = s * math.exp((b - r) * t) * N(-d)
        return result