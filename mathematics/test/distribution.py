import unittest
import math
from mathematics.src.distribution import *

class Distribution(unittest.TestCase):

    def test_ndf(self):
        self.assertEqual(round(ndf(0.2387), 4), 0.3877)
        self.assertEqual(round(ndf(1.3446), 4), 0.1616)
        self.assertEqual(round(ndf(0.0837), 4), 0.3975)

    def test_cnd(self):
        self.assertEqual(round(cnd(0), 4), 0.5000)
        self.assertEqual(round(cnd(-1.0), 4), 0.1587)
        self.assertEqual(round(cnd(1.0), 4), 0.8413)

