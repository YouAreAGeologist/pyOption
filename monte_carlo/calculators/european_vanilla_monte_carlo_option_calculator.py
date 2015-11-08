import math
from mathematics.src.random import rand


class EuropeanVanillaMonteCarloOptionCalculator:
    def __init__(self, flag, s, x, r, b, t, sigma, n):
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma
        self.n = n

    def get_values(self, greeks):
        results = dict()
        sum = 0
        z = 0
        if self.flag == 'c':
            z = 1
        elif self.flag == 'p':
            z = -1

        for i in self.n:
            st = self.s * math.exp((self.b - math.pow(self.sigma, 2) * self.t) + (self.sigma * math.sqrt(self.t)) * rand())
            sum += max(z * (st - self.x), 0)

        results['price'] = math.exp(-self.r * self.t) * sum / self.n

        if 'delta' in greeks:
            results['delta'] = math.exp(self.r * self.t) * sum / (self.s * self.n)
        if 'gamma' in greeks:
            results['gamma'] = math.exp(self.r * self.t) * math.pow(self.x / self.s, 2) * sum / (4 * self.n)
        if 'theta' in greeks:
            results['theta'] = 0
        if 'vega' in greeks:
            results['vega'] = (math.exp(self.r * self.t) * math.pow(self.x / self.s, 2) * sum / (4 * self.n)) * self.sigma * math.pow(self.s, 2) * self.t
        return results