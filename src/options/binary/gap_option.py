from src.options.option_base import OptionBase

** Build option class inheritance trees i.e. OptionBase -> BinaryOptionBase -> GapOption


class GapOption(OptionBase):
    def __init__(self, flag, s, x, r, b, t, sigma):
        super(GapOption, self).__init__()

    def get_value(self):
        result=None
        return result

