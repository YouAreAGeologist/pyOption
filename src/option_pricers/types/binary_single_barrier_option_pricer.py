import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class BinarySingleBarrierOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        x = option['x']
        k = option['k']
        h = option['h']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        mu = (b - math.pow(sigma, 2)/2)/math.pow(sigma, 2)
        lmd = math.sqrt(math.pow(mu, 2) + (2*r/math.pow(sigma, 2)))
        z = (math.log(h/s)/(sigma * math.sqrt(t))) + (lmd * sigma * math.sqrt(t))
        x1 = (math.log(s/x)/(sigma * math.sqrt(t))) + ((mu + 1) * sigma * math.sqrt(t))
        x2 = (math.log(s/h)/(sigma * math.sqrt(t))) + ((mu + 1) * sigma * math.sqrt(t))
        y1 = (math.log(math.pow(h, 2)/(s * x))/(sigma * math.sqrt(t))) + ((mu + 1) * sigma * math.sqrt(t))
        y2 = (math.log(h/s)/(sigma * math.sqrt(t))) + ((mu + 1) * sigma * math.sqrt(t))

        a1 = lambda phi: s * math.exp((b - r) * t) * N(phi * x1)
        b1 = lambda phi: k * math.exp(r * t) * N((phi * x1) - (phi * sigma * math.sqrt(t)))
        a2 = lambda phi: s * math.exp((b - r) * t) * N(phi * x2)
        b2 = lambda phi: k * math.exp(-r * t) * N((phi * x2) - (phi * sigma * math.sqrt(t)))
        a3 = lambda eta: s * math.exp((b - r) * t) * math.pow(h/s, 2 * (mu + 1)) * N(eta * y1)
        b3 = lambda eta: k * math.exp(-r * t) * math.pow(h/s, 2 * mu) * N((eta * y1) - (eta * sigma * math.sqrt(t)))
        a4 = lambda eta: s * math.exp((b - r) * t) * math.pow(h/s, 2 * (mu + 1)) * N(eta * y2)
        b4 = lambda eta: k * math.exp(-r * t) * math.pow(h/s, 2 * mu) * N((eta * y2) - (eta * sigma * math.sqrt(t)))
        a5 = lambda eta: k * (math.pow(h/s, mu + lmd) * N(eta * z) + math.pow(h/s, mu - lmd) * N((eta * z) - (2 * eta * lmd * sigma * math.sqrt(t))))

        if flag == 'down-and-in cash-at-hit-or-nothing':
            result = a5(1)
        elif flag == 'up-and-in cash-at-hit-or-nothing':
            result = a5(-1)
        elif flag == 'down-and-in asset-at-hit-or-nothing':
            result = a5(1)
        elif flag == 'up-and-in asset-at-hit-or-nothing':
            result = a5(-1)
        elif flag == 'down-and-in cash-at-expiration-or-nothing':
            result = b2(-1) + b4(1)
        elif flag == 'up-and-in cash-at-expiration-or-nothing':
            result = b2(1) + b4(-1)
        elif flag == 'down-and-in asset-at-expiration-or-nothing':
            result = a2(-1) + a4(1)
        elif flag == 'up-and-in asset-at-expiration-or-nothing':
            result = a2(1) + a4(-1)
        elif flag == 'down-and-out cash-or-nothing':
            result = b2(1) - b4(1)
        elif flag == 'up-and-out cash-or-nothing':
            result = b2(-1) - b4(-1)
        elif flag == 'down-and-out asset-or-nothing':
            result = a2(1) - a4(1)
        elif flag == 'up-and-out asset-or-nothing':
            result = a2(-1) - a4(-1)
        elif flag == 'down-and-in cash-or-nothing call':
            if x > h:
                result = b3(1)
            elif x < h:
                result = b1(1) - b2(-1) + b4(-1)
        elif flag == 'up-and-in cash-or-nothing call':
            if x > h:
                result = b1(1)
            elif x < h:
                result = b2(1) - b3(-1) + b4(-1)
        elif flag == 'down-and-in asset-or-nothing call':
            if x > h:
                result = a3(1)
            elif x < h:
                result = a1(1) - a2(1) + a4(1)
        elif flag == 'up-and-in asset-or-nothing call':
            if x > h:
                result = a1(1)
            elif x < h:
                result = a2(1) - a3(-1) + a4(-1)
        elif flag == 'down-and-in cash-or-nothing put':
            if x > h:
                result = b2(-1) - b3(1) + b4(1)
            elif x < h:
                result = b1(-1)
        elif flag == 'up-and-in cash-or-nothing put':
            if x > h:
                result = b1(-1) - b2(-1) + b4(-1)
            elif x < h:
                result = b3(-1)
        elif flag == 'down-and-in asset-or-nothing put':
            if x > h:
                result = a2(-1) - a3(1) + a4(1)
            elif x < h:
                result = a1(-1)
        elif flag == 'up-and-in asset-or-nothing put':
            if x > h:
                result = a1(-1) + a2(-1) + a3(-1)
            elif x < h:
                result = a3(-1)
        elif flag == 'down-and-out cash-or-nothing call':
            if x > h:
                result = b1(1) - b3(1)
            elif x < h:
                result = b2(1) - b4(1)
        elif flag == 'up-and-out cash-or-nothing call':
            if x > h:
                result = 0
            elif x < h:
                result = b1(1) - b2(1) + b3(-1) - b4(-1)
        elif flag == 'down-and-out asset-or-nothing call':
            if x > h:
                result = a1(1) - a3(1)
            elif x < h:
                result = a2(1) - a4(1)
        elif flag == 'up-and-out asset-or-nothing call':
            if x > h:
                result = 0
            elif x < h:
                result = a1(1) - a2(1) + a3(-1) - a4(-1)
        elif flag == 'down-and-out cash-or-nothing put':
            if x > h:
                result = b1(-1) - b2(-1) + b3(1) - b4(1)
            elif x < h:
                result = 0
        elif flag == 'up-and-out cash-or-nothing put':
            if x > h:
                result = b2(-1) - b4(-1)
            elif x < h:
                result = b1(-1) - b3(-1)
        elif flag == 'down-and-out asset-or-nothing put':
            if x > h:
                result = a1(-1) - a2(-1) + a3(1) - a4(1)
            elif x < h:
                result = 0
        elif flag == 'up-and-out asset-or-nothing put':
            if x > h:
                result = a2(-1) - a4(-1)
            elif x < h:
                result = a1(-1) - a3(-1)
        return result