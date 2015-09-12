import math


class ConvexityBasis:
    def __init__(self, f, kappa, t1, t2, sigma, tau):
        self.f = f
        self.kappa = kappa
        self.t1 = t1
        self.t2 = t2
        self.sigma = sigma
        self.tau = tau

    def get_value(self):
        z = (math.pow(self.sigma,2) * ((1 - math.exp(-2 * self.kappa * self.t1))/(2 * self.kappa)) * math.pow((1 - math.exp(-self.kappa * (self.t2 - self.t1)))/self.kappa, 2)) + ((0.5 * math.pow(self.sigma, 2)/self.kappa) * (1 - math.exp(-self.kappa * (self.t2 - self.t1))) * ())


        return 0