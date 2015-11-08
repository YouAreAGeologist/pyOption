import math

from src.options.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class StandardPowerOption(OptionBase):
    def __init__(self, flag, s, x, i, r, b, t, sigma):
        super(StandardPowerOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.i = i
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        d1 = (math.log(self.s/math.pow(self.x,-self.i)) + (self.b + (self.i - 0.5) * math.pow(self.sigma, 2)) * self.t) / (self.sigma * math.sqrt(self.t))
        d2 = d1 - self.i * self.sigma * math.sqrt(self.t)
        if self.flag == 'call':
            result = (math.pow(self.s, self.i) * math.exp(((self.i - 1) * (self.r + self.i * math.pow(self.sigma,2)/2) - self.i * (self.r - self.b) * self.t)) * N(d1)) - (self.x * math.exp(-self.r * self.t) * N(d2))
        elif self.flag == 'put':
            result =  (self.x * math.exp(-self.r * self.t) * N(-d2)) - (math.pow(self.s, self.i) * math.exp(((self.i - 1) * (self.r + self.i * math.pow(self.sigma,2)/2) - self.i * (self.r - self.b) * self.t)) * N(-d1))
        return result
