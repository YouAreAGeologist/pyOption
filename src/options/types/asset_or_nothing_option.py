import math
from src.options.types.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class AssetOrNothingOption(OptionBase):
    def __init__(self, flag, s, x, r, b, t, sigma):
        super(AssetOrNothingOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result = None
        d = (math.log(self.s / self.x) + (self.s + math.pow(self.sigma, 2)/2) * self.t) / (self.sigma * math.sqrt(self.t))
        if self.flag == 'call':
            result = self.s * math.exp((self.b - self.r) * self.t) * N(d)
        elif self.flag == 'put':
            result = self.s * math.exp((self.b - self.r) * self.t) * N(-d)
        return result
