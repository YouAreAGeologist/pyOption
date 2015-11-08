import math


# Bivariate normal density function
def b(x, y, rho):
    return (1 / (2 * math.pi * math.sqrt(1 - math.pow(rho, 2)))) * math.exp(
        -(math.pow(x, 2) - 2 * rho * x * y + math.pow(y, 2)) / (2 * (1 - math.pow(rho, 2))))