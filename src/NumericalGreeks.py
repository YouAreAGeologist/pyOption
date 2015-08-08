# Greeks by finite difference approximations

class NumericalGreeks:
    
    @staticmethod
    def get_delta(price,price_lower,price_upper,ds):
        return (price_upper - price_lower)/(2 * ds)