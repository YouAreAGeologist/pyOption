import math
from mathematics.src.distribution import cnd


class Swaption:
    def __init__(self, flag, f, x, r, t, t1, sigma, m):
        self.flag = flag
        self.f = f
        self.x = x
        self.r = r
        self.t = t
        self.t1 = t1
        self.sigma = sigma
        self.m = m
        self.d1 = (math.log(f / x) + ((math.pow(sigma, 2)/2) * t)) / (sigma * math.sqrt(t))
        self.d2 = self.d1 - (sigma * math.sqrt(t))

    def get_value(self):
        result=None
        if self.flag == 'c':
            result = ((1 - (1 / (math.pow(1 + (self.f / self.m), self.t1 * self.m)))) / self.f) * math.exp(-self.r * self.t) * ((self.f * cnd(self.d1)) - (self.x * cnd(self.d2)))
        elif self.flag == 'p':
            result = ((1 - (1 / (math.pow(1 + (self.f / self.m), self.t1 * self.m)))) / self.f) * math.exp(-self.r * self.t) * ((self.x * cnd(-self.d2)) - (self.f * cnd(-self.d1)))
        return result