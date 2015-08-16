import math
from mathematics.src.distribution import cnd


class AssetOrNothingOption():


    def __init__(self, flag, s, x, k, b, t, sigma):
        self.__flag = flag
        self.__s = s
        self.__x = x
        self.__k = k
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__d = (math.log(s / x) + (b - math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        
        
    def get_price(self, result=None):
        if self.__flag == 'c':
            result = self.__k * math.exp(self.__r * self.__t) * cnd(self.__d)
        elif self.__flag == 'p':
            result = self.__k * math.exp(self.__r * self.__t) * cnd(-self.__d)
        return result