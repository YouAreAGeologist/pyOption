import math
from mathematics.src.random import rand


class EuropeanVanillaOptionMonteCarlo:
    def __init__(self, flag, s, x, r, b, t, sigma, n, greeks):
        self.__flag = flag
        self.__s = s
        self.__x = x
        self.__r = r
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__n = n
        self.__greeks = greeks

    def get_values(self):
        results = dict()
        sum = 0
        z = 0
        if self.__flag == 'c':
            z = 1
        elif self.__flag == 'p':
            z = -1

        for i in self.__n:
            st = self.__s * math.exp((self.__b - math.pow(self.__sigma, 2) * self.__t) + (self.__sigma * math.sqrt(self.__t)) * rand())
            sum += max(z * (st - self.__x), 0)

        results['price'] = math.exp(-self.__r * self.__t) * sum / self.__n

        if 'delta' in self.__greeks:
            results['delta'] = math.exp(self.__r * self.__t) * sum / (self.__s * self.__n)
        if 'gamma' in self.__greeks:
            results['gamma'] = math.exp(self.__r * self.__t) * math.pow(self.__x / self.__s, 2) * sum / (4 * self.__n)
        if 'theta' in self.__greeks:
            results['theta'] = 0
        if 'vega' in self.__greeks:
            results['vega'] = (math.exp(self.__r * self.__t) * math.pow(self.__x / self.__s, 2) * sum / (4 * self.__n)) * self.__sigma * math.pow(self.__s, 2) * self.__t
        return results