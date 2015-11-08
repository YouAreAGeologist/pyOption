from abc import ABCMeta, abstractmethod

class OptionBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_value(self):
        pass