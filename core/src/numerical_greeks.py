import math


class NumericalGreeks:
    def __init__(self, optionType, greeks, ds=0.01, dr=0.01, db=0.01, dsigma=0.01, dt=0.00001):
        self.__optionType = optionType
        self.__greeks = greeks


    def get_values(self):
        results = dict()

        if 'delta' in self.__greeks:
            pass
        if 'gamma' in self.__greeks:
            pass
        if 'theta' in self.__greeks:
            pass
        if 'vega' in self.__greeks:
            pass
        if 'rho' in self.__greeks:
            pass

        return results
