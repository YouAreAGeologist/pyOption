import math


def get_historical_volatility_from_close_prices(close_prices):
    result = None
    n = len(close_prices)
    sum1 = 0
    sum2 = 0
    for i in (1,n):
        sum1 += math.pow(math.log(close_prices[i]/close_prices[i-1]),2)
        sum2 += math.log(close_prices[i]/close_prices[i-1])
    return math.sqrt((sum1/(n-1)) - ((math.pow(close_prices[i]/close_prices[i-1],2)/(n * (n-1)))))


def get_high_low_volatility(low_prices,high_prices):

    n = len(low_prices)
    sum1 = 0
    for i in (1,n):
        sum1 += high_prices(i)/low_prices(i)
    return sum1/(2 * n * math.sqrt(math.log(2)))