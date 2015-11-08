import unittest
from options.binary.src.gap_option import GapOption


class GapOptionTest(unittest.TestCase):
    def setUp(self):
        self.call_option = GapOption('call', 50.0, 50.0, 57.0, 0.09, 0.09, 0.5, 0.2)

    def test_call_option(self):
        self.assertEqual(round(self.call_option.get_value(), 4), 20.2069)

    def test_put_option(self):
        pass


if __name__ == '__main__':
    unittest.main()