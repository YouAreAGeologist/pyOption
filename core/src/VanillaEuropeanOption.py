import math
from mathematics.src.Distribution import ndf, cnd


class VanillaEuropeanOption:
    def __init__(self, flag, s, x, r, b, t, sigma):
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma
        self.d1 = (math.log(s / x) + (r - b + math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        self.d2 = self.d1 - sigma * math.sqrt(t)


    def get_price(self, result=None):
        if self.flag == 'c':
            result = (self.s * math.exp(-self.b * self.t) * cnd(self.d1)) - (self.x * math.exp(-self.r * self.t) * cnd(self.d2))
        elif self.flag == 'p':
            result = (self.x * math.exp(-self.r * self.t) * cnd(-self.d2)) - (self.s * math.exp(-self.q * self.t) * cnd(-self.d1))
        return result


    def get_delta(self, result=None):
        if self.flag == 'c':
            result = math.exp((self.b - self.r) * self.t) * cnd(self.d1)
        elif self.flag == 'p':
            result = math.exp((self.b - self.r) * self.t) * (cnd(self.d1) - 1)
        return result
        

    def get_gamma(self):
        return ndf(self.d1) * math.exp((self.b - self.r) * self.t) / (self.s * self.sigma * math.sqrt(self.t))


    def get_vega(self):
        return self.s * math.exp((self.b - self.r) * self.t) * ndf(self.d1) * math.exp(self.t)
    
    
    def get_theta(self, result=None):
        if self.flag == 'c':
            result = - (((self.s * math.exp((self.b - self.r) * self.t) * ndf(self.d1) * self.sigma) / (2 * math.sqrt(self.t))) - (
            (self.b - self.r) * math.exp((self.b - self.r) * self.t) * cnd(self.d1)) - (self.r * self.x * math.exp(-self.r * self.t) * cnd(self.d2)))
        elif self.flag == 'p':
            result = - (((self.s * math.exp((self.b - self.r) * self.t) * ndf(self.d1) * self.sigma) / (2 * math.sqrt(self.t))) + (
            (self.b - self.r) * math.exp((self.b - self.r) * self.t) * cnd(-self.d1)) + (self.r * self.x * math.exp(-self.r * self.t) * cnd(-self.d2)))
        return result


    def get_rho(self, result=None):
        if self.flag == 'c':
            result = self.r * self.x * math.exp(-self.r * self.t) * cnd(self.d2)
        elif self.flag == 'p':
            result = self.r * self.x * math.exp(-self.r * self.t) * cnd(-self.d2)
        return result
