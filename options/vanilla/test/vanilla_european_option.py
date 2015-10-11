import unittest
from options.vanilla.src.vanilla_european_option import VanillaEuropeanOption


class VanillaEuropeanOptionTest(unittest.TestCase):
    def setUp(self):
        self.call_option = VanillaEuropeanOption('call', 60.0, 65.0, 0.08, 0.0, 0.25, 0.3)
        self.put_option = VanillaEuropeanOption('put', 100.0, 95.0, 0.1, 0.05, 0.5, 0.2)

    def test_call_option(self):
        self.assertEqual(round(self.call_option.get_value(), 4), 2.1334)

    def test_put_option(self):
        self.assertEqual(round(self.put_option.get_value(), 4), 2.4648)


if __name__ == '__main__':
    unittest.main()
