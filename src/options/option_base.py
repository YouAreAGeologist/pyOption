from abc import ABCMeta, abstractmethod
import src.config as config
import logging

logger = logging.getLogger(config.settings['logger_name'])
hdlr = logging.FileHandler(config.settings['logger_path'])
formatter = logging.Formatter(config.settings['logger_format'])
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.WARNING)

class OptionBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, flag):
        self.logger.info('OptionBase.__init__')
        self.flag = flag

    @abstractmethod
    def get_value(self):
        self.logger.info('OptionBase.get_value')