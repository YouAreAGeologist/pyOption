import math
from src.mathematics.distributions.cumulative_normal_distribution import N
from src.mathematics.distributions.cumulative_bivariate_normal_distribution import M


class FloatingStrikeLookbackOptionPricer:
    def __init__(self, params):

        '''do params checking for s_min/s_max for calls and puts'''


        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        s_min = option['s_min']
        s_max = option['s_max']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        if flag == 'call':
            a1 = (math.log(s/s_min) + (b + 0.5 * math.pow(sigma, 2)) * t)/(sigma * math.sqrt(t))
            a2 = a1 - sigma * math.sqrt(t)
            result = s * math.exp((b-r)*t) * N(a1) - (s_min * math.exp(-r*t) * N(a2)) + ((s * math.exp(-r*t) * 0.5 * math.pow(sigma, 2)/b) * (math.pow(s/s_min, -2*b/math.pow(sigma, 2)) * N(-a1 + (2 * b * math.sqrt(t)/sigma) - (math.exp(b*t) * N(-a1)))))
        elif flag == 'put':
            b1 = (math.log(s/s_min) + (b + 0.5 * math.pow(sigma, 2)) * t)/(sigma * math.sqrt(t))
            b2 = b1 - sigma * math.sqrt(t)
            result = s_max * math.exp(-r*t) * N(-b2) - (s * math.exp((b-r)*t) * N(-b1)) + (s * math.exp(-r*t) * math.pow(sigma, 2)/(2*b)) + ((s * math.exp(-r*t) * math.pow(sigma, 2)/(2 * b)) * (-(math.pow(s/s_max, -2*b/math.pow(sigma, 2)) * N(b1 - 2 * b * math.sqrt(t)/sigma)) + (math.exp(b*t) * N(b1))))
        return result
