import unittest

from casino.roulette.bin import Bin
from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import RouletteGame as RoG
from casino.roulette.outcome import Outcome
from casino.roulette.wheel import Wheel

EXPECTED_SPINS = [8, 36, 4, 16, 7, 31, 28, 30, 24, 13]


class WheelTest(unittest.TestCase):
    """Test the implementation of the class Wheel."""

    def setUp(self):
        self.test_wheel = Wheel()
        self.test_wheel.rng.seed(1)
        BinBuilder().build_bins(self.test_wheel)

    def test_can_create_wheel(self):
        self.assertIsNotNone(self.test_wheel)

    def test_wheel_contains_38_bins(self):
        expected_bins = 38
        self.assertEqual(expected_bins, len(self.test_wheel.bins))
        self.assertIsInstance(self.test_wheel.bins[0], Bin)

    def test_get_returns_correct_bin(self):
        self.assertEqual(self.test_wheel.get_bin(1), self.test_wheel.bins[1])

    def test_wheel_returns_expected_bins(self):
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[8])
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[36])
        self.assertTrue(self.test_wheel.next() == self.test_wheel.bins[4])

    def test_zero_bin_outcomes(self):
        outcomes = [Outcome(RoG.five_bet_name, RoG.five_bet_odds),
                    Outcome(RoG.straight_bet_name + ' 0',
                            RoG.straight_bet_odds)]
        actual_bin = self.test_wheel.get_bin(0)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_bin_one_outcomes(self):
        outcomes = [
            Outcome(RoG.straight_bet_name + ' 1', RoG.straight_bet_odds),
            Outcome(RoG.red_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.odd_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.low_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.column_bet_name + " 1", RoG.column_bet_odds),
            Outcome(RoG.dozen_bet_name + " 1", RoG.dozen_bet_odds),
            Outcome(RoG.split_bet_name + " 1-2", RoG.split_bet_odds),
            Outcome(RoG.split_bet_name + " 1-4", RoG.split_bet_odds),
            Outcome(RoG.street_bet_name + " 1-2-3", RoG.street_bet_odds),
            Outcome(RoG.corner_bet_name + " 1-2-4-5", RoG.corner_bet_odds),
            Outcome(RoG.five_bet_name, RoG.five_bet_odds),
            Outcome(RoG.line_bet_name + " 1-2-3-4-5-6", RoG.line_bet_odds)
        ]
        actual_bin = self.test_wheel.get_bin(1)
        self.assertEqual(len(outcomes), len(actual_bin),
                         actual_bin)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_bin_twenty_outcomes(self):
        outcomes = [
            Outcome(RoG.straight_bet_name + ' 20', RoG.straight_bet_odds),
            Outcome(RoG.black_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.even_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.high_bet_name, RoG.even_money_bet_odds),
            Outcome(RoG.column_bet_name + " 2", RoG.column_bet_odds),
            Outcome(RoG.dozen_bet_name + " 2", RoG.dozen_bet_odds),
            Outcome(RoG.split_bet_name + " 17-20", RoG.split_bet_odds),
            Outcome(RoG.split_bet_name + " 19-20", RoG.split_bet_odds),
            Outcome(RoG.split_bet_name + " 20-21", RoG.split_bet_odds),
            Outcome(RoG.split_bet_name + " 20-23", RoG.split_bet_odds),
            Outcome(RoG.street_bet_name + " 19-20-21", RoG.street_bet_odds),
            Outcome(RoG.corner_bet_name + " 16-17-19-20", RoG.corner_bet_odds),
            Outcome(RoG.corner_bet_name + " 17-18-20-21", RoG.corner_bet_odds),
            Outcome(RoG.corner_bet_name + " 19-20-22-23", RoG.corner_bet_odds),
            Outcome(RoG.corner_bet_name + " 20-21-23-24", RoG.corner_bet_odds),
            Outcome(RoG.line_bet_name + " 16-17-18-19-20-21",
                    RoG.line_bet_odds),
            Outcome(RoG.line_bet_name + " 19-20-21-22-23-24",
                    RoG.line_bet_odds)
        ]
        actual_bin = self.test_wheel.get_bin(20)
        self.assertEqual(len(outcomes), len(actual_bin),
                         actual_bin)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_get_outcome(self):
        self.assertEqual(self.test_wheel.get_outcome("Red"),
                         Outcome(RoG.red_bet_name, RoG.even_money_bet_odds))
        self.assertEqual(self.test_wheel.get_outcome("Five 00-0-1-2-3"),
                         Outcome(RoG.five_bet_name, RoG.five_bet_odds))
        self.assertEqual(self.test_wheel.get_outcome("Split 32-33"),
                         Outcome(RoG.split_bet_name + " 32-33",
                                 RoG.split_bet_odds))


if __name__ == '__main__':
    unittest.main()
