# Pricing and greeks of vanilla options

import math
import Distributions

class VanillaEuropeanOption:
    
    def __init__(self,flag,s,x,r,t,sigma):
        self.flag = flag
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
     
    # Delta greeks   
    def get_delta():
        result = None
        return result
        
    def get_ddelta_dvol():
        result = None
        return result
        
    def get_ddelta_dtime():
        result = None
        return result
        
    def get_charm():
        result = None
        return result
    
    def get_elasticity():
        result = None
        return result
    
    # Gamma greeks 
    def get_gamma():
        result = None
        return result
        
    def get_dgamma_dvol():
        result = None
        return result
        
    def get_zomma():
        result = None
        return result
        
    def get_dgamma_dspot():
        result = None
        return result
        
    def get_speed():
        result = None
        return result
        
    def get_dgamma_dtime():
        result = None
        return result
        
    def get_color():
        result = None
        return result
    
    # Vega greeks  
    def get_vega():
        result = None
        return result
        
    def get_vegap():
        result = None
        return result
        
    def get_vega_leverage():
        result = None
        return result
        
    def get_vega_elasticity():
        result = None
        return result
        
    def get_dvega_dvol():
        result = None
        return result
        
    def get_vomma():
        result = None
        return result
        
    def get_dvomma_dvol():
        result = None
        return result
        
    def get_dvega_dtime():
        result = None
        return result
        
    # Variance greeks
    def get_variance_vega():
        result = None
        return result
        
    def get_ddelta_dvar():
        result = None
        return result
    
    # Theta greeks
    def get_theta():
        result = None
        return result 
    
    # Rho greeks
    def get_rho():
        result = None
        return result
        
    # Probability greeks
    def get_in_the_money_probability():
        result = None
        return result
        
    def get_dzeta_dvol():
        result = None
        return result
        
    def get_dzeta_dtime():
        result = None
        return result
        
    def get_probability_of_ever_getting_in_the_money():
        result = None
        return
        