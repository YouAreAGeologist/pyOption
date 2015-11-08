import math
from options.bases.src.option_base import OptionBase
from mathematics.distributions.src.cumulative_normal_distribution import N


class BinarySingleBarrierOption(OptionBase):
    def __init__(self, flag, s, x, k, h, r, b, t, sigma):
        super(BinarySingleBarrierOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.k = k
        self.h = h
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        mu = (self.b - math.pow(self.sigma, 2)/2)/math.pow(self.sigma, 2)
        lmd = math.sqrt(math.pow(mu, 2) + (2*self.r/math.pow(self.sigma, 2)))
        z = (math.log(self.h/self.s)/(self.sigma * math.sqrt(self.t))) + (lmd * self.sigma * math.sqrt(self.t))
        x1 = (math.log(self.s/self.x)/(self.sigma * math.sqrt(self.t))) + ((mu + 1) * self.sigma * math.sqrt(self.t))
        x2 = (math.log(self.s/self.h)/(self.sigma * math.sqrt(self.t))) + ((mu + 1) * self.sigma * math.sqrt(self.t))
        y1 = (math.log(math.pow(self.h, 2)/(self.s * self.x))/(self.sigma * math.sqrt(self.t))) + ((mu + 1) * self.sigma * math.sqrt(self.t))
        y2 = (math.log(self.h/self.s)/(self.sigma * math.sqrt(self.t))) + ((mu + 1) * self.sigma * math.sqrt(self.t))
        a1 = lambda phi: self.s * math.exp((self.b - self.r) * self.t) * N(phi * x1)
        b1 = lambda phi: self.k * math.exp(self.r * self.t) * N((phi * x1) - (phi * self.sigma * math.sqrt(self.t)))
        a2 = lambda phi: self.s * math.exp((self.b - self.r) * self.t) * N(phi * x2)
        b2 = lambda phi: self.k * math.exp(-self.r * self.t) * N((phi * x2) - (phi * self.sigma * math.sqrt(self.t)))
        a3 = lambda eta: self.s * math.exp((self.b - self.r) * self.t) * math.pow(self.h/self.s, 2 * (mu + 1)) * N(eta * y1)
        b3 = lambda eta: self.k * math.exp(-self.r * self.t) * math.pow(self.h/self.s, 2 * mu) * N((eta * y1) - (eta * self.sigma * math.sqrt(self.t)))
        a4 = lambda eta: self.s * math.exp((self.b - self.r) * self.t) * math.pow(self.h/self.s, 2 * (mu + 1)) * N(eta * y2)
        b4 = lambda eta: self.k * math.exp(-self.r * self.t) * math.pow(self.h/self.s, 2 * mu) * N((eta * y2) - (eta * self.sigma * math.sqrt(self.t)))
        a5 = lambda eta: self.k * (math.pow(self.h/self.s, mu + lmd) * N(eta * z) + math.pow(self.h/self.s, mu - lmd) * N((eta * z) - (2 * eta * lmd * self.sigma * math.sqrt(self.t))))

        if self.flag == 'down_and_in_cash_at_hit_or_nothing':
            result = a5(1)
        elif self.flag == 'up_and_in_cash_at_hit_or_nothing':
            result = a5(-1)
        elif self.flag == 'down_and_in_asset_at_hit_or_nothing':
            result = a5(1)
        elif self.flag == 'up_and_in_asset_at_hit_or_nothing':
            result = a5(-1)
        elif self.flag == 'down-and-in cash-at-expiration-or-nothing':
            result = b2(-1) + b4(1)
        elif self.flag == 'up-and-in cash-at-expiration-or-nothing':
            result = b2(1) + b4(-1)
        elif self.flag == 'down-and-in asset-at-expiration-or-nothing':
            result = a2(-1) + a4(1)
        elif self.flag == 'up-and-in asset-at-expiration-or-nothing':
            result = a2(1) + a4(-1)
        elif self.flag == 'down-and-out cash-or-nothing':
            result = b2(1) - b4(1)
        elif self.flag == 'up-and-out cash-or-nothing':
            result = b2(-1) - b4(-1)
        elif self.flag == 'down-and-out asset-or-nothing':
            result = a2(1) - a4(1)
        elif self.flag == 'up-and-out asset-or-nothing':
            result = a2(-1) - a4(-1)
        elif self.flag == 'down-and-in cash-or-nothing call':
            if self.x > self.h:
                result = b3(1)
            elif self.x < self.h:
                result = b1(1) - b2(-1) + b4(-1)
        elif self.flag == 'up-and-in cash-or-nothing call':
            if self.x > self.h:
                result = b1(1)
            elif self.x < self.h:
                result = b2(1) - b3(-1) + b4(-1)
        elif self.flag == 'down-and-in asset-or-nothing call':
            if self.x > self.h:
                result = a3(1)
            elif self.x < self.h:
                result = a1(1) - a2(1) + a4(1)
        elif self.flag == 'up-and-in asset-or-nothing call':
            if self.x > self.h:
                result = a1(1)
            elif self.x < self.h:
                result = a2(1) - a3(-1) + a4(-1)
        elif self.flag == 'down-and-in cash-or-nothing put':
            if self.x > self.h:
                result = b2(-1) - b3(1) + b4(1)
            elif self.x < self.h:
                result = b1(-1)
        elif self.flag == 'up-and-in cash-or-nothing put':
            if self.x > self.h:
                result = b1(-1) - b2(-1) + b4(-1)
            elif self.x < self.h:
                result = b3(-1)
        elif self.flag == 'down-and-in asset-or-nothing put':
            if self.x > self.h:
                result = a2(-1) - a3(1) + a4(1)
            elif self.x < self.h:
                result = a1(-1)
        elif self.flag == 'up-and-in asset-or-nothing put':
            if self.x > self.h:
                result = a1(-1) + a2(-1) + a3(-1)
            elif self.x < self.h:
                result = a3(-1)
        elif self.flag == 'down-and-out cash-or-nothing call':
            if self.x > self.h:
                result = b1(1) - b3(1)
            elif self.x < self.h:
                result = b2(1) - b4(1)
        elif self.flag == 'up-and-out cash-or-nothing call':
            if self.x > self.h:
                result = 0
            elif self.x < self.h:
                result = b1(1) - b2(1) + b3(-1) - b4(-1)
        elif self.flag == 'down-and-out asset-or-nothing call':
            if self.x > self.h:
                result = a1(1) - a3(1)
            elif self.x < self.h:
                result = a2(1) - a4(1)
        elif self.flag == 'up-and-out asset-or-nothing call':
            if self.x > self.h:
                result = 0
            elif self.x < self.h:
                result = a1(1) - a2(1) + a3(-1) - a4(-1)
        elif self.flag == 'down-and-out cash-or-nothing put':
            if self.x > self.h:
                result = b1(-1) - b2(-1) + b3(1) - b4(1)
            elif self.x < self.h:
                result = 0
        elif self.flag == 'up-and-out cash-or-nothing put':
            if self.x > self.h:
                result = b2(-1) - b4(-1)
            elif self.x < self.h:
                result = b1(-1) - b3(-1)
        elif self.flag == 'down-and-out asset-or-nothing put':
            if self.x > self.h:
                result = a1(-1) - a2(-1) + a3(1) - a4(1)
            elif self.x < self.h:
                result = 0
        elif self.flag == 'up-and-out asset-or-nothing put':
            if self.x > self.h:
                result = a2(-1) - a4(-1)
            elif self.x < self.h:
                result = a1(-1) - a3(-1)
        return result
