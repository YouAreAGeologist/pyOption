import math


class GenericEuropeanBinomialOption:
    def __init__(self, flag, optionType, s, x, r, b, t, n, sigma, pow=None, cap=None):
        self.__flag = flag
        self.__optionType = optionType
        self.__s = s
        self.__x = x
        self.__r = r
        self.__b = b
        self.__t = t
        self.__n = n
        self.__sigma = sigma
        self.__dt = t/n
        self.__u = math.exp(sigma * math.sqrt(self.__dt))
        self.__d = 1 / self.__u
        self.__p = (math.exp(self.__b * self.__dt) - self.__d) / (self.__u - self.__d)
        self.__pow = pow
        self.__cap = cap

        if self.__flag == 'c':
            self.__z = 1
        elif self.__flag == 'p':
            self.__z = -1


    def get_price(self):
        sum = 0
        for i in range(0, self.__n + 1):
            si = self.__s * (self.__u * self.i) * (self.__d * (self.__n - self.i))
            sum += (math.factorial(self.__n) / math.factorial(i) * math.factorial(self.__n - i)) * self.__get_binomial_payoff(si)
        result = math.exp(-self.__r * self.__t) * sum


    def __get_binomial_payoff(self, si):
        result=None
        if self.__optionType == 'plain vanilla':
            result = max(self.z * (si - self.__x), 0)
        elif self.__optionType == 'power contract 1':
            result == math.pow(si, self.__pow)
        elif self.__optionType == 'capped power contract':
            result = min(math.pow(si, self.__pow), self.__cap)
        elif self.__optionType == 'power contact 2':
            result = math.pow(self.__s / self.__x, self.__pow)
        elif self.__optionType == 'power contact 3':
            result = math.pow(self.__z * (si - self.__x), self.__pow)
        elif self.__optionType == 'standard power option':
            result = max(self.__z * math.pow(si - self.__x, self.__pow), 0)
        elif self.__optionType == 'capped power option*':
            result = min(max(self.__z * (math.pow(si, self.__pow) - self.__x), 0), self.__cap)
        elif self.__optionType == 'powered option':
            result = math.pow(max(self.__z * (si - self.__x), 0), self.__pow)
        elif self.__optionType == 'capped power option':
            result = min(math.pow(max(self.__z * (si - self.__x), 0), self.__cap), self.__cap)
        elif self.__optionType == 'sinus option':
            result = max(self.__z * (math.sin(si) - self.__x), 0)
        elif self.__optionType == 'cosinus option':
            result = max(self.__z * (math.cos(si) - self.__x), 0)
        elif self.__optionType == 'tangens options':
            result = max(self.__z * (math.tan(si) - self.__x), 0)
        elif self.__optionType == 'log contract 1':
            result = math.log(si)
        elif self.__optionType == 'log contract 2':
            result = math.log(si / self.__x)
        elif self.__optionType == 'log option':
            result = max(math.log(si / self.__x) , 0)
        elif self.__optionType == 'square root contract 1':
            result = math.sqrt(si)
        elif self.__optionType == 'square root contract 2':
            result = math.sqrt(si / self.__x)
        elif self.__optionType == 'square root option':
            result = math.sqrt(max(self.__z * (si - self.__x) , 0))
        return result