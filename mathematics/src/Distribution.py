import math


def ndf(x):
    return math.exp(-math.pow(x, 2) / 2) / math.sqrt(2 * math.pi)


def cnd(x):
    a1 = 0.31938153
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429

    if x == 0:
        return 0.5
    elif x > 10:
        return 1
    elif x < -10:
        return 0
    else:
        l = math.fabs(x)
        k = 1 / (1 + 0.2316419 * l)
        n = 1 - 1 / math.sqrt(2 * math.pi) * math.exp(-math.pow(l, 2) / 2) * (
            (a1 * k) + (a2 * math.pow(k, 2)) + (a3 * math.pow(k, 3) + (a4 * math.pow(k, 4) + (a5 * math.pow(k, 5)))))
        if x < 0:
            n = 1 - n
    return n
