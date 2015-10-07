import math
from src.mathematics.distributions.cumulative_normal_distribution import N


# Cumulative bivariate normal density function
# Drezner (1978) approximation
@staticmethod
def M(a, b, rho):
    result = None

    if a <= 0 and b <= 0 and rho <= 0:
        result = __phi(a, b, rho)
    elif a <= 0 and b >= 0 and rho >= 0:
        result = N(a) - __phi(a, -b, -rho)
    elif a >= 0 and b <= 0 and rho >= 0:
        result = N(a) - __phi(-a, b, -rho)
    elif a >= 0 and b >= 0 and rho <= 0:
        result = N(a) + N(b) - 1 + __phi(-a, -b, rho)
    elif a * b * rho > 0:
        rho1 = ((rho * a - b) * math.copysign(1, a)) / (math.sqrt(math.pow(a, 2) + (2 * rho * a * b) + math.pow(b, 2)))
        rho2 = ((rho * b - a) * math.copysign(1, b)) / (math.sqrt(math.pow(a, 2) + (2 * rho * a * b) + math.pow(b, 2)))
        delta = (1 - math.copysign(1, a) * math.copysign(1, b))
        result = M(a, 0, rho1) + M(b, 0, rho2) - delta
    return result


@staticmethod
def __phi(a, b, rho):
    sum = 0
    a1 = a / math.sqrt(2 * (1 - math.pow(rho, 2)))
    b1 = b / math.sqrt(2 * (1 - math.pow(rho, 2)))
    x = [0.24840615, 0.39233107, 0.21141819, 0.033246660, 0.00082485334]
    y = [0.10024215, 0.48281397, 1.0609498, 1.7797294, 2.6697604]

    f = lambda i, j: math.exp((a1 * (2 * y[i] - a1)) + (b1 * (2 * y[j] - b1) + (2 * rho * (y[i] - a1) * (y[j] - b1))))

    for i in range(0, 5):
        for j in range(0, 5):
            sum += x[i] * x[j] * f(i, j)
    return math.sqrt(1 - math.pow(rho, 2)) * sum / math.pi
