import math
from src.options.types.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N
from src.mathematics.distributions.cumulative_bivariate_normal_distribution import M


class FadeInOption(OptionBase):
    def __init__(self, flag, s, x, l, u, n, h, r, b, t, sigma):
        super(FadeInOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.l = l
        self.u = u
        self.n = n
        self.h = h
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        d1 = (math.log(self.s/self.x) + (self.b + 0.5 * math.pow(self.sigma, 2))*self.t)/(self.sigma * math.sqrt(self.t))
        d2 = d1 - self.sigma * math.sqrt(self.t)
        sum = 0
        for i in range(1, self.n+1):
            t1 = i * self.t / self.n
            d3 = (math.log(self.s/self.l) + (self.b + 0.5 * math.pow(self.sigma, 2))*self.t)/(self.sigma * math.sqrt(t1))
            d4 = d3 - self.sigma * math.sqrt(t1)
            d5 = (math.log(self.s/self.u) + (self.b + 0.5 * math.pow(self.sigma, 2))*self.t)/(self.sigma * math.sqrt(t1))
            d6 = d5 - self.sigma * math.sqrt(t1)
            rho = math.sqrt(t1)/math.sqrt(self.t)

            if self.flag == 'call':
                sum += (math.pow(self.s, (self.b-self.r)*self.t) * (M(-d5, d1, -rho) - M(-d3, d1, -rho))) - (self.x * math.exp(-self.r*self.t) * ((M(-d6, d2, -rho) - M(-d4, d2, -rho))))
            elif self.flag == 'put':
                sum += -(math.pow(self.s, (self.b-self.r)*self.t) * (M(-d5, d1, rho) -M(-d3, -d1, rho))) + (self.x * math.exp(-self.r*self.t) * ((M(-d6, -d2, rho) - M(-d4, -d2, rho))))
        return sum / self.n