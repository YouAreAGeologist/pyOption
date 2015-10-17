import unittest
from options.exotic.src.time_switch_option import TimeSwitchOption


class TimeSwitchOptionTest(unittest.TestCase):
    def setUp(self):
        self.call_option = TimeSwitchOption('call', 100.0, 110.0, 5.0, 0.06, 0.06, 1.0, 1/365.0, 0.26)

    def test_call_option(self):
        self.assertEqual(round(self.call_option.get_value(), 4), 1.3750)

    def test_put_option(self):
        pass


if __name__ == '__main__':
    unittest.main()