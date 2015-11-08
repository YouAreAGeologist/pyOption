import unittest
from options.binary.src.cash_or_nothing_option import CashOrNothingOption


class CashOrNothingOptionTest(unittest.TestCase):
    def setUp(self):
        self.put_option = CashOrNothingOption('put', 100.0, 80.0, 10.0, 0.06, 0.0, 0.75, 0.35)

    def test_call_option(self):
        pass

    def test_put_option(self):
        self.assertEqual(round(self.put_option.get_value(), 4), 2.6710)


if __name__ == '__main__':
    unittest.main()