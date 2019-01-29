import unittest

from casino.simulator.integerstatistics import IntegerStatistics


class IntegerStatisticsTest(unittest.TestCase):
    """Test the implementation of the class IntegerStatistics."""

    def setUp(self):
        self.test_small_data = IntegerStatistics([1, 2, 3])
        self.test_data = IntegerStatistics(
            [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])

    def test_mean_is_correct(self):
        self.assertEqual(self.test_small_data.mean(), 2)
        self.assertEqual(self.test_data.mean(), 9)

    def test_standard_deviation_is_correct(self):
        self.assertEqual(self.test_small_data.stdev(), 1)
        self.assertEqual(self.test_data.stdev(), 3.31662)


if __name__ == '__main__':
    unittest.main()
