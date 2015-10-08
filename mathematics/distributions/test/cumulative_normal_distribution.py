import unittest
from mathematics.distributions.src.cumulative_normal_distribution import N


class CumulativeNormalDistributionTest(unittest.TestCase):
    def test_values(self):
        self.assertEqual(round(N(10.0), 4), 1.0)
        self.assertEqual(round(N(-10.0), 4), 0.0)
        self.assertEqual(round(N(0), 4), 0.5)
        self.assertEqual(round(N(1), 4), 0.8413)
        self.assertEqual(round(N(-1), 4), 0.1587)

if __name__ == '__main__':
    unittest.main()
