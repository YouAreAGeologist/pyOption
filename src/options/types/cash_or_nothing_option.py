import math
from src.options.types.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class CashOrNothingOption(OptionBase):
    def __init__(self, flag, s, x, k, r, b, t, sigma):
        super(CashOrNothingOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.k = k
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        d = (math.log(self.s/self.x) + (self.b - math.pow(self.sigma, 2)/2) * self.t) / (self.sigma * math.sqrt(self.t))
        if self.flag == 'call':
            result = self.k * math.exp(-self.r * self.t) * N(d)
        elif self.flag == 'put':
            result = self.k * math.exp(-self.r * self.t) * N(d)
        return result

