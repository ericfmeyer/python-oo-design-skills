import unittest

from casino.roulette.binbuilder import BinBuilder
from casino.roulette.outcome import Outcome
from casino.roulette.wheel import Wheel


class BinBuilderTest(unittest.TestCase):
    """Test the implementation of the class BinBuilder."""

    straight_bet_odds = 35
    split_bet_odds = 17
    street_bet_odds = 11
    corner_bet_odds = 8
    five_bet_odds = 6
    line_bet_odds = 5
    dozen_bet_odds = 2
    column_bet_odds = 2
    even_money_bet_odds = 1

    straight_bet_name = 'Number'
    split_bet_name = 'Split'
    street_bet_name = 'Street'
    corner_bet_name = 'Corner'
    five_bet_name = 'Five 00-0-1-2-3'
    line_bet_name = 'Line'
    dozen_bet_name = 'Dozen'
    column_bet_name = 'Column'
    black_bet_name = 'Black'
    red_bet_name = 'Red'
    even_bet_name = 'Even'
    odd_bet_name = 'Odd'
    high_bet_name = 'High'
    low_bet_name = 'Low'

    def setUp(self):
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)

    def test_can_create_bin_builder(self):
        self.assertIsNotNone(BinBuilder())

    # five bets
    def test_five_bets_for_zero(self):
        actual_bin = self.wheel.get_bin(0)
        expected = Outcome(self.five_bet_name, self.five_bet_odds)
        self.assertTrue(expected in actual_bin)

    def test_five_bets_for_dbl_zero(self):
        actual_bin = self.wheel.get_bin(37)
        expected = Outcome(self.five_bet_name, self.five_bet_odds)
        self.assertTrue(expected in actual_bin)

    def test_no_other_five_bets(self):
        five_bet = Outcome(self.five_bet_name, self.five_bet_odds)
        for i in range(1, 37):
            self.assertTrue(five_bet not in self.wheel.get_bin(i))

    # straight bets
    def test_straight_bets_for_all_except_double_zero(self):
        for bin_number in range(0, 37):
            actual_bin = self.wheel.get_bin(bin_number)
            expected = Outcome(
                '{} {}'.format(self.straight_bet_name, bin_number),
                self.straight_bet_odds)
            self.assertTrue(expected in actual_bin)

    def test_straight_bets_for_dbl_zero(self):
        bin_number = 37
        actual_bin = self.wheel.get_bin(bin_number)
        expected = Outcome(
            '{} {}'.format(self.straight_bet_name, '00'),
            self.straight_bet_odds)
        self.assertTrue(expected in actual_bin)

    # split bets
    def test_all_split_bets(self):
        for row in range(0, 12):
            self.helper_split_bets_test(row * 3 + 1, 1)
            self.helper_split_bets_test(row * 3 + 2, 1)

        for i in range(1, 34):
            self.helper_split_bets_test(i, 3)

    def helper_split_bets_test(self, n, inc):
        actual_bin1 = self.wheel.get_bin(n)
        actual_bin2 = self.wheel.get_bin(n + inc)
        exp_1 = Outcome('{} {}-{}'.format(self.split_bet_name, n, n + inc),
                        self.split_bet_odds)
        self.assertTrue(exp_1 in actual_bin1)
        self.assertTrue(exp_1 in actual_bin2)

    def test_no_split_bets_for_zeros(self):
        zero = self.wheel.get_bin(0)
        dbl_zero = self.wheel.get_bin(37)
        for oc in zero | dbl_zero:
            self.assertTrue(self.split_bet_name not in str(oc))

    # street bets
    def test_street_bets(self):
        pass


if __name__ == '__main__':
    unittest.main()
