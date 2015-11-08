import math

from src.options.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class ExecutiveStockOption(OptionBase):
    def __init__(self, flag, s, x, r, b, t, lmd, sigma):
        super(ExecutiveStockOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.lmd = lmd
        self.sigma = sigma

    def get_value(self):
        result=None
        d1 = (math.log(self.s / self.x) + (self.r - self.b + math.pow(self.sigma, 2) / 2) * self.t) / (self.sigma * math.sqrt(self.t))
        d2 = d1 - self.sigma * math.sqrt(self.t)
        if self.flag == 'call':
            result = math.exp(-self.lmd * self.t) * ((self.s * math.exp((self.b - self.r) * self.t) * N(d1)) - (self.x * math.exp(-self.r * self.t) * N(d2)))
        elif self.flag == 'put':
            result = math.exp(-self.lmd * self.t) * ((self.x * math.exp(-self.r * self.t) * N(-d2)) - (self.s * math.exp((self.b - self.r) * self.t) * N(-d1)))
        return result