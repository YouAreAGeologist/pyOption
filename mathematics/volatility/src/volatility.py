import math


def get_historical_volatility_from_close_prices(prices):
    n = len(prices)
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        sum1 += math.pow(math.log(prices[i].close/prices[i-1].close), 2)
        sum2 += math.log(prices[i].close/prices[i-1].close)
    return math.sqrt((sum1/(n-1)) - (math.pow(sum2, 2)/(n * (n-1))))


# Parkinson (1980)
def get_high_low_volatility(prices):
    n = len(prices)
    sum = 0
    for i in range(0, n):
        sum += math.log(prices[i].high/prices[i].low)
    return sum/(2 * n * math.sqrt(math.log(2)))


# Garman and Klass (1980)
def get_high_low_close_volatility(prices):

    n = len(prices)
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        sum1 += 0.5 * math.pow(math.log(prices[i].high/prices[i].low), 2)
        sum2 += (2 * math.log(2) - 1) * math.pow(math.log(prices[i].close/prices[i-1].close), 2)
    return math.sqrt((sum1-sum2)/n)