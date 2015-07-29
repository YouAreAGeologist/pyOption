# Double barrier option pricing

class DoubleBarrierOption:
    
    def __init__(self,flag,s,x,u,l,t,r,b,sigma):
        self.s = s
        self.x = x
        self.u = u
        self.l = l
        self.t = t
        self.r = r
        self.b = b
        self.sigma = sigma
        
        
        
    def get_price():
        result = None
        
        # Approximate infinite series conversion using -5 to +5
        
        if flag == 'c':
            
            # calculate F & E ??
            self.f = 0
            self.e = 0
            
            d1 = (math.log(s * math.pow(u,2*n) / (x * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d2 = (math.log(s * math.pow(u,2*n) / (f * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d3 = (math.pow(l,2*n + 2) / (x * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d4 = (math.pow(l,2*n + 2) / (f * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            
            result = 0
            
        elif flag == 'p':
            result = 0
        
        return result