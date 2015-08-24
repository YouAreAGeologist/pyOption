import math
from mathematics.src.distribution import cnd


class Swaption:
    def __init__(self, flag, f, x, r, t, t1, sigma, m):
        self.__flag = flag
        self.__f = f
        self.__x = x
        self.__r = r
        self.__t = t
        self.__t1 = t1
        self.__sigma = sigma
        self.__m = m
        self.__d1 = (math.log(f / x) + ((math.pow(sigma, 2)/2) * t)) / (sigma * math.sqrt(t))
        self.__d2 = self.__d1 - (sigma * math.sqrt(t))

    def get_value(self):
        result=None
        if self.__flag == 'c':
            result = ((1 - (1 / (math.pow(1 + (self.__f / self.__m), self.__t1 * self.__m)))) / self.__f) * math.exp(-self.__r * self.__t) * ((self.__f * cnd(self.__d1)) - (self.x * cnd(self.__d2)))
        elif self.__flag == 'p':
            result = ((1 - (1 / (math.pow(1 + (self.__f / self.__m), self.__t1 * self.__m)))) / self.__f) * math.exp(-self.__r * self.__t) * ((self.__x * cnd(-self.__d2)) - (self.f * cnd(-self.__d1)))
        return result