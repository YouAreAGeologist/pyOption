import math
from core.src.vanilla_european_option import VanillaEuropeanOption


class VanillaEuropeanOptionNumbericalGreeks:
    def __init__(self, flag, s, x, r, b, t, sigma, greeks, ds = 0.01, dr = 0.01, db = 0.01, dt = 0.00001, dsigma= 0.01):
        self.__flag = flag
        self.__s = s
        self.__x = s
        self.__r = r
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__ds = ds
        self.__dr = dr
        self.__db = db
        self.__dt = dt
        self.__dsigma = dsigma
        self._greeks = greeks

    def get_greeks(self):
        calculatedGreeks = dict()

        if ('price' in self._greeks):
            calculatedGreeks['price': VanillaEuropeanOption(self.__flag, self.__s + self.__ds, self.__x, self.__r, self.__b, self.__t, self.__sigma).get_price()]

        if ('delta' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s + self.__ds, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s - self.__ds, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            delta = (option1.get_price() - option2.get_price()) / (2 * self.__ds)
            calculatedGreeks['delta': delta]

        if ('gamma' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s + self.__ds, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            option3 = VanillaEuropeanOption(self.__flag, self.__s - self.__ds, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            gamma = (option1.get_price() - (2 * option2.get_price()) + option3.get_price()) / math.pow(self.__ds, 2)
            calculatedGreeks['gamma': gamma]

        if ('theta' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b, self.__t + self.__dt, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b, self.__t - self.__dt, self.__sigma)
            theta = (option1.get_price() - option2.get_price()) / self.__dt
            calculatedGreeks['theta': theta]

        if ('vega' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b, self.__t, self.__sigma)
            vega = (option1.get_price() - option2.get_price()) / 2
            calculatedGreeks['vega': vega]

        if ('rho' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r + self.__dr, self.__b + self.__db, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r - self.__dr, self.__b - self.__db, self.__t, self.__sigma)
            rho = (option1.get_price() - option2.get_price()) / 2
            calculatedGreeks['rho': rho]

        if ('rho_futures' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r + self.__dr, self.__b, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r - self.__dr, self.__b, self.__t, self.__sigma)
            rho_futures = (option1.get_price() - option2.get_price()) / 2
            calculatedGreeks['rho_futures': rho_futures]


        if ('rho_2' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b - self.__db, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b + self.__db, self.__t, self.__sigma)
            rho_2 = (option1.get_price() - option2.get_price()) / 2
            calculatedGreeks['rho_2': rho_2]


        if ('rho_carry' in self._greeks):
            option1 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b + self.__db, self.__t, self.__sigma)
            option2 = VanillaEuropeanOption(self.__flag, self.__s, self.__x, self.__r, self.__b - self.__db, self.__t, self.__sigma)
            rho_carry = (option1.get_price() - option2.get_price()) / 2
            calculatedGreeks['rho_carry': rho_carry]

        return calculatedGreeks