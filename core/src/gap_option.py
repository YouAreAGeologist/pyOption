import math
from mathematics.src.distribution import cnd


class GapOption:


    def __init__(self, flag, s, x1, x2, r, b, t, sigma):
        self.__flag = flag
        self.__s = s
        self.__x1 = x1
        self.__x2 = x2
        self.__r = r
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__d1 = (math.log(s / x1) + (b + math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        self.__d2 = self.__d1 - sigma * math.sqrt(t)


    def get_price(self):
        result=None
        if self.__flag == 'c':
            result = (self.__s * math.exp((self.__b - self.__r) * self.__t) * cnd(self.__d1)) - (self.__x2 * math.exp(-self.__r * self.__t) * cnd(self.__d2))
        elif self.__flag == 'p':
            result = (self.__x2 * math.exp(-self.__r * self.__t) * cnd(-self.__d2)) - ((self.__s * math.exp(self.__b - self.__r)  * self.__t) * cnd(-self.__d1))
        return result