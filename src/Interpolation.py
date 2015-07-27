# Interpolation functions

class Interpolation:
    
    @staticmethod
    def get_linear_interpolation(x1,x2,xi,y1,y2):
        return (y2 - y1) * ((xi - x1)/(x2 - x1)) + y1
    
    @staticmethod
    def get_log_linear_interpolation(x1,x2,x1,y1,y2):
        return math.pow(y2/y1, (xi - x1)/(x2 - x1)) * y1
        
    @staticmethod
    def get_exponential_interpolation():
        return math.pow(y1, (xi/x1) * (x2-xi)/(x2-x1)) * math.pow(y2, (xi/x2) * (xi-x1)/(x2-x1))
        
    @staticmethod
    def get_cubic_interpolation():
        return 0
        
    @staticmethod
    def get_cubic_spline_interpolation():
        return 0
    
    @staticmethod
    def get_two_dimensional_interpolation():
        return 0