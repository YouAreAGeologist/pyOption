import math

from options.bases.src.option_base import OptionBase
from mathematics.distributions.cumulative_normal_distribution import N
from mathematics.distributions.cumulative_bivariate_normal_distribution import M


class PartialTimeFloatingStrikeLookbackOption(OptionBase):
    def __init__(self, flag, s, s_min, s_max, x, r, b, t1, t2, lmd, sigma):
        super(PartialTimeFloatingStrikeLookbackOption, self).__init__()
        self.flag = flag
        self.s = s
        self.s_min = s_min
        self.s_max = s_max
        self.x = x
        self.r = r
        self.b = b
        self.t1 = t1
        self.t2 = t2
        self.lmd = lmd
        self.sigma = sigma

    def get_value(self):
        m0 = None
        if self.flag == 'call':
            m0 = self.s_min
        elif self.flag == 'put':
            m0 = self.s_max
        d1 = (math.log(self.s / m0) + (self.b + 0.5 * math.pow(self.sigma, 2) * self.t2)) / (
            self.sigma * math.sqrt(self.t2))
        d2 = d1 - self.sigma * math.sqrt(self.t2)
        e1 = ((self.b + 0.5 * math.pow(self.sigma, 2) / 2) * (self.t2 - self.t1)) / (
            self.sigma * math.sqrt(self.t2 - self.t1))
        e2 = e1 - self.sigma * math.sqrt(self.t2 - self.t1)
        f1 = (math.log(self.s / m0) + (self.b + 0.5 * math.pow(self.sigma, 2)) * self.t1) / (
            self.sigma * math.sqrt(self.t1))
        f2 = f1 - self.sigma * math.sqrt(self.t1)
        g1 = math.log(self.lmd) / (self.sigma * math.sqrt(self.t2))
        g2 = math.log(self.lmd) / (self.sigma * math.sqrt(self.t2 - self.t1))

        if self.flag == 'call':
            a1 = self.lmd * self.s_min * math.exp(-self.r * self.t2) * N(d2 - g1)
            a2 = self.s * math.exp((self.b - self.r) * self.t2) * N(d1 - g1)
            a3 = self.lmd * self.s * math.exp(-self.r * self.t2) * math.sqrt(self.sigma, 2) / (2 * self.b)
            b1 = math.pow(self.s / self.s_min, -2 * self.b / math.pow(self.sigma, 2)) * M(
                -f1 + (2 * self.b * math.sqrt(self.t1) / self.sigma),
                -d1 + (2 * self.b * math.sqrt(self.t2) / self.sigma) - g1, math.sqrt(self.t1 / self.t2))
            b2 = math.exp(self.b * self.t2) * math.pow(self.lmd, 2 * self.b / math.pow(self.sigma, 2)) * M(-d1 - g1,
                                                                                                           e1 + g2,
                                                                                                           -math.sqrt(
                                                                                                               1 - (
                                                                                                                   self.t1 / self.t2)))
            c1 = self.s * math.exp((self.b - self.r) * self.t2) * M(-d1 + g1, e1 - g2,
                                                                    -math.sqrt(1 - (self.t1 / self.t2)))
            c2 = self.lmd * self.s_min * math.exp(-self.r * self.t2) * M(-f2, d2 - g1,
                                                                         -math.sqrt(self.t1 / self.t2))
            c3 = math.exp(-self.b * (self.t2 - self.t1)) * (
                1 + math.pow(self.sigma, 2) / (2 * self.b)) * self.lmd * self.s * math.exp(
                (self.b - self.r) * self.t2) * N(e2 - g2) * N(-f1)
            result = -a1 + a2 + (a3 * (b1 - b2)) + c1 + c2 - c3
        elif self.flag == 'put':
            a1 = self.lmd * self.s_max * math.exp(-self.r * self.t2) * N(-d2 + g1)
            a2 = self.s * math.exp((self.b - self.r) * self.t2) * N(-d1 + g1)
            a3 = self.lmd * self.s * math.exp(-self.r * self.t2) * math.sqrt(self.sigma, 2) / (2 * self.b)
            b1 = -math.pow(self.s / self.s_max, -2 * self.b / math.pow(self.sigma, 2)) * M(
                f1 - (2 * self.b * math.sqrt(self.t1) / self.sigma),
                d1 - (2 * self.b * math.sqrt(self.t2) / self.sigma) + g1, math.sqrt(self.t1 / self.t2))
            b2 = math.exp(self.b * self.t2) * math.pow(self.lmd, 2 * self.b / math.pow(self.sigma, 2)) * M(d1 + g1,
                                                                                                           -e1 - g2,
                                                                                                           -math.sqrt(
                                                                                                               1 - (
                                                                                                                   self.t1 / self.t2)))
            c1 = self.s * math.exp((self.b - self.r) * self.t2) * M(d1 - g1, -e1 + g2,
                                                                    -math.sqrt(1 - (self.t1 / self.t2)))
            c2 = self.lmd * self.s_max * math.exp(-self.r * self.t2) * M(-f2, -d2 + g1,
                                                                         -math.sqrt(self.t1 / self.t2))
            c3 = math.exp(-self.b * (self.t2 - self.t1)) * (
                1 + math.pow(self.sigma, 2) / (2 * self.b)) * self.lmd * self.s * math.exp(
                (self.b - self.r) * self.t2) * N(-e2 + g2) * N(f1)
            result = a1 - a2 + (a3 * (b1 + b2)) - c1 - c2 + c3
        return result
