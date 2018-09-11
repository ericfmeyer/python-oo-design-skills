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

    zero_bin = 0
    dbl_zero_bin = 37

    def setUp(self):
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)

    def test_can_create_bin_builder(self):
        self.assertIsNotNone(BinBuilder())

    # five bets
    def test_five_bets_for_zero(self):
        actual_bin = self.wheel.get_bin(self.zero_bin)
        expected = Outcome(self.five_bet_name, self.five_bet_odds)
        self.assertTrue(expected in actual_bin,
                        '{} is not in {}'.format(expected, actual_bin))

    def test_five_bets_for_dbl_zero(self):
        actual_bin = self.wheel.get_bin(self.dbl_zero_bin)
        expected = Outcome(self.five_bet_name, self.five_bet_odds)
        self.assertTrue(expected in actual_bin,
                        '{} is not in {}'.format(expected, actual_bin))

    def test_five_bets_for_one_two_three(self):
        expected = Outcome(self.five_bet_name, self.five_bet_odds)
        for i in range(1, 4):
            actual_bin = self.wheel.get_bin(i)
            self.assertTrue(expected in actual_bin,
                            '{} is not in {}'.format(expected, actual_bin))

    def test_no_other_five_bets(self):
        five_bet = Outcome(self.five_bet_name, self.five_bet_odds)
        for i in range(4, self.dbl_zero_bin):
            actual_bin = self.wheel.get_bin(i)
            self.assertTrue(five_bet not in actual_bin,
                            '{} is in {}'.format(five_bet, actual_bin))

    # verify zero has nothing but Five and Straight bets
    def test_zero_and_dbl_zero_have_only_five_and_straight_bets(self):
        zero = self.wheel.get_bin(0)
        dbl_zero = self.wheel.get_bin(37)
        for oc in zero | dbl_zero:
            self.assertTrue(
                self.five_bet_name or self.straight_bet_name in str(oc),
                '{} is not in {}'.format(self.split_bet_name, str(oc))
            )

    # straight bets
    def test_straight_bets_for_all_except_double_zero(self):
        for bin_number in range(0, 37):
            actual_bin = self.wheel.get_bin(bin_number)
            expected = Outcome(
                '{} {}'.format(self.straight_bet_name, bin_number),
                self.straight_bet_odds)
            self.assertTrue(expected in actual_bin,
                            '{} is not in {}'.format(expected, actual_bin))

    def test_straight_bets_for_dbl_zero(self):
        bin_number = 37
        actual_bin = self.wheel.get_bin(bin_number)
        expected = Outcome(
            '{} {}'.format(self.straight_bet_name, '00'),
            self.straight_bet_odds)
        self.assertTrue(expected in actual_bin,
                        '{} is not in {}'.format(expected, actual_bin))

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
        expected = Outcome('{} {}-{}'.format(self.split_bet_name, n, n + inc),
                           self.split_bet_odds)
        self.assertTrue(expected in actual_bin1,
                        '{} is not in {}'.format(expected, actual_bin1))
        self.assertTrue(expected in actual_bin2,
                        '{} is not in {}'.format(expected, actual_bin2))

    # street bets
    def test_street_bets(self):
        for row in range(0, 12):
            n = 3 * row + 1
            exp_oc = Outcome(
                '{} {}-{}-{}'.format(self.street_bet_name, n, n + 1, n + 2),
                self.street_bet_odds)
            for i in range(0, 3):
                actual_bin = self.wheel.get_bin(n + i)
                self.assertTrue(exp_oc in actual_bin,
                                '{} is not in {}'.format(exp_oc, actual_bin))

    # corner bets
    def test_corner_bets_for_all_corners(self):
        self.assertTrue(
            Outcome(self.corner_bet_name + ' 1-2-4-5',
                    self.corner_bet_odds)
            in self.wheel.get_bin(1)
        )
        self.assertTrue(
            Outcome(self.corner_bet_name + ' 2-3-5-6',
                    self.corner_bet_odds)
            in self.wheel.get_bin(3)
        )
        self.assertTrue(
            Outcome(self.corner_bet_name + ' 31-32-34-35',
                    self.corner_bet_odds)
            in self.wheel.get_bin(34)
        )
        self.assertTrue(
            Outcome(self.corner_bet_name + ' 32-33-35-36',
                    self.corner_bet_odds)
            in self.wheel.get_bin(36)
        )

    def test_corner_bets_for_top_edge(self):
        ocs = [Outcome(self.corner_bet_name + ' 1-2-4-5',
                       self.corner_bet_odds),
               Outcome(self.corner_bet_name + ' 2-3-5-6',
                       self.corner_bet_odds)]
        for exp in ocs:
            self.assertTrue(exp in self.wheel.get_bin(2))

    def test_corner_bets_for_bottom_edge(self):
        ocs = [Outcome(self.corner_bet_name + ' 31-32-34-35',
                       self.corner_bet_odds),
               Outcome(self.corner_bet_name + ' 32-33-35-36',
                       self.corner_bet_odds)]
        for exp in ocs:
            self.assertTrue(exp in self.wheel.get_bin(35))

    # line bets
    def test_all_line_bets(self):
        for row in range(0, 11):
            n = 3 * row + 1
            exp = Outcome(self.line_bet_name +
                          ' {:d}-{:d}-{:d}-{:d}-{:d}-{:d}'
                          .format(n, n + 1, n + 2, n + 3, n + 4, n + 5),
                          self.line_bet_odds)
            for i in range(n, n + 6):
                actual_bin = self.wheel.get_bin(n)
                self.assertTrue(exp in actual_bin,
                                '{} is not in {}'.format(exp, actual_bin))

    # dozen bets
    def test_all_dozen_bets(self):
        for dozen in range(0, 3):
            exp = Outcome('{} {}'.format(self.dozen_bet_name, dozen + 1),
                          self.dozen_bet_odds)
            for n in range(0, 12):
                bin_number = 12 * dozen + n + 1
                actual_bin = self.wheel.get_bin(bin_number)
                self.assertTrue(exp in actual_bin,
                                '{} is not in {}'.format(exp, actual_bin))

    # column bets
    def test_all_column_bets(self):
        for col in range(0, 3):
            exp = Outcome('{} {}'.format(self.column_bet_name, col + 1),
                          self.dozen_bet_odds)
            for row in range(0, 12):
                bin_number = 3 * row + col + 1
                actual_bin = self.wheel.get_bin(bin_number)
                self.assertTrue(exp in actual_bin,
                                '{} is not in {}'.format(exp, actual_bin))

    # even money bets
    def test_some_red_bets(self):
        red = Outcome(self.red_bet_name, self.even_money_bet_odds)
        self.assertTrue(red in self.wheel.get_bin(9))
        self.assertTrue(red in self.wheel.get_bin(18))

    def test_some_black_bets(self):
        black = Outcome(self.black_bet_name, self.even_money_bet_odds)
        self.assertTrue(black in self.wheel.get_bin(6))
        self.assertTrue(black in self.wheel.get_bin(31))


if __name__ == '__main__':
    unittest.main()
