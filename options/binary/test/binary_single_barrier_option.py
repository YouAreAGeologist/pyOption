import unittest
from options.binary.src.binary_single_barrier_option import BinarySingleBarrierOption


class BinarySingleBarrierOptionTest(unittest.TestCase):
    def setUp(self):

        #1
        self.down_and_in_cash_at_hit_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_cash_at_hit_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_in_cash_at_hit_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_cash_at_hit_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #2
        self.up_and_in_cash_at_hit_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_cash_at_hit_or_nothing', 95.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_in_cash_at_hit_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_cash_at_hit_or_nothing', 95.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #3
        self.down_and_in_asset_at_hit_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_asset_at_hit_or_nothing', 105.0, 102.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_in_asset_at_hit_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_asset_at_hit_or_nothing', 105.0, 98.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #4
        self.up_and_in_asset_at_hit_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_asset_at_hit_or_nothing', 95.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_in_asset_at_hit_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_asset_at_hit_or_nothing', 95.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #5
        self.down_and_in_cash_at_expiration_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_cash_at_expiration_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_in_cash_at_expiration_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_cash_at_expiration_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #6
        self.up_and_in_cash_at_expiration_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_cash_at_expiration_or_nothing', 95.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_in_cash_at_expiration_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_cash_at_expiration_or_nothing', 95.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #7
        self.down_and_in_asset_at_expiration_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_asset_at_expiration_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_in_asset_at_expiration_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_asset_at_expiration_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #8
        self.up_and_in_asset_at_expiration_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_asset_at_expiration_or_nothing', 95.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_in_asset_at_expiration_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_asset_at_expiration_or_nothing', 95.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #9
        self.down_and_out_cash_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_asset_at_expiration_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_out_cash_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_asset_at_expiration_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #10
        self.down_and_out_asset_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_asset_at_expiration_or_nothing', 95.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_out_asset_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_asset_at_expiration_or_nothing', 95.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #11
        self.down_and_out_asset_or_nothing_option_102 = BinarySingleBarrierOption('down_and_out_asset_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_out_asset_or_nothing_option_98 = BinarySingleBarrierOption('down_and_out_asset_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #12
        self.up_and_out_asset_or_nothing_option_102 = BinarySingleBarrierOption('up_and_out_asset_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_out_asset_or_nothing_option_98 = BinarySingleBarrierOption('up_and_out_asset_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #13
        self.down_and_in_cash_or_nothing_option_102 = BinarySingleBarrierOption('down_and_in_cash_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.down_and_in_cash_or_nothing_option_98 = BinarySingleBarrierOption('down_and_in_cash_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #14
        self.up_and_in_cash_or_nothing_option_102 = BinarySingleBarrierOption('up_and_in_cash_or_nothing', 105.0, 102.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)
        self.up_and_in_cash_or_nothing_option_98 = BinarySingleBarrierOption('up_and_in_cash_or_nothing', 105.0, 98.0, 15.0, 100.0, 0.1, 0.1, 0.5, 0.2)

        #15

        #16

        #17

        #18

        #19

        #20

        #21

        #22

        #23

        #24

        #25

        #26

        #27

        #28

    #1
    def test_down_and_in_cash_at_hit_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_cash_at_hit_or_nothing_option_102.get_value(), 4), 9.7264)
        self.assertEqual(round(self.down_and_in_cash_at_hit_or_nothing_option_98.get_value(), 4), 9.7264)

    #2
    def test_up_and_in_cash_at_hit_or_nothing_option(self):
        self.assertEqual(round(self.up_and_in_cash_at_hit_or_nothing_option_102.get_value(), 4), 11.6553)
        self.assertEqual(round(self.up_and_in_cash_at_hit_or_nothing_option_98.get_value(), 4), 11.6553)

    #3
    def test_down_and_in_asset_at_hit_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_asset_at_hit_or_nothing_option_102.get_value(), 4), 68.0848)
        self.assertEqual(round(self.down_and_in_asset_at_hit_or_nothing_option_98.get_value(), 4), 68.0848)

    #4
    def test_up_and_in_asset_at_hit_or_nothing_option(self):
        self.assertEqual(round(self.up_and_in_asset_at_hit_or_nothing_option_102.get_value(), 4), 11.6553)
        self.assertEqual(round(self.up_and_in_asset_at_hit_or_nothing_option_98.get_value(), 4), 11.6553)

    #5
    def test_down_and_in_cash_at_expiration_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_cash_at_expiration_or_nothing_option_102.get_value(), 4), 9.3604)
        self.assertEqual(round(self.down_and_in_cash_at_expiration_or_nothing_option_98.get_value(), 4), 9.3604)

    #6
    def test_up_and_in_cash_at_expiration_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_cash_at_expiration_or_nothing_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_cash_at_expiration_or_nothing_option_98.get_value(), 4), 11.2223)

    #7
    def test_down_and_in_asset_at_expiration_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_asset_at_expiration_or_nothing_option_102.get_value(), 4), 9.3604)
        self.assertEqual(round(self.down_and_in_asset_at_expiration_or_nothing_option_98.get_value(), 4), 9.3604)

    #8
    def test_up_and_in_asset_at_expiration_or_nothing_option(self):
        self.assertEqual(round(self.down_and_in_asset_at_expiration_or_nothing_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_asset_at_expiration_or_nothing_option_98.get_value(), 4), 11.2223)

    #9
    def test_down_and_out_cash_or_nothing_option(self):
        self.assertEqual(round(self.down_and_out_cash_or_nothing_option_102.get_value(), 4), 9.3604)
        self.assertEqual(round(self.down_and_out_cash_or_nothing_option_98.get_value(), 4), 9.3604)

    #10
    def test_up_and_out_cash_or_nothing_option(self):
        self.assertEqual(round(self.up_and_out_cash_or_nothing_option_102.get_value(), 4), 9.3604)
        self.assertEqual(round(self.up_and_out_cash_or_nothing_option_98.get_value(), 4), 9.3604)

    #11
    def test_down_and_out_asset_or_nothing_option(self):
        self.assertEqual(round(self.down_and_out_asset_or_nothing_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_asset_or_nothing_option_98.get_value(), 4), 11.2223)

    #12
    def test_up_and_out_asset_or_nothing_option(self):
        self.assertEqual(round(self.down_and_out_asset_or_nothing_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_asset_or_nothing_option_98.get_value(), 4), 11.2223)

    #13
    def test_down_and_in_cash_or_nothing_call_option(self):
        self.assertEqual(round(self.down_and_in_cash_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_cash_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #14
    def test_up_and_in_cash_or_nothing_call_option(self):
        self.assertEqual(round(self.up_and_in_cash_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_in_cash_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #15
    def test_down_and_in_asset_or_nothing_call_option(self):
        self.assertEqual(round(self.down_and_in_asset_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_asset_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #16
    def test_up_and_in_asset_or_nothing_call_option(self):
        self.assertEqual(round(self.up_and_in_asset_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_in_asset_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #17
    def test_down_and_in_cash_or_nothing_put_option(self):
        self.assertEqual(round(self.down_and_in_cash_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_cash_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #18
    def test_up_and_in_cash_or_nothing_put_option(self):
        self.assertEqual(round(self.up_and_in_cash_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_in_cash_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #19
    def test_down_and_in_asset_or_nothing_put_option(self):
        self.assertEqual(round(self.down_and_in_asset_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_in_asset_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #20
    def test_up_and_in_asset_or_nothing_put_option(self):
        self.assertEqual(round(self.up_and_in_asset_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_in_asset_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #21
    def test_down_and_out_cash_or_nothing_call_option(self):
        self.assertEqual(round(self.down_and_out_cash_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_cash_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #22
    def test_up_and_out_cash_or_nothing_call_option(self):
        self.assertEqual(round(self.up_and_out_cash_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_out_cash_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #23
    def test_down_and_out_asset_or_nothing_call_option(self):
        self.assertEqual(round(self.down_and_out_asset_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_asset_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #24
    def test_up_and_out_asset_or_nothing_call_option(self):
        self.assertEqual(round(self.up_and_out_asset_or_nothing_call_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_out_asset_or_nothing_call_option_98.get_value(), 4), 11.2223)

    #25
    def test_down_and_out_cash_or_nothing_put_option(self):
        self.assertEqual(round(self.down_and_out_cash_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_cash_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #26
    def test_up_and_out_cash_or_nothing_put_option(self):
        self.assertEqual(round(self.up_and_out_cash_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_out_cash_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #27
    def test_down_and_out_asset_or_nothing_put_option(self):
        self.assertEqual(round(self.down_and_out_asset_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.down_and_out_asset_or_nothing_put_option_98.get_value(), 4), 11.2223)

    #28
    def test_up_and_out_asset_or_nothing_put_option(self):
        self.assertEqual(round(self.up_and_out_asset_or_nothing_put_option_102.get_value(), 4), 11.2223)
        self.assertEqual(round(self.up_and_out_asset_or_nothing_put_option_98.get_value(), 4), 11.2223)

if __name__ == '__main__':
    unittest.main()
