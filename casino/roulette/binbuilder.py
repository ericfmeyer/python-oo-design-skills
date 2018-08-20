"""Package: casino.roulette
Module: binbuilder

Implements the BinBuilder class.
"""

from casino.roulette.outcome import Outcome
from casino.roulette.game import RouletteGame as RoG


class BinBuilder(object):
    def __init__(self):
        pass

    def build_bins(self, wheel):
        self.build_five_bets(wheel)
        self.build_straight_bets(wheel)

    @classmethod
    def build_five_bets(cls, wheel):
        wheel.add_outcome(0, Outcome(RoG.five_bet_name, RoG.five_bet_odds))

    @classmethod
    def build_straight_bets(cls, wheel):
        for n in range(0, 37):
            wheel.add_outcome(n, Outcome(
                '{} {}'.format(RoG.straight_bet_name, n),
                RoG.straight_bet_odds))

        # special case for double zero, at index 37
        wheel.add_outcome(37, Outcome(
            '{} {}'.format(RoG.straight_bet_name, '00'),
            RoG.straight_bet_odds))

    def build_split_bets(self, wheel):
        pass

    def build_street_bets(self, wheel):
        pass

    def build_corner_bets(self, wheel):
        pass

    def build_line_bets(self, wheel):
        pass

    def build_dozen_bets(self, wheel):
        pass

    def build_column_bets(self, wheel):
        pass
