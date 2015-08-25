import math
from copy import deepcopy
import src.options.types.option


class NumericalGreeksCalculator:
    def __init__(self, params, ds = 0.01, dr = 0.01, db = 0.01, dt = 0.00001, dsigma= 0.01):
        self.__params = params
        self.__ds = ds
        self.__dr = dr
        self.__db = db
        self.__dt = dt
        self.__dsigma = dsigma

    def get_values(self):
        calculated_greeks = {}
        required_greeks = self.__params['greeks']

        if ('delta' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['s'] = p1['option']['s'] + self.__ds
            p2['option']['s'] = p2['option']['s'] - self.__ds
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['delta'] = (option1.calculator.get_price() - option2.calculator.get_price()) / (2 * self.__ds)

        if ('gamma' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['s'] = p1['option']['s'] + self.__ds
            p2['option']['s'] = p2['option']['s'] - self.__ds
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(self.__params)
            option3 = src.options.types.option.Option(p2)
            calculated_greeks['gamma'] = (option1.calculator.get_price() - (2 * option2.calculator.get_price()) + option3.calculator.get_price()) / math.pow(self.__ds, 2)

        if ('theta' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['t'] = p1['option']['t'] + self.__dt
            p2['option']['t'] = p2['option']['t'] - self.__dt
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['theta'] = (option1.calculator.get_price() - option2.calculator.get_price()) / self.__dt

        if ('vega' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['sigma'] = p1['option']['sigma'] + self.__dsigma
            p2['option']['sigma'] = p2['option']['sigma'] - self.__dsigma
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['vega'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        if ('rho' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['r'] = p1['option']['r'] + self.__dr
            p1['option']['b'] = p1['option']['b'] + self.__db
            p2['option']['r'] = p2['option']['r'] - self.__dr
            p2['option']['b'] = p2['option']['b'] - self.__db
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['rho'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        if ('rho_futures' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['r'] = p1['option']['r'] + self.__dr
            p2['option']['r'] = p2['option']['r'] - self.__dr
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['rho_futures'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2


        if ('rho_2' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['b'] = p1['option']['b'] - self.__db
            p2['option']['b'] = p2['option']['b'] + self.__db
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['rho_2'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2


        if ('rho_carry' in required_greeks):
            p1 = deepcopy(self.__params)
            p2 = deepcopy(self.__params)
            p1['option']['b'] = p1['option']['b'] + self.__db
            p2['option']['b'] = p2['option']['b'] - self.__db
            option1 = src.options.types.option.Option(p1)
            option2 = src.options.types.option.Option(p2)
            calculated_greeks['rho_carry'] = (option1.calculator.get_price() - option2.calculator.get_price()) / 2

        return calculated_greeks