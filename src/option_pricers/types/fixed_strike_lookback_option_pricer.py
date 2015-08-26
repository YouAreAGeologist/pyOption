import math
from src.mathematics.distributions.cumulative_normal_distribution import N
from src.mathematics.distributions.cumulative_bivariate_normal_distribution import M


class FixedStrikeLookbackOptionPricer:
    def __init__(self, params):

        """
        do params checking for s_min/s_max for calls and puts
        """

        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        s_min = option['s_min']
        s_max = option['s_max']
        x = option['x']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        if flag == 'call':
            if x > s_max:
                d1 = math.log(s/x) + (b + 0.5 * math.pow(sigma, 2))/(sigma * math.sqrt(t))
                d2 = d1 - sigma * math.sqrt(t)
                result = (s * math.exp((b-r)*t) * N(d1)) - (x * math.exp(-r*t) * N(d2)) + (s * math.exp(-r*t) * sigma/(2*b)) * (-math.pow(s/x, -2 * b * math.sqrt(t)/sigma) * N(d1 - 2 * b * math.sqrt(t)/sigma) + (math.exp(b*t) * N(d1)))
            else:
                e1 = math.log(s/s_max) + (b + 0.5 * math.pow(sigma, 2))/(sigma * math.sqrt(t))
                e2 = e1 - sigma * math.sqrt(t)
                result = (math.exp(-r*t) * (s_max - x)) + (s * math.exp((b-r)*t) * N(e1)) - (s_max * math.exp(-r*t)*N(e2)) + (s * math.exp(-r*t) * math.pow(sigma, 2)/(2*b) * (-math.pow(s/s_max, -2*b/math.pow(sigma, 2)) * N(e1 - 2 * b * math.sqrt(t)/sigma) + (math.exp(b*t) * N(e1))))
        elif flag == 'put':
            if x < s_min:
                d1 = math.log(s/x) + (b + 0.5 * math.pow(sigma, 2))/(sigma * math.sqrt(t))
                d2 = d1 - sigma * math.sqrt(t)
                result = -(s * math.exp((b-r)*t) * N(-d1)) + (x * math.exp(-r*t) * N(-d2)) + (s * math.exp(-r*t) * sigma/(2*b)) * (-math.pow(s/x, -2 * b * math.sqrt(t)/sigma) * N(-d1 + 2 * b * math.sqrt(t)/sigma) - (math.exp(b*t) * N(-d1)))
            else:
                f1 = math.log(s/s_min) + (b + 0.5 * math.pow(sigma, 2))/(sigma * math.sqrt(t))
                f2 = f1 - sigma * math.sqrt(t)
                result = (math.exp(-r*t) * (x - s_min)) - (s * math.exp((b-r)*t) * N(-f1)) + (s_min * math.exp(-r*t)*N(-f2)) + (s * math.exp(-r*t) * math.pow(sigma, 2)/(2*b) * (math.pow(s/s_min, -2*b/math.pow(sigma, 2)) * N(-f1 + 2 * b * math.sqrt(t)/sigma) - (math.exp(b*t) * N(-f1))))
        return result
