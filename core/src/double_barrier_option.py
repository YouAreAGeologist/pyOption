import math

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
        
    def get_price(self):
        result = None
        mu1 = ((2 * (b - delta2 - (n * (delta1 - delta2))))/math.pow(sigma,2)) + 1
        mu2 = 2 * n * (delta1 - delta2)/math.pow(sigma,2)
        mu3 = ((2 * (b - delta2 + (n * (delta1 - delta2))))/math.pow(sigma,2)) + 1
        sum1 = 0
        sum2 = 0
        
        if flag == 'c':
            f = u * math.exp(delta1 * t)
            d1 = (math.log(s * math.pow(u,2*n) / (x * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d2 = (math.log(s * math.pow(u,2*n) / (f * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d3 = (math.pow(l,2*n + 2) / (x * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            d4 = (math.pow(l,2*n + 2) / (f * s * math.pow(l,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            
            # Approximate infinite series conversion using -5 to +5
            for n in range(-5,5):
                sum1 += (math.pow(math.pow(u,n)/math.pow(l,n),mu1) * math.pow(l/s,mu2) * ((cnd(d1)-cnd(d2)) - math.pow(math.pow(l,n+1)/(math.pow(u,n) * s),mu3) * (cnd(d3) - cnd(d4)))) 
                sum2 += (math.pow(math.pow(u,n)/math.pow(l,n),mu1 - 2) * math.pow(l/s,mu2) * ((cnd(d1 - sigma * math.sqrt(t))-cnd(d2 - sigma * math.sqrt(t))) - math.pow(math.pow(l,n+1)/(math.pow(u,n) * s),mu3) * (cnd(d3 - sigma * math.sqrt(t)) - cnd(d4 - sigma * math.sqrt(t)))))
            
            sum1 = sum1 * s * math.exp((b-r)*t)
            sum2 = sum2 * x * math.exp(r*t)
            
        elif flag == 'p':
            e = l * math.exp(delta2 * t)
            y1 = (math.log(s * math.pow(u,2*n) / (e * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y2 = (math.log(s * math.pow(u,2*n) / (x * math.pow(l,2*n))) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y3 = (math.pow(l,2*n + 2) / (e * s * math.pow(u,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            y4 = (math.pow(l,2*n + 2) / (x * s * math.pow(u,2*n)) + ((b + math.sqrt(sigma,2)/2) * t))/(sigma * math.sqrt(t))
            
            # Approximate infinite series conversion using -5 to +5
            for n in range(-5,5):
                sum1 += (math.pow(math.pow(u,n)/math.pow(l,n),mu1 - 2) * math.pow(l/s,mu2) * ((cnd(y1 - sigma * math.sqrt(t))-cnd(y2 - sigma * math.sqrt(t))) - math.pow(math.pow(l,n+1)/(math.pow(u,n) * s),mu3 - 2) * (cnd(y3 - sigma * math.sqrt(t)) - cnd(y4 - sigma * math.sqrt(t))))) 
                sum2 += (math.pow(math.pow(u,n)/math.pow(l,n),mu1) * math.pow(l/s,mu2) * ((cnd(y1)-cnd(y2) - math.pow(math.pow(l,n+1)/(math.pow(u,n) * s),mu3) * (cnd(y3) - cnd(y4))))
        
            sum1 = sum1 * x * math.exp(r*t)
            sum2 = sum2 * s * math.exp((b-r)*t)
        
        return sum1 + sum2