"""Package: casino.roulette
Module: binbuilder

Implements the BinBuilder class.
"""

from casino.roulette.outcome import Outcome
from casino.roulette.game import RouletteGame as RoG


class BinBuilder(object):
    def __init__(self):
        """Create an instance of BinBuilder."""
        pass

    def build_bins(self, wheel):
        """Build the bins of the wheel.

        :param wheel: the wheel with bins to populate with outcomes.
        """
        self.add_five_bets(wheel)
        self.add_straight_bets(wheel)
        self.add_split_bets(wheel)
        self.add_street_bets(wheel)
        self.add_corner_bets(wheel)
        self.add_line_bets(wheel)
        self.add_column_bets(wheel)
        self.add_dozen_bets(wheel)
        self.add_even_money_bets(wheel)

    @classmethod
    def add_five_bets(cls, wheel):
        """Add five bet outcomes to bins 00, 0, 1, 2 and 3"""
        for i in (0, 1, 2, 3, 37):
            wheel.add_outcome(i, Outcome(RoG.five_bet_name, RoG.five_bet_odds))

    @classmethod
    def add_straight_bets(cls, wheel):
        for n in range(0, 37):
            wheel.add_outcome(n, Outcome(
                '{} {}'.format(RoG.straight_bet_name, n),
                RoG.straight_bet_odds))

        # special case for double zero, at index 37
        wheel.add_outcome(37, Outcome(
            '{} {}'.format(RoG.straight_bet_name, '00'),
            RoG.straight_bet_odds))

    @classmethod
    def add_split_bets(cls, wheel):
        # add all {n, n + 1} outcomes
        for row in range(0, 12):
            cls.helper_add_split_bets(wheel, row * 3 + 1, 1)
            cls.helper_add_split_bets(wheel, row * 3 + 2, 1)

        # add all {n, n + 3} outcomes
        for i in range(1, 34):
            cls.helper_add_split_bets(wheel, i, 3)

    @classmethod
    def helper_add_split_bets(cls, wheel, n_bin, inc):
        oc = Outcome(
            '{} {}-{}'.format(RoG.split_bet_name, n_bin, n_bin + inc),
            RoG.split_bet_odds)
        wheel.add_outcome(n_bin, oc)
        wheel.add_outcome(n_bin + inc, oc)

    @classmethod
    def add_street_bets(cls, wheel):
        for row in range(0, 12):
            n = 3 * row + 1
            oc = Outcome(
                '{} {}-{}-{}'.format(RoG.street_bet_name, n, n + 1, n + 2),
                RoG.street_bet_odds
            )
            for i in range(0, 3):
                wheel.add_outcome(n + i, oc)

    @classmethod
    def add_corner_bets(cls, wheel):
        for row in range(0, 11):
            for i in range(1, 3):
                n = 3 * row + i
                oc = Outcome(
                    '{} {}-{}-{}-{}'.format(
                        RoG.corner_bet_name, n, n + 1, n + 3, n + 4),
                    RoG.corner_bet_odds
                )
                for j in [n, n + 1, n + 3, n + 4]:
                    wheel.add_outcome(j, oc)

    @classmethod
    def add_line_bets(cls, wheel):
        for row in range(0, 11):
            n = 3 * row + 1
            oc = Outcome(
                '{:s} {:d}-{:d}-{:d}-{:d}-{:d}-{:d}'
                .format(RoG.line_bet_name,
                        n, n + 1, n + 2, n + 3, n + 4, n + 5),
                RoG.line_bet_odds
            )
            for i in range(0, 6):
                wheel.add_outcome(n + i, oc)

    @classmethod
    def add_dozen_bets(cls, wheel):
        for dozen in range(0, 3):
            oc = Outcome('{} {}'.format(RoG.dozen_bet_name, dozen + 1),
                         RoG.dozen_bet_odds)
            for n in range(0, 12):
                bin_number = 12 * dozen + n + 1
                wheel.add_outcome(bin_number, oc)

    @classmethod
    def add_column_bets(cls, wheel):
        for col in range(0, 3):
            oc = Outcome('{} {}'.format(RoG.column_bet_name, col + 1),
                         RoG.dozen_bet_odds)
            for row in range(0, 12):
                bin_number = 3 * row + col + 1
                wheel.add_outcome(bin_number, oc)

    @classmethod
    def add_even_money_bets(cls, wheel):
        red = Outcome(RoG.red_bet_name, RoG.even_money_bet_odds)
        black = Outcome(RoG.black_bet_name, RoG.even_money_bet_odds)
        even = Outcome(RoG.even_bet_name, RoG.even_money_bet_odds)
        odd = Outcome(RoG.odd_bet_name, RoG.even_money_bet_odds)
        high = Outcome(RoG.high_bet_name, RoG.even_money_bet_odds)
        low = Outcome(RoG.low_bet_name, RoG.even_money_bet_odds)

        for bin_number in range(1, 37):
            if bin_number < 19:
                wheel.add_outcome(bin_number, low)
            else:
                wheel.add_outcome(bin_number, high)

            if bin_number % 2 == 0:
                wheel.add_outcome(bin_number, even)
            else:
                wheel.add_outcome(bin_number, odd)

            if bin_number in RoG.red_bins:
                wheel.add_outcome(bin_number, red)
            else:
                wheel.add_outcome(bin_number, black)
