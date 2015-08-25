import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class TimeSwitchOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result=None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        x = option['x']
        a = option['a']
        r = option['r']
        b = option['b']
        i = option['i']
        t = option['t']
        dt = option['dt']
        sigma = option['sigma']

        n = t/dt
        sum = 0
        if flag == 'call':
            for i in range(i, n+1):
                result += N((math.log(s/x) + (b - 0.5 * math.pow(sigma, 2) * i * dt))/(sigma * math.sqrt(i * dt))) * dt
        elif flag == 'put':
            for i in range(i, n+1):
                result += N((-math.log(s/x) - (b - 0.5 * math.pow(sigma, 2) * i * dt))/(sigma * math.sqrt(i * dt))) * dt
        return a * math.exp(-r * t) * sum