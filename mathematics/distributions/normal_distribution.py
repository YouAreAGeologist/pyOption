import math


# Normal distribution function
def n(x):
    return math.exp(-math.pow(x, 2) / 2) / math.sqrt(2 * math.pi)