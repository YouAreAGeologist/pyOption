import math
from copy import deepcopy


class NumericalGreeksCalculator:
    def __init__(self, option, ds=0.01, dr=0.01, db=0.01, dt=0.00001, dsigma=0.01):
        self.option = option
        self.ds = ds
        self.dr = dr
        self.db = db
        self.dt = dt
        self.dsigma = dsigma

    def get_values(self, greeks):
        calculated_greeks = dict()
        if ('delta' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.s = option1.s + self.ds
            option2.s = option2.s - self.ds
            calculated_greeks['delta'] = (option1.get_value() - option2.get_value()) / (
            2 * self.ds)

        if ('gamma' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option3 = deepcopy(self.option)
            option1.s = option1.s + self.ds
            option3.s = option2.s - self.ds
            calculated_greeks['gamma'] = (option1.get_value() - (
            2 * option2.get_value()) + option3.get_value()) / math.pow(self.ds, 2)

        if ('theta' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.t = option1.t + self.dt
            option2.t = option2.t - self.dt
            calculated_greeks['theta'] = (option1.get_value() - option2.get_value()) / self.dt

        if ('vega' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.sigma = option1.sigma + self.dsigma
            option2.sigma = option2.sigma - self.dsigma
            calculated_greeks['vega'] = (option1.get_value() - option2.get_value()) / 2

        if ('rho' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.r = option1.r + self.dr
            option2.r = option2.r - self.dr
            option1.b = option1.b + self.db
            option2.b = option2.b - self.db
            calculated_greeks['rho'] = (option1.get_value() - option2.get_value()) / 2

        if ('rho_futures' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.r = option1.r + self.dr
            option2.r = option2.r - self.dr
            calculated_greeks['rho_futures'] = (option1.get_value() - option2.get_value()) / 2

        if ('rho_2' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.b = option1.b - self.db
            option2.b = option2.b + self.db
            calculated_greeks['rho_2'] = (option1.get_value() - option2.get_value()) / 2

        if ('rho_carry' in greeks):
            option1 = deepcopy(self.option)
            option2 = deepcopy(self.option)
            option1.b = option1.b + self.db
            option2.b = option2.b - self.db
            calculated_greeks['rho_carry'] = (option1.get_value() - option2.get_value()) / 2

        return calculated_greeks
