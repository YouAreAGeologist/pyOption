# Vanilla European option calculator

import math
import Distributions

class VanillaOptionDistributionCalculator:
    
    def getBlackScholesEquityOptionPrice(flag,s,x,k,r,t,sigma):
        result = None
        d1 = (math.log(s/x) + (r + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = (s * cnd(d1)) - (x * math.exp(-r * t) * cnd(d2))
        elif flag == 'p':
            result = (x * math.exp(-r * t) * cnd(-d2)) - (s * cnd(-d1))
        return result
        
    def getStockIndexOptionPrice(flag,s,x,k,q,r,t,sigma):
        result = None
        d1 = (math.log(s/x) + (r - q + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = (s * math.exp(-q*t) * cnd(d1)) - (x*math.exp(-r*t) * cnd(d2))
        elif flag == 'p':
            result = (x*math.exp(-r*t)*cnd(-d2)) - (s*math.exp(-q*t)*cnd(-d1))
        return result
        
    def getOptionOnFuturesPrice(flag,f,x,k,r,t,sigma):
       result = None
       
       return result
        
    def getCurrencyOptionPrice():
        result = None
        d1 = (math.log(f/x) + (math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = 0
        elif flag = 'p':
            ressult = 0
        return result
        
    # Greeks implementations for equity and fx options
    