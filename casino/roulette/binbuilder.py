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

    @classmethod
    def add_five_bets(cls, wheel):
        """Add five bet outcomes to the bin 0 and 00"""
        for i in (0, 37):
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
        pass

    @classmethod
    def add_corner_bets(cls, wheel):
        pass

    @classmethod
    def add_line_bets(cls, wheel):
        pass

    @classmethod
    def add_dozen_bets(cls, wheel):
        pass

    def add_column_bets(self, wheel):
        pass
