import math
from copy import deepcopy
import src.options.types.option


class NumericalGreeksCalculator:
    def __init__(self, params, greeks, ds = 0.01, dr = 0.01, db = 0.01, dt = 0.00001, dsigma= 0.01):
        self.__params = params
        self.__greeks = greeks
        self.__ds = ds
        self.__dr = dr
        self.__db = db
        self.__dt = dt

    def get_values(self):
        calculatedGreeks = {}

        if ('delta' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['s'] = p1['s'] + self.__ds
            p2['s'] = p2['s'] - self.__ds
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['delta'] = (option1.calculator.get_price() - option2.calculator.get_price()) / (2 * self.__ds)

        if ('gamma' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['s'] = p1['s'] + self.__ds
            p2['s'] = p2['s'] - self.__ds
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(self.__params, None)
            option3 = src.options.types.option.Option(p2, None)
            calculatedGreeks['gamma'] = (option1.calculator.get_price() - (2 * option2.calculator.get_price()) + option3.calculator.get_price()) / math.pow(self.__ds, 2)

        if ('theta' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['t'] = p1['t'] + self.__dt
            p2['t'] = p2['t'] - self.__dt
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['theta'] = (option1.calculator.get_price() - option2.calculator.get_price()) / self.__dt

        if ('vega' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['sigma'] = p1['sigma'] + self.__dsigma
            p2['sigma'] = p2['sigma'] - self.__dsigma
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['vega'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        if ('rho' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['r'] = p1['r'] + self.__dr
            p1['b'] = p1['b'] + self.__db
            p2['r'] = p2['r'] - self.__dr
            p2['b'] = p2['b'] - self.__db
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['rho'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        if ('rho_futures' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['r'] = p1['r'] + self.__dr
            p2['r'] = p2['r'] - self.__dr
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['rho_futures'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2


        if ('rho_2' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['b'] = p1['b'] - self.__db
            p2['b'] = p2['b'] + self.__db
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['rho_2'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2


        if ('rho_carry' in self.__greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['b'] = p1['b'] + self.__db
            p2['b'] = p2['b'] - self.__db
            option1 = src.options.types.option.Option(p1, None)
            option2 = src.options.types.option.Option(p2, None)
            calculatedGreeks['rho_carry'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        return calculatedGreeks