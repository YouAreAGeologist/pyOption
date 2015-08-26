import abc



class OptionBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abtractmethod
    def get_values(self):
        raise NotImplementedError("Please Implement this method")

    @abc.abtractmethod
    def get_analytic_price(self):
        raise NotImplementedError("Please Implement this method")


