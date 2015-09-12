import math

from src.options.bond.bond_option_base import BondOptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class EuropeanShortTermBondOption(BondOptionBase):
    def __init__(self, flag, s, f, x, r, b, t, sigma):
        super(EuropeanShortTermBondOption, self).__init__()
        self.flag = flag
        self.s = s
        self.f = f
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result = None
        d1 = (math.log(self.f / self.x) + (math.pow(self.sigma, 2)/2) * self.t) / (self.sigma * math.sqrt(self.t))
        d2 = d1 - self.sigma * math.sqrt(self.t)
        if self.flag == 'call':
            result = math.exp(-self.r * self.t) * ((self.f * N(d1)) - (self.x * N(d2)))
        elif self.flag == 'put':
            result = math.exp(-self.r * self.t) * ((self.x * N(-d2)) - (self.f * N(-d1)))
        return result
