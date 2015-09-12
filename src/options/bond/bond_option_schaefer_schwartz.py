import math

from src.options.bond.bond_option_base import BondOptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class BondOptionSchaeferSchwartz(BondOptionBase):
    def __init__(self, flag, s, f, d, d_star, x, r, b, t, sigma_0, alpha):
        super(BondOptionSchaeferSchwartz, self).__init__()
        self.flag = flag
        self.s = s
        self.f = f
        self.d = d
        self.d_star = d_star
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma_0 = sigma_0

    def get_value(self):
        result = None
        k = self.sigma_0/(math.pow(self.s, self.alpha-1) * self.d_star)
        sigma = k * math.pow(self.s, self.alpha-1) * self.d
        d1 = (math.log(self.s / self.x) + (self.b + math.pow(sigma, 2)/2) * self.t) / (sigma * math.sqrt(self.t))
        d2 = d1 - sigma * math.sqrt(self.t)
        if self.flag == 'call':
            result = math.exp(-self.r * self.t) * ((self.f * N(d1)) - (self.x * N(d2)))
        elif self.flag == 'put':
            result = math.exp(-self.r * self.t) * ((self.x * N(-d2)) - (self.f * N(-d1)))
        return result
