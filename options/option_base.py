from abc import ABCMeta, abstractmethod
import src.config as config
import logging

class OptionBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_value(self):
        pass