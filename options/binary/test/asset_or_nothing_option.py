import unittest
from options.binary.src.asset_or_nothing_option import AssetOrNothingOption


class AssetOrNothingOptionTest(unittest.TestCase):
    def setUp(self):
        self.put_option = AssetOrNothingOption('put', 70.0, 65.0, 0.07, 0.02, 0.5, 0.27)

    def test_call_option(self):
        pass

    def test_put_option(self):
        self.assertEqual(round(self.put_option.get_value(), 4), 20.2069)


if __name__ == '__main__':
    unittest.main()