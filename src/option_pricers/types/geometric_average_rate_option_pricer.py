import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class GeometricAverageRateOptionPricer:
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

        sigma_a = sigma/math.sqrt(3)
        b_a = 0.5 * (b - math.pow(sigma, 2)/6)
        d1 = (math.log(s/x) + (b_a + 0.5 * math.pow(sigma_a, 2)) * t)/(sigma_a * math.sqrt(t))
        d2 = d1 - (sigma * math.sqrt(t))

        if flag == 'call':
            result = (s * math.exp((b_a - r) * t) * N(d1)) - (x * math.exp(-r * t) * N(d2))
        elif flag == 'put':
            result = (x * math.exp(-r * t) * N(-d2)) - (s * math.exp((b_a - r) * t) * N(-d1))
        return result
