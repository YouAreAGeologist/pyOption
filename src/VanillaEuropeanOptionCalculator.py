# Vanilla European option calculator

import math
import Distributions

class VanillaOptionDistributionCalculator:
    
    # Black-Scholes-Merton (1973) option pricing formula
    def getBlackScholesEquityOptionPrice(flag,s,x,r,t,sigma):
        result = None
        d1 = (math.log(s/x) + (r + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = (s * cnd(d1)) - (x * math.exp(-r * t) * cnd(d2))
        elif flag == 'p':
            result = (x * math.exp(-r * t) * cnd(-d2)) - (s * cnd(-d1))
        return result
        
    def getStockIndexOptionPrice(flag,s,x,q,r,t,sigma):
        result = None
        d1 = (math.log(s/x) + (r - q + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = (s * math.exp(-q*t) * cnd(d1)) - (x*math.exp(-r*t) * cnd(d2))
        elif flag == 'p':
            result = (x*math.exp(-r*t)*cnd(-d2)) - (s*math.exp(-q*t)*cnd(-d1))
        return result
        
    def getOptionOnFuturePrice(flag,f,x,r,t,sigma):
        result = None
        d1 = math.log(f/x) + (math.pow(sigma,2)/2) * t
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = math.exp(-r*t) * ((f * cnd(d1) - (x * cnd(d2))))
        elif flag == 'p':
            result = math.exp(-r*t) * ((x * cnd(-d2) - (f * cnd(d1))))
        return result
        
    def getMarginedOptionOnFuturesPrice(flag,f,x,r,t,sigma):
       result = None
       d1 = (math.log(f/x) + (math.pow(sigma,2)/2) * t)/(sigma*math.sqrt(t))
       d2 = d1 - sigma*math.sqrt(t)
       if flag == 'c':
           result = (f * cnd(d1)) - (x * cnd(d2))
       elif flag == 'p':
           result = (x * cnd(-d2)) - (f * cnd(-d1))
       return result
      
    # Garman-Kholhagan formula  
    def getCurrencyOptionPrice(flag,s,x,r,rf,t,sigma):
        result = None
        d1 = (math.log(s/x) + (r - rf + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        d2 = d1 - sigma * math.sqrt(t)
        if flag == 'c':
            result = (s * math.exp(-rf * t) * cnd(d1)) - (x * math.exp(-r * t) * cnd(d2))
        elif flag == 'p':
            result = (x * math.exp(-r * t) * cnd(-d2)) - (s * math.exp(-rf*t) * cnd(-d1))
        return result
        
    # Greeks implementations for equity and fx options
    