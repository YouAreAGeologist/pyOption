import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class MirrorOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result=None
        option = self.__params['option']
        flag = option['flag']
        position = option['position']
        s = option['s']
        x = option['x']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        f = None
        if position == 'long':
            f = s * math.exp(0.5 * math.pow(sigma, 2)) + math.fabs(b - math.pow(sigma, 2)/2) * t
        elif position == 'short':
            f = s * math.exp(0.5 * math.pow(sigma, 2)) - math.fabs(b - math.pow(sigma, 2)/2) * t

        d1 = (math.log(s/x) + (t * math.pow(sigma, 2)/2))/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)

        if flag == 'call':
            result = math.exp(-r*t) * ((f * N(d1)) - (x * N(d2)))
        elif flag == 'put':
            result = math.exp(-r*t) * ((x * N(-d2)) - (f * N(-d1)))
        return result