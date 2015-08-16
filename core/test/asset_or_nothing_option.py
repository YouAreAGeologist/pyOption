import unittest
import math
from core.src.asset_or_nothing_option import AssetOrNothingOption


class AssetOrNothingOptionTest(unittest.TestCase):


    def test_get_put_price(self):
        option = AssetOrNothingOption('p', 100, 80, 10, 0.06, 0, 0.75, 0.35)
        self.assertEqual(round(option.get_price(), 4), 2.6710)