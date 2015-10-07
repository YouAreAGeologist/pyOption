import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class VasicekModel:
    def __init__(self, flag, f, x, t, T, tau, r, kappa, theta, sigma):
        self.flag = flag
        self.x = x
        self.t = t
        self.T = T
        self.tau = tau
        self.r = r
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma

    def get_value(self):
        result = None
        sigma_p = self.__b(self.t, self.T) * math.sqrt(
            (math.pow(self.sigma, 2) * (1 - math.exp(-2 * self.kappa * (self.T - self.t)))) / (2 * self.kappa))
        h = (math.log(self.__p(self.t, self.tau) / (self.__p(self.t, self.T) * self.x)) / sigma_p) + 0.5 * sigma_p
        b_t_T = self.__b(self.t, self.T)
        b_T_tau = self.__b(self.T, self.tau)
        b_t_tau = self.__b(self.t, self.tau)
        a_t_tau = self.__a(self.t, self.T)
        a_T_tau = self.__a(self.T, self.t)
        a_t_tau = self.__a(self.t, self.t)
        p_t_tau = self.__p(self.t, self.tau)
        p_t_T = self.__p(self.t, self.T)

        if self.flag == 'call':
            result = (self.__p(self.t, self.T) * N(h)) - (self.x * self.__p(self.t, self.T) * N(h - sigma_p))
        elif self.flag == 'put':
            result = (self.x * self.__p(self.t, self.T) * N(-h + sigma_p)) - (self.__p(self.t, self.T) * N(-h))
        return result

    def __p(self, t1, t2):
        return self.__a(t1, t2) * math.exp(-self.__b * self.r)

    def __a(self, b, t1, t2):
        return math.exp((((b - t2 + t1) * (math.pow(self.kappa, 2) - 0.5 * math.pow(self.sigma, 2))) / math.pow(
            self.kappa, 2)) - ((math.pow(self.sigma, 2) * math.pow(b, 2)) / (4 * self.kappa)))

    def __b(self, t1, t2):
        return (1 - math.exp(-self.kappa * (t2 - t1))) / self.kappa
