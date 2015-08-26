import math
from src.mathematics.distributions.cumulative_normal_distribution import N
from src.mathematics.distributions.cumulative_bivariate_normal_distribution import M


class PartialTimeFloatingStrikeLookbackOptionPricer:
    def __init__(self, params):

        '''

        do params checking for s_min/s_max for calls and puts

        check lambda as rules for calls and puts on what values this can take

        '''


        self.__params = params

    def get_price(self):
        result = None
        option = self.__params['option']
        flag = option['flag']
        s = option['s']
        s_min = option['s_min']
        s_max = option['s_max']
        r = option['r']
        b = option['b']
        t1 = option['t1']
        t2 = option['t2']
        sigma = option['sigma']
        lmd = option['lmd']

        m0 = None
        if flag == 'call':
            m0 = s_min
        elif flag == 'put':
            m0 = s_max

        d1 = (math.log(s/m0) + (b + 0.5 * math.pow(sigma, 2) * t2))/(sigma * math.sqrt(t2))
        d2 = d1 - sigma * math.sqrt(t2)
        e1 = ((b + 0.5 * math.pow(sigma, 2)/2) * (t2 - t1))/(sigma * math.sqrt(t2 - t1))
        e2 = e1 - sigma * math.sqrt(t2 - t1)
        f1 = (math.log(s/m0) + (b + 0.5 * math.pow(sigma, 2)) * t1)/(sigma * math.sqrt(t1))
        f2 = f1 - sigma * math.sqrt(t1)
        g1 = math.log(lmd)/(sigma * math.sqrt(t2))
        g2 = math.log(lmd)/(sigma * math.sqrt(t2 - t1))

        if flag == 'call':
            a1 = lmd * s_min * math.exp(-r *t2) * N(d2 - g1)
            a2 = s * math.exp((b-r)*t2) * N(d1 - g1)
            a3 = lmd * s * math.exp(-r * t2) * math.sqrt(sigma, 2)/(2*b)
            b1 = math.pow(s/s_min, -2*b/math.pow(sigma, 2)) * M(-f1 + (2*b*math.sqrt(t1)/sigma), -d1 + (2*b*math.sqrt(t2)/sigma) - g1, math.sqrt(t1/t2))
            b2 = math.exp(b*t2) * math.pow(lmd, 2*b/math.pow(sigma, 2)) * M(-d1-g1, e1+g2, -math.sqrt(1 - (t1/t2)))
            c1 = s * math.exp((b-r)*t2) * M(-d1+g1, e1-g2, -math.sqrt(1 - (t1/t2)))
            c2 = lmd * s_min * math.exp(-r*t2) * M(-f2, d2-g1, -math.sqrt(t1/t2))
            c3 = math.exp(-b * (t2 - t1)) * (1 + math.pow(sigma, 2)/(2*b)) * lmd * s * math.exp((b-r)*t2) * N(e2 - g2) * N(-f1)
            result = -a1 + a2 + (a3 * (b1 - b2)) + c1 + c2 - c3
        elif flag == 'put':
            a1 = lmd * s_max * math.exp(-r *t2) * N(-d2 + g1)
            a2 = s * math.exp((b-r)*t2) * N(-d1 + g1)
            a3 = lmd * s * math.exp(-r * t2) * math.sqrt(sigma, 2)/(2*b)
            b1 = -math.pow(s/s_max, -2*b/math.pow(sigma, 2)) * M(f1 - (2*b*math.sqrt(t1)/sigma), d1 - (2*b*math.sqrt(t2)/sigma) + g1, math.sqrt(t1/t2))
            b2 = math.exp(b*t2) * math.pow(lmd, 2*b/math.pow(sigma, 2)) * M(d1+g1, -e1-g2, -math.sqrt(1 - (t1/t2)))
            c1 = s * math.exp((b-r)*t2) * M(d1-g1, -e1+g2, -math.sqrt(1 - (t1/t2)))
            c2 = lmd * s_max * math.exp(-r*t2) * M(-f2, -d2+g1, -math.sqrt(t1/t2))
            c3 = math.exp(-b * (t2 - t1)) * (1 + math.pow(sigma, 2)/(2*b)) * lmd * s * math.exp((b-r)*t2) * N(-e2 + g2) * N(f1)
            result = a1 - a2 + (a3 * (b1 + b2)) - c1 - c2 + c3
        return result

