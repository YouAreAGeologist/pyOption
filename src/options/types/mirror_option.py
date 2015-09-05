import math
from src.options.types.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class MirrorOption(OptionBase):
    def __init__(self, flag, position, s, x, r, b, t, sigma):
        super(MirrorOption, self).__init__()
        self.flag = flag
        self.position = position
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        f = None
        if self.position == 'long':
            f = self.s * math.exp(0.5 * math.pow(self.sigma, 2)) + math.fabs(self.b - math.pow(self.sigma, 2)/2) * self.t
        elif self.position == 'short':
            f = self.s * math.exp(0.5 * math.pow(self.sigma, 2)) - math.fabs(self.b - math.pow(self.sigma, 2)/2) * self.t

        d1 = (math.log(self.s/self.x) + (self.t * math.pow(self.sigma, 2)/2))/(self.sigma * math.sqrt(self.t))
        d2 = d1 - self.sigma * math.sqrt(self.t)

        if self.flag == 'call':
            result = math.exp(-self.r*self.t) * ((f * N(d1)) - (self.x * N(d2)))
        elif self.flag == 'put':
            result = math.exp(-self.r*self.t) * ((self.x * N(-d2)) - (f * N(-d1)))
        return result