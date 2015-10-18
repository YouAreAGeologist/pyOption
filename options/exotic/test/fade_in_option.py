import unittest
from options.exotic.src.fade_in_option import FadeInOption


class FadeInOptionTest(unittest.TestCase):
    def setUp(self):
        self.s = 100.0
        self.x = 100.0
        self.t = 0.5
        self.r = 0.1
        self.b = 0.0
        self.n = 183

    def test_call_option(self):
        self.assertEqual(round(FadeInOption('call', self.s, self.x, 95.0, 105.0, self.n, self.r, self.b, self.t, 0.1).get_value(), 4), 1.5427)

    def test_put_option(self):
        pass


if __name__ == '__main__':
    unittest.main()