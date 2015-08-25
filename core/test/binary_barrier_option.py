import unittest
from core.src.binary_barrier_option import BinaryBarrierOption


class BinaryBarrierOptionTest(unittest.TestCase):


    def test_get_price(self):
        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-at-hit-or-nothing', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 9.7264)
        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-at-hit-or-nothing', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 9.7264)

        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-at-hit-or-nothing', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.6553)
        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-at-hit-or-nothing', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.6553)

        # self.assertEqual(round(BinaryBarrierOption('down-and-in asset-at-hit-or-nothing', 105.0, 102.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 68.0848)
        # self.assertEqual(round(BinaryBarrierOption('down-and-in asset-at-hit-or-nothing', 105.0, 98.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 68.0848)

        # self.assertEqual(round(BinaryBarrierOption('up-and-in asset-at-hit-or-nothing', 95.0, 102.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.6553)
        # self.assertEqual(round(BinaryBarrierOption('up-and-in asset-at-hit-or-nothing', 95.0, 98.0, 100.0, 100.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.6553)

        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-at-expiration-or-nothing', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 9.3604)
        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-at-expiration-or-nothing', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 9.3604)

        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-at-expiration-or-nothing', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.2223)
        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-at-expiration-or-nothing', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 11.2223)

        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-at-expiration-or-nothing', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 64.8426)
        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-at-expiration-or-nothing', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 64.8426)

        self.assertEqual(round(BinaryBarrierOption('up-and-in asset-at-expiration-or-nothing', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 77.7017)
        self.assertEqual(round(BinaryBarrierOption('up-and-in asset-at-expiration-or-nothing', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 77.7017)

        # self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4.9289)
        # self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4,9289)

        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.0461)
        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.0461)

        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-or-nothing call', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4.9289)
        # self.assertEqual(round(BinaryBarrierOption('down-and-in cash-or-nothing call', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 6.2150)

        # self.assertEqual(round(BinaryBarrierOption('up-and-in cash-or-nothing call', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 5.3710)
        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-or-nothing call', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 7.4519)

        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-or-nothing call', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 37.2782)
        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-or-nothing call', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 45.8530)

        self.assertEqual(round(BinaryBarrierOption('up-and-in asset-or-nothing call', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 44.5294)
        self.assertEqual(round(BinaryBarrierOption('up-and-in asset-or-nothing call', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 54.9262)

        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-or-nothing put', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4.4314)
        self.assertEqual(round(BinaryBarrierOption('down-and-in cash-or-nothing put', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.1454)

        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-or-nothing put', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 5.3297)
        self.assertEqual(round(BinaryBarrierOption('up-and-in cash-or-nothing put', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.7704)

        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-or-nothing put', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 27.5644)
        self.assertEqual(round(BinaryBarrierOption('down-and-in asset-or-nothing put', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 18.9896)

        # self.assertEqual(round(BinaryBarrierOption('up-and-in asset-or-nothing put', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 27.5644)
        # self.assertEqual(round(BinaryBarrierOption('up-and-in asset-or-nothing put', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 18.9896)

        self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing call', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4.8758)
        self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing call', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 4.9081)

        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing call', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0000)
        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing call', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0407)

        self.assertEqual(round(BinaryBarrierOption('down-and-out asset-or-nothing call', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 39.9391)
        self.assertEqual(round(BinaryBarrierOption('down-and-out asset-or-nothing call', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 40.1574)

        self.assertEqual(round(BinaryBarrierOption('up-and-out asset-or-nothing call', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0000)
        self.assertEqual(round(BinaryBarrierOption('up-and-out asset-or-nothing call', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.2676)

        self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing put', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0323)
        self.assertEqual(round(BinaryBarrierOption('down-and-out cash-or-nothing put', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0000)

        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing put', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.0461)
        self.assertEqual(round(BinaryBarrierOption('up-and-out cash-or-nothing put', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 3.0054)

        self.assertEqual(round(BinaryBarrierOption('down-and-out asset-or-nothing put', 105.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.2183)
        self.assertEqual(round(BinaryBarrierOption('down-and-out asset-or-nothing put', 105.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 0.0000)

        self.assertEqual(round(BinaryBarrierOption('up-and-out asset-or-nothing put', 95.0, 102.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 17.2983)
        self.assertEqual(round(BinaryBarrierOption('up-and-out asset-or-nothing put', 95.0, 98.0, 100.0, 15.0, 0.1, 0.1, 0.5, 0.2).get_price(), 4), 17.0306)