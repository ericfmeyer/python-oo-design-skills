import unittest

from casino.roulette.binbuilder import BinBuilder
from casino.roulette.outcome import Outcome
from casino.roulette.game import RouletteGame as RoG
from casino.roulette.wheel import Wheel


class BinBuilderTest(unittest.TestCase):
    """Test the implementation of the class BinBuilder."""

    def setUp(self):
        self.bin_builder = BinBuilder()
        self.wheel = Wheel()

    def test_can_create_bin_builder(self):
        self.assertIsNotNone(self.bin_builder)

    def test_builder_generates_five_bets(self):
        self.bin_builder.build_five_bets(self.wheel)
        actual_bin = self.wheel.get_bin(0)
        expected = Outcome(RoG.five_bet_name, RoG.five_bet_odds)
        self.assertTrue(expected in actual_bin)

    def test_builder_generates_straight_bets_for_all_except_double_zero(self):
        self.bin_builder.build_straight_bets(self.wheel)
        for bin_number in range(0, 37):
            actual_bin = self.wheel.get_bin(bin_number)
            expected = Outcome(
                '{} {}'.format(RoG.straight_bet_name, bin_number),
                RoG.five_bet_odds)
            self.assertTrue(expected in actual_bin)

    def test_builder_generates_straight_bets_for_double_zero(self):
        self.bin_builder.build_straight_bets(self.wheel)
        bin_number = 37
        actual_bin = self.wheel.get_bin(bin_number)
        expected = Outcome(
            '{} {}'.format(RoG.straight_bet_name, '00'),
            RoG.five_bet_odds)
        self.assertTrue(expected in actual_bin)


if __name__ == '__main__':
    unittest.main()
