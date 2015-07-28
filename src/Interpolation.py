# Interpolation functions

class Interpolation:
    
    @staticmethod
    def get_linear_interpolation(x1,x2,xi,y1,y2):
        return (y2 - y1) * ((xi - x1)/(x2 - x1)) + y1
    
    @staticmethod
    def get_log_linear_interpolation(x1,x2,xi,y1,y2):
        return math.pow(y2/y1, (xi - x1)/(x2 - x1)) * y1
        
    @staticmethod
    def get_exponential_interpolation():
        return math.pow(y1, (xi/x1) * (x2-xi)/(x2-x1)) * math.pow(y2, (xi/x2) * (xi-x1)/(x2-x1))
        
    @staticmethod
    def get_cubic_lagrange_interpolation(x1,x2,x3,x4,xi,y1,y2,y3,y4):
        a = ((xi-x2)*(xi-x3)*(xi-x4))/((x1-x2)*(x1-x3)*(x1-x4))
        b = ((xi-x1)*(xi-x3)*(xi-x4))/((x2-x1)*(x2-x3)*(x2-x4))
        c = ((xi-x1)*(xi-x2)*(xi-x4))/((x3-x1)*(x3-x2)*(x3-x4))
        d = ((xi-x1)*(xi-x2)*(xi-x3))/((x4-x1)*(x4-x2)*(x4-x3))
        return (a * y1) + (b * y2) + (c * y3) + (d * y4)