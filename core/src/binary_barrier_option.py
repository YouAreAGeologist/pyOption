import math
from mathematics.src.distribution import cnd

class BinaryBarrierOption:


    def __init__(self, flag, s, x, h, k, r, b, t, sigma, greeks):
        self.__flag = flag
        self.__s = s
        self.__x = x
        self.__k = k
        self.__h = h
        self.__r = r
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__greeks = greeks
        self.__mu = (b - math.pow(sigma, 2)/2)/math.pow(sigma, 2)
        self.__lmd = math.sqrt(math.pow(self.__mu, 2) + (2*r/math.pow(sigma, 2)))
        self.__z = (math.log(h/s)/(sigma * math.sqrt(t))) + (self.__lmd * sigma * math.sqrt(t))
        self.__x1 = (math.log(s/x)/(sigma * math.sqrt(t))) + ((self.__mu + 1) * sigma * math.sqrt(t))
        self.__x2 = (math.log(s/h)/(sigma * math.sqrt(t))) + ((self.__mu + 1) * sigma * math.sqrt(t))
        self.__y1 = (math.log(math.pow(h, 2)/(s * x))/(sigma * math.sqrt(t))) + ((self.__mu + 1) * sigma * math.sqrt(t))
        self.__y2 = (math.log(h/s)/(sigma * math.sqrt(t))) + ((self.__mu + 1) * sigma * math.sqrt(t))

    def get_values(self):
        results = dict()
        price = None
        if self.__flag == 'down-and-in cash-at-hit-or-nothing':
            price = self.__a5(1)
        elif self.__flag == 'up-and-in cash-at-hit-or-nothing':
            price = self.__a5(-1)
        elif self.__flag == 'down-and-in asset-at-hit-or-nothing':
            price = self.__a5(1)
        elif self.__flag == 'up-and-in asset-at-hit-or-nothing':
            price = self.__a5(-1)
        elif self.__flag == 'down-and-in cash-at-expiration-or-nothing':
            price = self.__b2(-1) + self.__b4(1)
        elif self.__flag == 'up-and-in cash-at-expiration-or-nothing':
            price = self.__b2(1) + self.__b4(-1)
        elif self.__flag == 'down-and-in asset-at-expiration-or-nothing':
            price = self.__a2(-1) + self.__a4(1)
        elif self.__flag == 'up-and-in asset-at-expiration-or-nothing':
            price = self.__a2(1) + self.__a4(-1)
        elif self.__flag == 'down-and-out cash-or-nothing':
            price = self.__b2(1) - self.__b4(1)
        elif self.__flag == 'up-and-out cash-or-nothing':
            price = self.__b2(-1) - self.__b4(-1)
        elif self.__flag == 'down-and-out asset-or-nothing':
            price = self.__a2(1) - self.__a4(1)
        elif self.__flag == 'up-and-out asset-or-nothing':
            price = self.__a2(-1) - self.__a4(-1)
        elif self.__flag == 'down-and-in cash-or-nothing call':
            if self.__x > self.__h:
                price = self.__b3(1)
            elif self.__x < self.__h:
                price = self.__b1(1) - self.__b2(-1) + self.__b4(-1)
        elif self.__flag == 'up-and-in cash-or-nothing call':
            if self.__x > self.__h:
                price = self.__b1(1)
            elif self.__x < self.__h:
                price = self.__b2(1) - self.__b3(-1) + self.__b4(-1)
        elif self.__flag == 'down-and-in asset-or-nothing call':
            if self.__x > self.__h:
                price = self.__a3(1)
            elif self.__x < self.__h:
                price = self.__a1(1) - self.__a2(1) + self.__a4(1)
        elif self.__flag == 'up-and-in asset-or-nothing call':
            if self.__x > self.__h:
                price = self.__a1(1)
            elif self.__x < self.__h:
                price = self.__a2(1) - self.__a3(-1) + self.__a4(-1)
        elif self.__flag == 'down-and-in cash-or-nothing put':
            if self.__x > self.__h:
                price = self.__b2(-1) - self.__b3(1) + self.__b4(1)
            elif self.__x < self.__h:
                price = self.__b1(-1)
        elif self.__flag == 'up-and-in cash-or-nothing put':
            if self.__x > self.__h:
                price = self.__b1(-1) - self.__b2(-1) + self.__b4(-1)
            elif self.__x < self.__h:
                price = self.__b3(-1)
        elif self.__flag == 'down-and-in asset-or-nothing put':
            if self.__x > self.__h:
                price = self.__a2(-1) - self.__a3(1) + self.__a4(1)
            elif self.__x < self.__h:
                price = self.__a1(-1)
        elif self.__flag == 'up-and-in asset-or-nothing put':
            if self.__x > self.__h:
                price = self.__a1(-1) + self.__a2(-1) + self.__a3(-1)
            elif self.__x < self.__h:
                price = self.__a3(-1)
        elif self.__flag == 'down-and-out cash-or-nothing call':
            if self.__x > self.__h:
                price = self.__b1(1) - self.__b3(1)
            elif self.__x < self.__h:
                price = self.__b2(1) - self.__b4(1)
        elif self.__flag == 'up-and-out cash-or-nothing call':
            if self.__x > self.__h:
                price = 0
            elif self.__x < self.__h:
                price = self.__b1(1) - self.__b2(1) + self.__b3(-1) - self.__b4(-1)
        elif self.__flag == 'down-and-out asset-or-nothing call':
            if self.__x > self.__h:
                price = self.__a1(1) - self.__a3(1)
            elif self.__x < self.__h:
                price = self.__a2(1) - self.__a4(1)
        elif self.__flag == 'up-and-out asset-or-nothing call':
            if self.__x > self.__h:
                price = 0
            elif self.__x < self.__h:
                price = self.__a1(1) - self.__a2(1) + self.__a3(-1) - self.__a4(-1)
        elif self.__flag == 'down-and-out cash-or-nothing put':
            if self.__x > self.__h:
                price = self.__b1(-1) - self.__b2(-1) + self.__b3(1) - self.__b4(1)
            elif self.__x < self.__h:
                price = 0
        elif self.__flag == 'up-and-out cash-or-nothing put':
            if self.__x > self.__h:
                price = self.__b2(-1) - self.__b4(-1)
            elif self.__x < self.__h:
                price = self.__b1(-1) - self.__b3(-1)
        elif self.__flag == 'down-and-out asset-or-nothing put':
            if self.__x > self.__h:
                price = self.__a1(-1) - self.__a2(-1) + self.__a3(1) - self.__a4(1)
            elif self.__x < self.__h:
                price = 0
        elif self.__flag == 'up-and-out asset-or-nothing put':
            if self.__x > self.__h:
                price = self.__a2(-1) - self.__a4(-1)
            elif self.__x < self.__h:
                price = self.__a1(-1) - self.__a3(-1)
        results['price'] = price

        return results


    def __a1(self, phi):
        return self.__s * math.exp((self.__b - self.__r) * self.__t) * cnd(phi * self.__x1)


    def __b1(self, phi):
        return self.__k * math.exp(-self.__r * self.__t) * cnd((phi * self.__x1) - (phi * self.__sigma * math.sqrt(self.__t)))


    def __a2(self, phi):
        return self.__s * math.exp((self.__b - self.__r) * self.__t) * cnd(phi * self.__x2)


    def __b2(self, phi):
        return self.__k * math.exp(-self.__r * self.__t) * cnd((phi * self.__x2) - (phi * self.__sigma * math.sqrt(self.__t)))


    def __a3(self, eta):
        return self.__s * math.exp((self.__b - self.__r) * self.__t) * math.pow(self.__h/self.__s, 2 * (self.__mu + 1)) * cnd(eta * self.__y1)


    def __b3(self, eta):
        return self.__k * math.exp(-self.__r * self.__t) * math.pow(self.__h/self.__s, 2 * self.__mu) * cnd((eta * self.__y1) - (eta * self.__sigma * math.sqrt(self.__t)))


    def __a4(self, eta):
        return self.__s * math.exp((self.__b - self.__r) * self.__t) * math.pow(self.__h/self.__s, 2 * (self.__mu + 1)) * cnd(eta * self.__y2)


    def __b4(self, eta):
        return self.__k * math.exp(-self.__r * self.__t) * math.pow(self.__h/self.__s, 2 * self.__mu) * cnd((eta * self.__y2) - (eta * self.__sigma * math.sqrt(self.__t)))


    def __a5(self, eta):
        return self.__k * (math.pow(self.__h/self.__s, self.__mu + self.__lmd) * cnd(eta * self.__z) + math.pow(self.__h/self.__s, self.__mu - self.__lmd) * cnd((eta * self.__z) - (2 * eta * self.__lmd * self.__sigma * math.sqrt(self.__t))))