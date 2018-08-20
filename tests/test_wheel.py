import unittest

from casino.roulette.bin import Bin
from casino.roulette.outcome import Outcome
from casino.roulette.wheel import Wheel

EXPECTED_SPINS = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]


class WheelTest(unittest.TestCase):
    """Test the implementation of the class Wheel."""

    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Even", 1)
        self.oc3 = Outcome("Split 1-2", 17)
        self.test_wheel = Wheel()
        self.test_wheel.rng.seed(1)

    def test_can_create_wheel(self):
        self.assertIsNotNone(self.test_wheel)

    def test_wheel_contains_38_bins(self):
        expected_bins = 38
        self.assertEqual(expected_bins, len(self.test_wheel.bins))
        self.assertIsInstance(self.test_wheel.bins[0], Bin)

    def test_get_returns_correct_bin(self):
        self.assertEqual(self.test_wheel.get_bin(1), self.test_wheel.bins[1])

    def test_can_add_outcomes_to_wheel_bins(self):
        self.test_wheel.add_outcome(1, self.oc1)
        self.assertTrue(self.oc1 in self.test_wheel.get_bin(1))

    def test_wheel_returns_expected_bins(self):
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[8])
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[36])
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[4])


if __name__ == '__main__':
    unittest.main()
