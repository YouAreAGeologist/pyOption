import unittest
from options.exotic.src.standard_power_option import StandardPowerOption


class StandardPowerOptionTest(unittest.TestCase):
    def setUp(self):
        self.call_option = StandardPowerOption('call', 10.0, 100.0, 1.90, 0.08, 0.02, 0.5, 0.1)
        self.put_option = StandardPowerOption('put', 10.0, 100.0, 1.90, 0.08, 0.02, 0.5, 0.1)

    def test_call_option(self):
        self.assertEqual(round(self.call_option.get_value(), 4), 0.3102)

    def test_put_option(self):
        self.assertEqual(round(self.put_option.get_value(), 4), 18.2738)


if __name__ == '__main__':
    unittest.main()