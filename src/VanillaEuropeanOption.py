# Pricing and greeks of vanilla options

import math
import Distributions

class VanillaEuropeanOption:
    
    def __init__(self,flag,s,x,r,b,t,sigma):
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.t = t
        self.sigma = sigma
        self.d1 = (math.log(s/x) + (r - b + math.pow(sigma,2)/2) * t)/(sigma * math.sqrt(t))
        self.d2 = d1 - sigma * math.sqrt(t)
    
    # Option price  
    def get_price():
        result = None
        if flag == 'c':
            result = (s * math.exp(-b*T) * cnd(d1)) - (x * math.exp(-r * t) * cnd(d2))
        elif flag == 'p':
            result = (x * math.exp(-r * t) * cnd(-d2)) - (s * math.exp(-q*t) * cnd(-d1))
        return result
     
    # Delta greeks  
    #
    
    # Delta, spot delta
    def get_delta():
        result = None
        if flag == 'c':
            result = math.exp((b-r)*t) * cnd(d1)
        elif flag == 'p':
            result = math.exp((b-r)*t) * (cnd(d1) - 1)
        return result
    
    # DdeltaDvol, vanna
    def get_ddelta_dvol():
        return (-math.exp((b-r)*t) * d2 * ndf(d1))/sigma
        
    def get_ddelta_dtime():
        result = None
        return result
        
    def get_charm():
        result = None
        return result
    
    def get_elasticity():
        result = None
        if flag == 'c':
            result = math.exp((b-r)*t) * cnd(d1) * s / get_price()
        elif flag == 'p':
            result = math.exp((b-r)*t) * (cnd(d1) - 1) * s / get_price()
        return result
    
    # Gamma greeks 
    #
    
    # Gamma
    def get_gamma():
        return ndf(d1) * math.exp((b-r)*t)/(s * sigma * math.sqrt(t))
        
    # Maximal gamma for asset price
    def get_maximal_gamma_for_asset_price():
        return x * (math.exp(-b - 3 * math.pow(sigma,2)/2) * t)
    
    # Maximal gamma for strike price
    def get_maximal_gamma_for_strike_price():
        return s * math.exp((b + math.pow(sigma,2)/2) * t)
        
    # Gamma percentage
    def get_gammaP():
        return ndf(d1) * math.exp((b-r)*t)/(100 * sigma * math.sqrt(t))
      
    # DgammaDvol, zomma  
    def get_dgamma_dvol():
        return get_gamma() * (d1 * d2 - 1)/sigma
    
    # DgammaDspot, speed  
    def get_dgamma_dspot():
        return -get_gamma() * (1 + (d1/(sigma*math.sqrt(t))))/s 
    
    # DgammaDtime, color    
    def get_dgamma_dtime():
        result = None
        return result
    
    # Vega greeks  
    def get_vega():
        return s * math.exp((b-r)*t) * ndf(d1) * math.exp(t)
    
    # VegaP for 10% change in volatility    
    def get_vegap():
        return (sigma * s * math.exp((b-r)*t) * ndf(d1) * math.sqrt(t))/10
     
    # Vega leverage, elasticity   
    def get_vega_leverage():
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
        
