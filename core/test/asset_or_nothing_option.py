import unittest
from core.src.asset_or_nothing_option import AssetOrNothingOption


class AssetOrNothingOptionTest(unittest.TestCase):


    def test_get_put_price(self):
        option = AssetOrNothingOption('p', 70, 65, 0.07, 0.02, 0.5, 0.27)
        self.assertEqual(round(option.get_price(), 4), 20.2069)
