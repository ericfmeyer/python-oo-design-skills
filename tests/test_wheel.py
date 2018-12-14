import unittest
from unittest.mock import Mock

from casino.roulette.bin import Bin
from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.outcome import Outcome
from casino.roulette.wheel import Wheel

TEST_BIN = "bin1"


class WheelTest(unittest.TestCase):
    """Test the implementation of the class Wheel."""
    def setUp(self):
        self.test_wheel = Wheel()
        BinBuilder().build_bins(self.test_wheel)
        self.test_wheel.rng = Mock()
        self.test_wheel.rng.choice = Mock(return_value=TEST_BIN)

    def test_can_create_wheel(self):
        self.assertIsNotNone(self.test_wheel)

    def test_wheel_contains_38_bins(self):
        expected_bins = 38
        self.assertEqual(expected_bins, len(self.test_wheel.bins))
        self.assertIsInstance(self.test_wheel.bins[0], Bin)

    def test_get_returns_correct_bin(self):
        self.assertEqual(self.test_wheel.get_bin(1), self.test_wheel.bins[1])

    def test_wheel_returns_expected_bin(self):
        self.assertTrue(self.test_wheel.next() == TEST_BIN)

    def test_zero_bin_outcomes(self):
        outcomes = [Outcome(Game.FIVE_BET_NAME, Game.FIVE_BET_ODDS),
                    Outcome(Game.STRAIGHT_BET_NAME + ' 0',
                            Game.STRAIGHT_BET_ODDS)]
        actual_bin = self.test_wheel.get_bin(0)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_bin_one_outcomes(self):
        outcomes = [
            Outcome(Game.STRAIGHT_BET_NAME + ' 1', Game.STRAIGHT_BET_ODDS),
            Outcome(Game.RED_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.ODD_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.LOW_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.COLUMN_BET_NAME + " 1", Game.COLUMN_BET_ODDS),
            Outcome(Game.DOZEN_BET_NAME + " 1", Game.DOZEN_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 1-2", Game.SPLIT_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 1-4", Game.SPLIT_BET_ODDS),
            Outcome(Game.STREET_BET_NAME + " 1-2-3", Game.STREET_BET_ODDS),
            Outcome(Game.CORNER_BET_NAME + " 1-2-4-5", Game.CORNER_BET_ODDS),
            Outcome(Game.FIVE_BET_NAME, Game.FIVE_BET_ODDS),
            Outcome(Game.LINE_BET_NAME + " 1-2-3-4-5-6", Game.LINE_BET_ODDS)
        ]
        actual_bin = self.test_wheel.get_bin(1)
        self.assertEqual(len(outcomes), len(actual_bin),
                         actual_bin)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_bin_twenty_outcomes(self):
        outcomes = [
            Outcome(Game.STRAIGHT_BET_NAME + ' 20', Game.STRAIGHT_BET_ODDS),
            Outcome(Game.BLACK_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.EVEN_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.HIGH_BET_NAME, Game.EVEN_MONEY_BET_ODDS),
            Outcome(Game.COLUMN_BET_NAME + " 2", Game.COLUMN_BET_ODDS),
            Outcome(Game.DOZEN_BET_NAME + " 2", Game.DOZEN_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 17-20", Game.SPLIT_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 19-20", Game.SPLIT_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 20-21", Game.SPLIT_BET_ODDS),
            Outcome(Game.SPLIT_BET_NAME + " 20-23", Game.SPLIT_BET_ODDS),
            Outcome(Game.STREET_BET_NAME + " 19-20-21", Game.STREET_BET_ODDS),
            Outcome(Game.CORNER_BET_NAME + " 16-17-19-20",
                    Game.CORNER_BET_ODDS),
            Outcome(Game.CORNER_BET_NAME + " 17-18-20-21",
                    Game.CORNER_BET_ODDS),
            Outcome(Game.CORNER_BET_NAME + " 19-20-22-23",
                    Game.CORNER_BET_ODDS),
            Outcome(Game.CORNER_BET_NAME + " 20-21-23-24",
                    Game.CORNER_BET_ODDS),
            Outcome(Game.LINE_BET_NAME + " 16-17-18-19-20-21",
                    Game.LINE_BET_ODDS),
            Outcome(Game.LINE_BET_NAME + " 19-20-21-22-23-24",
                    Game.LINE_BET_ODDS)
        ]
        actual_bin = self.test_wheel.get_bin(20)
        self.assertEqual(len(outcomes), len(actual_bin),
                         actual_bin)
        for exp in outcomes:
            self.assertTrue(exp in actual_bin,
                            '{} not in {}'.format(exp, actual_bin))

    def test_get_outcome(self):
        self.assertEqual(self.test_wheel.get_outcome("Red"),
                         Outcome(Game.RED_BET_NAME, Game.EVEN_MONEY_BET_ODDS))
        self.assertEqual(self.test_wheel.get_outcome("Five 00-0-1-2-3"),
                         Outcome(Game.FIVE_BET_NAME, Game.FIVE_BET_ODDS))
        self.assertEqual(self.test_wheel.get_outcome("Split 32-33"),
                         Outcome(Game.SPLIT_BET_NAME + " 32-33",
                                 Game.SPLIT_BET_ODDS))


if __name__ == '__main__':
    unittest.main()
