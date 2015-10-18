import unittest
from options.exotic.src.executive_stock_option import ExecutiveStockOption


class ExecutiveStockOptionTest(unittest.TestCase):
    def setUp(self):
        self.call_option = ExecutiveStockOption('put', 60.0, 64.0, 0.07, 0.04, 2.0, 0.15, 0.38)

    def test_call_option(self):
        self.assertEqual(round(self.call_option.get_value(), 4), 9.1244)

    def test_put_option(self):
        pass


if __name__ == '__main__':
    unittest.main()