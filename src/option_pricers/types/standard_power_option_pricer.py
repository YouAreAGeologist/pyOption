import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class StandardPowerOptionPricer:
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

        d1 = (math.log(s/math.pow(x,-i)) + (b + (i - 0.5) * math.pow(sigma, 2)) * t) / (sigma * math.sqrt(t))
        d2 = d1 - i * sigma * math.sqrt(t)

        if flag == 'call':
            result = (math.pow(s, i) * math.exp(((i - 1) * (r + i * math.pow(sigma,2)/2) - i * (r - b) * t)) * N(d1)) - (x * math.exp(-r * t) * N(d2))
        elif flag == 'put':
            result =  (x * math.exp(-r * t) * N(-d2)) - (math.pow(s, i) * math.exp(((i - 1) * (r + i * math.pow(sigma,2)/2) - i * (r - b) * t)) * N(-d1))
        return result