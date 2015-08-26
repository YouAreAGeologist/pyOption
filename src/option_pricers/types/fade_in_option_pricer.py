import math
from src.mathematics.distributions.cumulative_bivariate_normal_distribution import M


class FadeInOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        x = option['x']
        l = option['l']
        u = option['u']
        n = option['n']
        h = option['h']
        r = option['r']
        b = option['b']
        t = option['t']
        sigma = option['sigma']

        d1 = (math.log(s/x) + (b + 0.5 * math.pow(sigma, 2))*t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)

        sum = 0
        for i in range(1, n+1):
            t1 = i * t / n
            d3 = (math.log(s/l) + (b + 0.5 * math.pow(sigma, 2))*t)/(sigma * math.sqrt(t1))
            d4 = d3 - sigma * math.sqrt(t1)
            d5 = (math.log(s/u) + (b + 0.5 * math.pow(sigma, 2))*t)/(sigma * math.sqrt(t1))
            d6 = d5 - sigma * math.sqrt(t1)
            rho = math.sqrt(t1)/math.sqrt(t)

            if flag == 'call':
                sum += (math.pow(s, (b-r)*t) * (M(-d5, d1, -rho) - M(-d3, d1, -rho))) - (x * math.exp(-r*t) * ((M(-d6, d2, -rho) - M(-d4, d2, -rho))))
            elif flag == 'put':
                sum += -(math.pow(s, (b-r)*t) * (M(-d5, d1, rho) -M(-d3, -d1, rho))) + (x * math.exp(-r*t) * ((M(-d6, -d2, rho) - M(-d4, -d2, rho))))

        return sum / n