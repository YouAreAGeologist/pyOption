import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class VanillaEuropeanOptionPricer:
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
        t = option['t']
        sigma = option['sigma']

        d1 = (math.log(s / x) + (r - b + math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)

        if flag == 'call':
            result = (s * math.exp(-b * t) * N(d1)) - (x * math.exp(-r * t) * N(d2))
        elif flag == 'put':
            result = (x * math.exp(-r * t) * N(-d2)) - (s * math.exp(-b * t) * N(-d1))
        return result