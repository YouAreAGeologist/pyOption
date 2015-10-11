from options.bases.src.option_base import OptionBase


class BinaryDoubleBarrierOption(OptionBase):
    def __init__(self, flag, s, x, r, b, t, sigma):
        super(BinaryDoubleBarrierOption, self).__init__()
        self.flag = flag
        self.s = s
        self.x = x
        self.r = r
        self.b = b
        self.t = t
        self.sigma = sigma

    def get_value(self):
        result=None
        return result
