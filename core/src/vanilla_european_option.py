import math
from mathematics.src.distribution import ndf, cnd


class VanillaEuropeanOption:
    def __init__(self, flag, s, x, r, b, t, sigma):
        self.__flag = flag
        self.__s = s
        self.__x = x
        self.__r = r
        self.__b = b
        self.__t = t
        self.__sigma = sigma
        self.__d1 = (math.log(s / x) + (r - b + math.pow(sigma, 2) / 2) * t) / (sigma * math.sqrt(t))
        self.__d2 = self.__d1 - sigma * math.sqrt(t)

    # Option price
    def get_price(self):
        result=None
        if self.__flag == 'c':
            result = (self.__s * math.exp(-self.__b * self.__t) * cnd(self.__d1)) - (self.__x * math.exp(-self.__r * self.__t) * cnd(self.__d2))
        elif self.__flag == 'p':
            result = (self.__x * math.exp(-self.__r * self.__t) * cnd(-self.__d2)) - (self.__s * math.exp(-self.q * self.__t) * cnd(-self.__d1))
        return result

    # Delta (spot delta)
    def get_delta(self):
        result=None
        if self.__flag == 'c':
            result = math.exp((self.__b - self.__r) * self.__t) * cnd(self.__d1)
        elif self.__flag == 'p':
            result = math.exp((self.__b - self.__r) * self.__t) * (cnd(self.__d1) - 1)
        return result

    # # DdeltaDvol, vanna
    # def get_ddelta_dvol():
    #     return (-math.exp((b - r) * t) * d2 * ndf(d1)) / sigma
    #
    # # Ddeltatime, charm, delta bleed
    # def get_ddelta_dtime():
    #     result = None
    #     if flag == 'c':
    #         result = math.exp((b - r) * t) * (
    #         (cnd(d1) * ((b / (sigma * math.sqrt(t))) - (d2 / (2 * t))) + ((b - r) * cnd(d1))))
    #     elif flag == 'p':
    #         result = math.exp((b - r) * t) * (
    #         (cnd(d1) * ((b / (sigma * math.sqrt(t))) - (d2 / (2 * t))) - ((b - r) * cnd(-d1))))
    #     return result
    #
    # # Elasticity
    # def get_elasticity():
    #     result = None
    #     if flag == 'c':
    #         result = math.exp((b - r) * t) * cnd(d1) * s / get_price()
    #     elif flag == 'p':
    #         result = math.exp((b - r) * t) * (cnd(d1) - 1) * s / get_price()
    #     return result
    #
    # # Gamma greeks
    # #
    #
    # Gamma
    def get_gamma(self):
        return ndf(self.__d1) * math.exp((self.__b - self.__r) * self.__t) / (self.__s * self.__sigma * math.sqrt(self.__t))
    #
    # # Maximal gamma for asset price
    # def get_maximal_gamma_for_asset_price():
    #     return x * (math.exp(-b - 3 * math.pow(sigma, 2) / 2) * t)
    #
    # # Maximal gamma for strike price
    # def get_maximal_gamma_for_strike_price():
    #     return s * math.exp((b + math.pow(sigma, 2) / 2) * t)
    #
    # # Gamma percentage
    # def get_gammaP():
    #     return ndf(d1) * math.exp((b - r) * t) / (100 * sigma * math.sqrt(t))
    #
    # # DgammaDvol, zomma
    # def get_dgamma_dvol():
    #     return get_gamma() * (d1 * d2 - 1) / sigma
    #
    # # DgammaDspot, speed
    # def get_dgamma_dspot():
    #     return -get_gamma() * (1 + (d1 / (sigma * math.sqrt(t)))) / s
    #
    #     # DgammaDtime, color
    #
    # def get_dgamma_dtime():
    #     result = None
    #     return result
    #
    # # Vega greeks
    # #
    #

    # # Vega
    def get_vega(self):
        return self.__s * math.exp((self.__b - self.__r) * self.__t) * ndf(self.__d1) * math.exp(self.__t)
    #
    # # VegaP for 10% change in volatility
    # def get_vegap():
    #     return (sigma * s * math.exp((b - r) * t) * ndf(d1) * math.sqrt(t)) / 10
    #
    # # Vega leverage, elasticity
    # def get_vega_leverage():
    #     return get_vega() * sigma / get_price()
    #
    # # DvegaDvol, vomma
    # def get_dvega_dvol():
    #     return get_vega() * (d1 * d2 / sigma)
    #
    # # DvommaDvol, ultima
    # def get_dvomma_dvol():
    #     return get_dvega_dvol() * (1 / sigma) * ((d1 * d2) - (d1 / d2) - (d2 / d1) - 1)
    #
    # # DvegaDtime
    # def get_dvega_dtime():
    #     return get_vega() * (r - b + ((b * d1) / (sigma * math.sqrt(t))) - ((1 - d1 * d2) / (2 * t)))
    #
    # # Theta greeks
    # #

    # Theta
    def get_theta(self):
        result=None
        if self.__flag == 'c':
            result = - (((self.__s * math.exp((self.__b - self.__r) * self.__t) * ndf(self.__d1) * self.__sigma) / (2 * math.sqrt(self.__t))) - (
            (self.__b - self.__r) * math.exp((self.__b - self.__r) * self.__t) * cnd(self.__d1)) - (self.__r * self.__x * math.exp(-self.__r * self.__t) * cnd(self.__d2)))
        elif self.__flag == 'p':
            result = - (((self.__s * math.exp((self.__b - self.__r) * self.__t) * ndf(self.__d1) * self.__sigma) / (2 * math.sqrt(self.__t))) + (
            (self.__b - self.__r) * math.exp((self.__b - self.__r) * self.__t) * cnd(-self.__d1)) + (self.__r * self.__x * math.exp(-self.__r * self.__t) * cnd(-self.__d2)))
        return result

    #     # Rho greeks
    #
    # #
    #
    # Rho
    def get_rho(self):
        result=None
        if self.__flag == 'c':
            result = self.__r * self.__x * math.exp(-self.__r * self.__t) * cnd(self.__d2)
        elif self.__flag == 'p':
            result = self.__r * self.__x * math.exp(-self.__r * self.__t) * cnd(-self.__d2)
        return result

    # # Phi/Rho-2
    # def get_phi():
    #     result = None
    #     if flag == 'c':
    #         result = -t * math.pow(s, (b - r) * t) * cnd(d1)
    #     elif flag == 'p':
    #         result = t * math.pow(s, (b - r) * t) * cnd(-d1)
    #     return result
    #
    # # Carry Rho
    # def get_carry_rho():
    #     result = None
    #     if flag == 'c':
    #         result = t * math.pow(s, (b - r) * t) * cnd(d1)
    #     elif flag == 'p':
    #         result = -t * math.pow(s, (b - r) * t) * cnd(-d1)
    #     return result
    #
    # # Probability greeks
    # #
    #
    # # In-the-money probability
    # def get_in_the_money_probability():
    #     result = None
    #     if flag == 'c':
    #         result = cnd(d2)
    #     elif flag == 'p':
    #         result = cnd(-d2)
    #     return result
    #
    # # DzetaDvol
    # def get_dzeta_dvol():
    #     result = None
    #     if flag == 'c':
    #         result = -ndf(d2) * d1 / sigma
    #     elif flag == 'p':
    #         result = ndf(d2) * d1 / sigma
    #     return result
    #
    # # DzetaDtime
    # def get_dzeta_dtime():
    #     result = None
    #     if flag == 'c':
    #         result = -ndf(d2) * ((b / (sigma * math.sqrt(t))) - (d1 / (2 * t)))
    #     elif flag == 'p':
    #         result = ndf(d2) * ((b / (sigma * math.sqrt(t))) - (d1 / (2 * t)))
    #     return result
    #
    # # Probability of ever getting in the money
    # def get_probability_of_ever_getting_in_the_money():
    #     result = None
    #     mu = ((b - math.pow(sigma, 2)) / 2)
    #     lmd = math.sqrt(math.pow(mu, 2) + (2 * r / math.pow(sigma, 2)))
    #     z = math.log(x / s) / (sigma * math.sqrt(t)) * (lmb * sigma * math.sqrt(t))
    #     if flag == 'c':
    #         result = (math.pow(x / s, mu + lmd) * cnd(-z)) + (
    #         math.pow(x / s, mu - lmd) * cnd(-z + (2 * lmd * sigma * math.sqrt(t))))
    #     elif flag == 'p':
    #         result = (math.pow(x / s, mu + lmd) * cnd(z)) + (
    #         math.pow(x / s, mu - lmd) * cnd(z - (2 * lmd * sigma * math.sqrt(t))))
    #     return result
