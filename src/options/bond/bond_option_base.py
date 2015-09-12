from abc import ABCMeta, abstractmethod
from src.option_pricers.factories.option_pricer_factory import OptionPricerFactory

'''inherit from optionbase i.e. optionbase -> bondoptionbase'''


class BondOptionBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_value(self): pass