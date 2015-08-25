import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class VariablePurchaseOptionPricer:
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
        l = option['l']
        u = option['u']
        d = option['d']
        t = option['t']
        sigma = option['sigma']

        d1 = (math.log(s/u) + (b + math.pow(sigma, 2)/2) * t) / (sigma * math.sqrt(t))
        d2 = d1 - (sigma * math.sqrt(t))
        d3 = (math.log(s/l) + (b + math.pow(sigma, 2)/2) * t) / (sigma * math.sqrt(t))
        d4 = d3 - (sigma * math.sqrt(t))
        d5 = (math.log(s/(l * (1 -d))) + (b + math.pow(sigma, 2)/2) * t) / (sigma * math.sqrt(t))
        d6 = d5 - (sigma * math.sqrt(t))

        n_min = x/(u * (1 - d))
        n_max = x/(l * (1 - d))

        a = math.exp(-r * t) * (x * d)/(1 - d)
        b = n_min * ((s * math.exp((b -r) * t) * N(d1))-(u * math.exp(-r * t) * N(d2)))
        c = n_max * ((l * math.exp(-r * t) * N(-d4)) - (s * math.exp((b - r) * t) * N(-d3)))
        d = n_max * ((l (1 - d) * math.exp(-r * t) * N(-d6)) - (s * math.exp((b - r) * t) * N(-d5)))

        if flag == 'call':
            result = a + b - c + d

