import math
from mathematics.src.distribution import cnd

class Caplet:
    def __init__(self, notional, f, x, r, t, sigma, tau, basis):
        self.notional = notional
        self.f = f
        self.x = x
        self.r = r
        self.t = t
        self.sigma = sigma
        self.tau = tau
        self.basis = basis
        self.d1=(math.log(f / x) + (math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        self.d2 = self.d1 - (sigma * math.sqrt(t))

    def get_value(self):
        return (self.notional * (self.tau / self.basis) / (1 + (self.f * self.tau) / self.basis)) * math.exp(-self.r * self.t * ((self.f * cnd(self.d1)) -(self.x * self.d2)))
