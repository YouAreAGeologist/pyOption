import math
from src.mathematics.distributions.cumulative_normal_distribution import N

class AssetOrNothingOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result = None
        params = self.__params['option']
        flag, s, x, r, b, t, sigma = params['flag'], params['s'], params['x'], params['r'], params['b'], params['t'], params['sigma']
        d = (math.log(s / x) + (b + math.pow(sigma, 2)/2) * t) / (sigma * math.sqrt(t))
        if flag == 'call':
            result = s * math.exp((b - r) * t) * N(d)
        elif flag == 'put':
            result = s * math.exp((b - r) * t) * N(-d)
        return result
