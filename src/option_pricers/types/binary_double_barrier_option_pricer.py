import math
from src.mathematics.distributions.cumulative_normal_distribution import N


class BinaryDoubleBarrierOptionPricer:
    def __init__(self, params):
        self.__params = params

    def get_price(self):
        pass