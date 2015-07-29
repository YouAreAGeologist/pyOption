# Double barrier option pricing

class DoubleBarrierOption:
    
    def __init__(self,flag,s,x,u,l,t,r,b,sigma,delta1,delta2):
        self.s = s
        self.x = x
        self.u = u
        self.l = l
        self.t = t
        self.r = r
        self.b = b
        self.sigma = sigma
        self.delta1 = delta1
        self.delta2 = delta2
        
    def get_price():
        result = None
        mu1 = ((2 * (b - delta2 - (n * (delta1 - delta2))))/math.pow(sigma,2)) + 1
        mu2 = 2n * (delta1 - delta2)/math.pow(sigma,2)
        mu3 = ((2 * (b - delta2 + (n * (delta1 - delta2))))/math.pow(sigma,2)) + 1
        
        if flag == 'c':
            f = u * math.exp(delta1 * t)
            d1 = (math.log(s * math.pow(u,2*n) / (x * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d2 = (math.log(s * math.pow(u,2*n) / (f * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d3 = (math.pow(l,2*n + 2) / (x * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d4 = (math.pow(l,2*n + 2) / (f * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            
            # Approximate infinite series conversion using -5 to +5
            for n in range(-5,5):
                result += 0
            
            result = 0
            
        elif flag == 'p':
            e = l * math.exp(delta2 * t)
            y1 = (math.log(s * math.pow(u,2*n) / (e * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y2 = (math.log(s * math.pow(u,2*n) / (x * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y3 = (math.pow(l,2*n + 2) / (e * s * math.pow(u,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y4 = (math.pow(l,2*n + 2) / (x * s * math.pow(u,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            
            # Approximate infinite series conversion using -5 to +5
            for n in range(-5,5):
                result += 0
            
            result = 0
        
        return result