import unittest
from core.src.gap_option import GapOption


class GapOptionTest(unittest.TestCase):


    def get_call_price(self):
        option = GapOption('c', 50, 50, 57, 0.09, 0.09, 0.5, 0.2)
        self.assertEqual(round(option.get_price(), 4), -0.0053)
