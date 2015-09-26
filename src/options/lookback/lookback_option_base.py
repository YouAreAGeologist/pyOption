from abc import ABCMeta, abstractmethod
from src.options.option_base import OptionBase
import logging
import src.config as config

logger = logging.getLogger('pyoption')


class LookbackOptionBase(OptionBase):
    __metaclass__ = ABCMeta

    def __init__(self, s, s_min, s_max, x, r, b, sigma):
        super(FixedStrikeLookbackOption, self).__init__(flag)
        self.logger = logging.getLogger(config.settings['logger_name'])
        self.logger.info('LookbackOptionBase.__init__')
        self.s = s
        self.s_min = s_min
        self.s_max = s_max
        self.x = x
        self.r = r
        self.b = b
        self.sigma = sigma

    @abstractmethod
    def get_value(self):
        self.logger.info('LookbackOptionBase.get_value')
