import math
from mathematics.src.distribution import cnd

class Caplet:
    def __init__(self, notional, f, x, r, t, sigma, tau, basis):
        self.__notional = notional
        self.__f = f
        self.__x = x
        self.__r = r
        self.__t = t
        self.__sigma = sigma
        self.__tau = tau
        self.__basis = basis
        self.__d1=(math.log(f / x) + (math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        self.__d2=self.__d1 - (sigma * math.sqrt(t))

    def get_value(self):
        return (self.__notional * (self.__tau / self.__basis) / (1 + (self.__f * self.__tau) / self.__basis)) * math.exp(-self.__r * self.__t * ((self.__f * cnd(self.__d1)) -(self.__x * self.__d2)))
