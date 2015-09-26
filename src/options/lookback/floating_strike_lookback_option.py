import math
import logging
from src.options.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N

logger = logging.getLogger(config.settings['logger_name'])


class FlostingStrikeLookbackOption(OptionBase):
    def __init__(self, flag, s, s_min, s_max, x, r, b, t, sigma):
        super(FlostingStrikeLookbackOption, self).__init__(flag)
        logger.info('FloatingStrikeLookbackOption.ctor')
        self.t = t

    def get_value(self):
        logger.info('FloatingStrikeLookbackOption.get_value')
        result = None
        try:
            if self.flag == 'call':
                a1 = (math.log(self.s / self.s_min) + (self.b + 0.5 * math.pow(self.sigma, 2)) * self.t) / (
                    self.sigma * math.sqrt(self.t))
                a2 = a1 - self.sigma * math.sqrt(self.t)
                result = self.s * math.exp((self.b - self.r) * self.t) * N(a1) - (
                    self.s_min * math.exp(-self.r * self.t) * N(a2)) + (
                             (self.s * math.exp(-self.r * self.t) * 0.5 * math.pow(self.sigma, 2) / self.b) * (
                                 math.pow(self.s / self.s_min, -2 * self.b / math.pow(self.sigma, 2)) * N(
                                     -a1 + (2 * self.b * math.sqrt(self.t) / self.sigma) - (
                                         math.exp(self.b * self.t) * N(-a1)))))
            elif self.flag == 'put':
                b1 = (math.log(self.s / self.s_min) + (self.b + 0.5 * math.pow(self.sigma, 2)) * self.t) / (
                    self.sigma * math.sqrt(self.t))
                b2 = b1 - self.sigma * math.sqrt(self.t)
                result = self.s_max * math.exp(-self.r * self.t) * N(-b2) - (
                    self.s * math.exp((self.b - self.r) * self.t) * N(-b1)) + (
                             self.s * math.exp(-self.r * self.t) * math.pow(self.sigma, 2) / (2 * self.b)) + (
                             (self.s * math.exp(-self.r * self.t) * math.pow(self.sigma, 2) / (2 * self.b)) * (-(
                                 math.pow(self.s / self.s_max, -2 * self.b / math.pow(self.sigma, 2)) * N(
                                     b1 - 2 * self.b * math.sqrt(self.t) / self.sigma)) + (math.exp(
                                 self.b * self.t) * N(b1))))
        except Exception, e:
            logger.error(e)
        return result
