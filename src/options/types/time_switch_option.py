import math
from src.options.types.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N


class TimeSwitchOption(OptionBase):
    def __init__(self, flag, s, x, a, r, b, i, t, dt, sigma):
        super(TimeSwitchOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.a = a
        self.r = r
        self.b = b
        self.i = i
        self.t = t
        self.dt = dt
        self.sigma = sigma

    def get_value(self):
        result=None
        n = self.t/self.dt
        sum = 0
        if self.flag == 'call':
            for i in range(self.i, n+1):
                result += N((math.log(self.s/self.x) + (self.b - 0.5 * math.pow(self.sigma, 2) * i * self.dt))/(self.sigma * math.sqrt(i * self.dt))) * self.dt
        elif self.flag == 'put':
            for i in range(self.i, n+1):
                result += N((-math.log(self.s/self.x) - (self.b - 0.5 * math.pow(self.sigma, 2) * i * self.dt))/(self.sigma * math.sqrt(i * self.dt))) * self.dt
        return a * math.exp(-r * t) * sum
