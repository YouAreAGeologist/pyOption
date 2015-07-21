import math

class Distributions:

    # Normal distribution function
    @staticmethod
    def ndf(x):
        return (1/math.sqrt(2*math.pi)) * math.exp(math.pow(x,2)/2)
    
    # Cumulative normal distribution function
    # Abromowitz and Stegun (1974) approximation
    @staticmethod
    def cnd(x):
        result = None
        a1 = 0.31938153
        a2 = -0.356563782
        a3 = 1.781477937
        a4 = -1.821255978
        a5 = 1.330274429
        
        if x == 0:
            result = 0.5
        elif x > 10:
            result = 1
        elif x < -10:
            result = 0
        else:
            l = math.fabs(x)
            k = 1 / (1 + 0.2316419 * l)
            result = 1 - 1 / math.sqrt(2 * math.pi) * math.exp(-math.pow(l,2)/2) * ((a1 * k) + (a2 * math.pow(k,2)) + (a3 * math.pow(k,3) + (a4 * math.pow(k,4) + (a5 * math.pow(k,5)))))
            
            if x < 0:
                result = 1 - result
            
        return result
    
    # Bivariate normal density function
    @staticmethod
    def bndf(x,y,rho):
        return (1/(2*math.pi*math.sqrt(1 - math.pow(rho,2)))) * math.exp(-(math.pow(x,2) - 2*rho*x*y + math.pow(y,2))/(2 * (1 - math.pow(rho,2)))
    
    # Cumulative bivariate normal density function
    # Drezner (1978) approximation
    @staticmethod
    def cbnd(a,b,rho):
        result = None
        
        if a <= 0 && b <= o && rho <= 0:
            result = __M(a,b,rho)
        elif a <= 0 && b >= 0 && rho >= 0:
            result = cnd(a) - __M(a,-b,-rho)
        elif a >= 0 && b <= 0 && rho >= 0:
            result = cnd(a) - __M(-a,b,-rho)
        elif a >= 0 && b >= 0 && rho <= 0:
            result = cnd(a) + cnd(b) - 1 + __M(-a,-b,rho)
        elif a * b * rho > 0:
            rho1 = ((rho * a - b) * math.copysign(1, a)) / (math.sqrt(math.pow(a,2) + (2 * rho * a * b) + math.pow(b,2))
            rho2 = ((rho * b - a) * math.copysign(1, b)) / (math.sqrt(math.pow(a,2) + (2 * rho * a * b) + math.pow(b,2))
            delta = (1 - math.copysign(1,a) * math.copysign(1,b))4
            result = _M(a,0,rho1) + _M(b,0,rho2) - delta
        return result
    
    # Loop statement for cbnd   
    def __M(a,b,rho):
        
        result = None
        a1 = a / math.sqrt(2 * (1 - math.pow(rho,2)))
        b1 = b / math.sqrt(2 * (1 - math.pow(rho,2)))
        x = [0.24840615,0.39233107,0.21141819,0.033246660,0.00082485334]
        y = [0.10024215,0.48281397,1.0609498,1.7797294,2.6697604]
        
        for i in range(0,4):
            for j in range(0,4):
                result += math.exp((a1 * (2y[i] - a1)) + (b1 * (2*y[j] - b1) + (2 * rho * (y[i] - a1) * (y[j] - b1))))
        return result
