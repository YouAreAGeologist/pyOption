import math


# Cumulative bivariate normal density function
    # Drezner (1978) approximation
    # @staticmethod
    # def cbnd(self,a,b,rho):
    #     result = None
    #
    #     if a <= 0 and b <= 0 and rho <= 0:
    #         result = self.__M(a,b,rho)
    #     elif a <= 0 and b >= 0 and rho >= 0:
    #         result = self.cnd(a) - self.__M(a,-b,-rho)
    #     elif a >= 0 and b <= 0 and rho >= 0:
    #         result = self.cnd(a) - self.__M(-a,b,-rho)
    #     elif a >= 0 and b >= 0 and rho <= 0:
    #         result = self.cnd(a) + self.cnd(b) - 1 + self.__M(-a,-b,rho)
    #     elif a * b * rho > 0:
    #         rho1 = ((rho * a - b) * mathematics.copysign(1, a)) / (mathematics.sqrt(mathematics.pow(a,2) + (2 * rho * a * b) + mathematics.pow(b,2)))
    #         rho2 = ((rho * b - a) * mathematics.copysign(1, b)) / (mathematics.sqrt(mathematics.pow(a,2) + (2 * rho * a * b) + mathematics.pow(b,2)))
    #         delta = (1 - mathematics.copysign(1,a) * mathematics.copysign(1,b))
    #         result = self._M(a,0,rho1) + self._M(b,0,rho2) - delta
    #     return result

    # Loop statement for cbnd
    # @staticmethod
    # def __M(a,b,rho):
    #
    #     result = None
    #     a1 = a / mathematics.sqrt(2 * (1 - mathematics.pow(rho,2)))
    #     b1 = b / mathematics.sqrt(2 * (1 - mathematics.pow(rho,2)))
    #     x = [0.24840615,0.39233107,0.21141819,0.033246660,0.00082485334]
    #     y = [0.10024215,0.48281397,1.0609498,1.7797294,2.6697604]
    #
    #     for i in range(0,4):
    #         for j in range(0,4):
    #             result += mathematics.exp((a1 * (2*y[i] - a1)) + (b1 * (2*y[j] - b1) + (2 * rho * (y[i] - a1) * (y[j] - b1))))
    #     return result
