# Volatility functions library

class Volatility:
    
    @staticmethod
    def get_historical_volatility_from_close_prices(close_prices):
        result = None
        n = len(close_prices)
        sum1 = 0
        sum2 = 0
        
        for i in (1,n):
            sum1 += math.pow(math.log(close_prices[i]/close_prices[i-1]),2)
            sum2 += math.log(close_prices[i]/close_prices[i-1])
        
        return math.sqrt((sum1/(n-1)) - ((math.pow(close_prices[i]/close_prices[i-1],2)/(n * (n-1)))))
        
    