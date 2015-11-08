import math


class GenericEuropeanBinomialOption:
    def __init__(self, flag, optionType, s, x, r, b, t, n, sigma, pow=None, cap=None):
        self.flag = flag
        self.optionType = optionType
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.n = n
        self.sigma = sigma
        self.dt = t / n
        self.u = math.exp(sigma * math.sqrt(self.dt))
        self.d = 1 / self.u
        self.p = (math.exp(self.b * self.dt) - self.d) / (self.u - self.d)
        self.pow = pow
        self.cap = cap

        if self.flag == 'c':
            self.z = 1
        elif self.flag == 'p':
            self.z = -1

    def get_value(self):
        sum = 0
        for i in range(0, self.n + 1):
            si = self.s * (self.u * self.i) * (self.d * (self.n - self.i))
            sum += (math.factorial(self.n) / math.factorial(i) * math.factorial(
                self.n - i)) * self.__get_binomial_payoff(si)
        result = math.exp(-self.r * self.t) * sum

    def __get_binomial_payoff(self, si):
        result = None
        if self.optionType == 'plain vanilla':
            result = max(self.z * (si - self.x), 0)
        elif self.optionType == 'power contract 1':
            result == math.pow(si, self.pow)
        elif self.optionType == 'capped power contract':
            result = min(math.pow(si, self.pow), self.cap)
        elif self.optionType == 'power contact 2':
            result = math.pow(self.s / self.x, self.pow)
        elif self.optionType == 'power contact 3':
            result = math.pow(self.z * (si - self.x), self.pow)
        elif self.optionType == 'standard power option':
            result = max(self.z * math.pow(si - self.x, self.pow), 0)
        elif self.optionType == 'capped power option*':
            result = min(max(self.z * (math.pow(si, self.pow) - self.x), 0), self.cap)
        elif self.optionType == 'powered option':
            result = math.pow(max(self.z * (si - self.x), 0), self.pow)
        elif self.optionType == 'capped power option':
            result = min(math.pow(max(self.z * (si - self.x), 0), self.cap), self.cap)
        elif self.optionType == 'sinus option':
            result = max(self.z * (math.sin(si) - self.x), 0)
        elif self.optionType == 'cosinus option':
            result = max(self.z * (math.cos(si) - self.x), 0)
        elif self.optionType == 'tangens options':
            result = max(self.z * (math.tan(si) - self.x), 0)
        elif self.optionType == 'log contract 1':
            result = math.log(si)
        elif self.optionType == 'log contract 2':
            result = math.log(si / self.x)
        elif self.optionType == 'log option':
            result = max(math.log(si / self.x), 0)
        elif self.optionType == 'square root contract 1':
            result = math.sqrt(si)
        elif self.optionType == 'square root contract 2':
            result = math.sqrt(si / self.x)
        elif self.optionType == 'square root option':
            result = math.sqrt(max(self.z * (si - self.x), 0))
        return result
