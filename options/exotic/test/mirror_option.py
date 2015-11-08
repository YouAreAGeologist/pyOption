import unittest
from options.exotic.src.mirror_option import MirrorOption


class FadeInOptionTest(unittest.TestCase):
    def setUp(self):
        self.s = 100.0
        self.t = 0.5
        self.r = 0.1
        self.b = 0.0

    def test_long_call_option(self):
        self.assertEqual(round(MirrorOption('call', 'long', self.s, 95.0, self.r, self.b, self.t, 2.0).get_value(), 4), 15.1251)

    def test_long_put_option(self):
        self.assertEqual(round(MirrorOption('put', 'long', self.s, 95.0, self.r, self.b, self.t, 0.2).get_value(), 4), 3.2476)

    def test_short_call_option(self):
        self.assertEqual(round(MirrorOption('call', 'short', self.s, 95.0, self.r, self.b, self.t, 2.0).get_value(), 4), -12.2959)

    def test_short_put_option(self):
        self.assertEqual(round(MirrorOption('put', 'short', self.s, 95.0, self.r, self.b, self.t, 0.2).get_value(), 4), -2.3841)


if __name__ == '__main__':
    unittest.main()