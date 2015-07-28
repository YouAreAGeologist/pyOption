# Standard Barrier Option pricing

class StanadardBarrierOption:
    
    def __init__(self,flag,barrierType,s,x,r,b,t,sigma):
        self.flag = flag
        self.barrierType = barrierType
        self.s = s
        self.x = x
        self.r = r
        self.t = t
        self.sigma = sigma
        self.mu = (b - math.pow(sigma,2)/2)/math.pow(sigma)
        self.lmd = math.sqrt(math.pow(mu,2) + (2 * r / math.pow(sigma,2)))
        self.x1 = math.log(s/x)/(sigma * math.sqrt(t)) + ((1 + mu) * sigma * t)
        self.x2 = math.log(s/h)/(sigma * math.sqrt(t)) + ((1 + mu) * sigma * t)
        self.y1 = math.log(math.pow(h,2)/(s * x))/(sigma * math.sqrt(t)) + ((1 + mu) * sigma * math.sqrt(t))
        self.y2 = math.log(h/s)/(sigma * math.sqrt(t)) + ((1 + mu) * sigma * math.sqrt(t))
        self.z = (math.log(h/s)/(sigma * math.sqrt(t))) + (lmd * sigma * math.sqrt(t))
        self.eta = None
        self.phi = None
    
    # Standard barrier option price
    def get_price():
        result = None
        
        # document all barrier types up and in call etc
        #
        
        if barrierType == "in":
            if flag == 'c':
                if s > h:
                    phi = 1
                    eta = 1
                    if x > h:
                        result = __c() + __e()
                    elif x < h:
                        result = __a() - __b() + __d() + __e()
                elif s < h:
                    phi = -1
                    eta = 1
                    if x > h:
                        result = __a() + __e()
                    elif x < h:
                        result = __b() - __c() + __d() + __e()
            elif flag == 'p':
                if s > h:
                    phi = 1
                    eta = -1
                    if x > h:
                        result = __b() - __c() + __d() + __e() 
                    elif x < h:
                        result = __a() + __e()
                elif s < h:
                    phi = -1
                    eta = -1
                    if x > h:
                        result = __a() - __b() + __d() + __e()
                    elif x < h:
                        result = __c() + __e()
        elif barrierType == "out":
            if flag == 'c':
                if s > h:
                    phi = 1
                    eta = 1
                    if x > h:
                        result = __a() - __c() + __f()
                    elif x < h:
                        result = __b() - __d() + __f()
                elif s < h:
                    phi = -1
                    eta = 1
                    if x > h:
                        result = __f()
                    elif x < h:
                        result = __a() - __b() + __c() - __d() + __f()
            elif flag == 'p':
                if s > h:
                    phi = 1
                    eta = -1
                    if x > h:
                        result = __a() - __b() + __c() - __d() + __f()
                    elif x < h:
                        result = __f()
                elif s < h:
                    phi = -1
                    eta = -1
                    if x > h:
                        result = __b() - __d() + __f()
                    elif x < h:
                        result = __a() - __c() + __f()
        return result
        
    def __a():
        return (phi * s * math.exp((b-r)*t) * cnd(phi * x1)) - (phi * x * math.exp(-r*t))
        
    def __b():
        return 0
        
    def __c():
        return 0
        
    def __d():
        return 0
        
    def __e():
        return 0
        
    def __f():
        return 0
    
        