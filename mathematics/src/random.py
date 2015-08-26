import math


def rand():
    x = 1
    while x >= 1:
       t = math.tan(math.pi * x)
       l = math.sqrt(-2 * math.log(x))
       x = l * (1 - math.pow(t, 2)) / (1 + math.pow(t, 2))
    return x