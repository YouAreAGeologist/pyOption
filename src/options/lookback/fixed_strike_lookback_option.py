import math
import logger
import src.config as config
from src.options.option_base import OptionBase
from src.mathematics.distributions.cumulative_normal_distribution import N

logger = logging.getLogger(config.settings['logger_name'])


class FixedStrikeLookbackOption(OptionBase):
    def __init__(self, flag, s, s_min, s_max, x, r, b, t, sigma):
        super(FixedStrikeLookbackOption, self).__init__(flag, s, s_min, s_max, x, r, b, sigma)
        logger.info('FixedStrikeLookbackOption.ctor')

    def get_value(self):
        logger.info('FixedStrikeLookbackOption.get_value')
        result = None
        try:
            if self.flag == 'call':
                if self.x > self.s_max:
                    d1 = math.log(self.s / self.x) + (self.b + 0.5 * math.pow(self.sigma, 2)) / (
                        self.sigma * math.sqrt(self.t))
                    d2 = d1 - self.sigma * math.sqrt(self.t)
                    result = (self.s * math.exp((self.b - self.r) * self.t) * N(d1)) - (
                        self.x * math.exp(-self.r * self.t) * N(d2)) + (self.s * math.exp(
                        -self.r * self.t) * self.sigma / (
                                                                            2 * self.b)) * (-math.pow(self.s / self.x,
                                                                                                      -2 * self.b * math.sqrt(
                                                                                                          self.t) / self.sigma) * N(
                        d1 - 2 * self.b * math.sqrt(self.t) / self.sigma) + (math.exp(self.b * self.t) * N(d1)))
                else:
                    e1 = math.log(self.s / self.s_max) + (self.b + 0.5 * math.pow(self.sigma, 2)) / (
                        self.sigma * math.sqrt(self.t))
                    e2 = e1 - self.sigma * math.sqrt(self.t)
                    result = (math.exp(-self.r * self.t) * (self.s_max - self.x)) + (
                        self.s * math.exp((self.b - self.r) * self.t) * N(e1)) - (
                                 self.s_max * math.exp(-self.r * self.t) * N(e2)) + (
                                 self.s * math.exp(-self.r * self.t) * math.pow(self.sigma, 2) / (2 * self.b) * (
                                     -math.pow(self.s / self.s_max, -2 * self.b / math.pow(self.sigma, 2)) * N(
                                         e1 - 2 * self.b * math.sqrt(self.t) / self.sigma) + (
                                     math.exp(self.b * self.t) * N(e1))))
            elif self.flag == 'put':
                if self.x < self.s_min:
                    d1 = math.log(self.s / self.x) + (self.b + 0.5 * math.pow(self.sigma, 2)) / (
                        self.sigma * math.sqrt(self.t))
                    d2 = d1 - self.sigma * math.sqrt(self.t)
                    result = -(self.s * math.exp((self.b - self.r) * self.t) * N(-d1)) + (
                        self.x * math.exp(-self.r * self.t) * N(-d2)) + (self.s * math.exp(
                        -self.r * self.t) * self.sigma / (
                                                                             2 * self.b)) * (-math.pow(self.s / self.x,
                                                                                                       -2 * self.b * math.sqrt(
                                                                                                           self.t) / self.sigma) * N(
                        -d1 + 2 * self.b * math.sqrt(self.t) / self.sigma) - (math.exp(self.b * self.t) * N(-d1)))
                else:
                    f1 = math.log(self.s / self.s_min) + (self.b + 0.5 * math.pow(self.sigma, 2)) / (
                        self.sigma * math.sqrt(self.t))
                    f2 = f1 - self.sigma * math.sqrt(self.t)
                    result = (math.exp(-self.r * self.t) * (self.x - self.s_min)) - (
                        self.s * math.exp((self.b - self.r) * self.t) * N(-f1)) + (
                                 self.s_min * math.exp(-self.r * self.t) * N(-f2)) + (
                                 self.s * math.exp(-self.r * self.t) * math.pow(self.sigma, 2) / (2 * self.b) * (
                                     math.pow(self.s / self.s_min, -2 * self.b / math.pow(self.sigma, 2)) * N(
                                         -f1 + 2 * self.b * math.sqrt(self.t) / self.sigma) - (
                                     math.exp(self.b * self.t) * N(-f1))))
        except Exception, e:
            logger.error(e)
        return result
