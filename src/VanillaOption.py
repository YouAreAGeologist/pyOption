# Pricing and greeks of vanilla options

import math
import Distributions

class VanillaEuropeanOption:
    
    def __init__(self,s,x,r,t,sigma):
        self.s = s
        self.x = x
        self.r = r
        self.t = t
        self.sigma = sigma
        self.d1 = None
        self.d2 = None
        
        self.d1 = (math.log(s/x) + (r + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        self.d2 = d1 - sigma * math.sqrt(t)
        
    def get_price():
        result = None
        return result
        
    def get_delta():
        result = None
        return result
        
    def get_gamma():
        result = None
        return result 
        
    def get_theta():
        result = None
        return result 
        
    def get_vega():
        result = None
        return result
        
    def get_rho:
        result = None
        return result