"""Implements the BinBuilder class."""

from casino.roulette.game import RouletteGame as RoG
from casino.roulette.outcome import Outcome


class BinBuilder(object):
    """Helper class to generate all outcomes and associate them to a wheel."""

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
        """Add the Five Bet outcome to bins 00, 0, 1, 2 and 3."""
        for i in (0, 1, 2, 3, 37):
            wheel.add_outcome(i, Outcome(RoG.FIVE_BET_NAME, RoG.FIVE_BET_ODDS))

    @classmethod
    def add_straight_bets(cls, wheel):
        """Add all Straight Bet outcomes to the corresponding bins."""
        for n in range(0, 37):
            wheel.add_outcome(n, Outcome(
                '{} {}'.format(RoG.STRAIGHT_BET_NAME, n),
                RoG.STRAIGHT_BET_ODDS))

        # special case for double zero, at index 37
        wheel.add_outcome(37, Outcome(
            '{} {}'.format(RoG.STRAIGHT_BET_NAME, '00'),
            RoG.STRAIGHT_BET_ODDS))

    @classmethod
    def add_split_bets(cls, wheel):
        """Add all Split Bet outcomes to the corresponding bins."""
        # add all {n, n + 1} outcomes
        for row in range(0, 12):
            cls.helper_add_split_bets(wheel, row * 3 + 1, 1)
            cls.helper_add_split_bets(wheel, row * 3 + 2, 1)

        # add all {n, n + 3} outcomes
        for i in range(1, 34):
            cls.helper_add_split_bets(wheel, i, 3)

    @classmethod
    def helper_add_split_bets(cls, wheel, n_bin, inc):
        """Helper function to add Split Bet outcomes."""
        oc = Outcome(
            '{} {}-{}'.format(RoG.SPLIT_BET_NAME, n_bin, n_bin + inc),
            RoG.SPLIT_BET_ODDS)
        wheel.add_outcome(n_bin, oc)
        wheel.add_outcome(n_bin + inc, oc)

    @classmethod
    def add_street_bets(cls, wheel):
        """Add all Street Bet outcomes to the corresponding bins."""
        for row in range(0, 12):
            n = 3 * row + 1
            oc = Outcome(
                '{} {}-{}-{}'.format(RoG.STREET_BET_NAME, n, n + 1, n + 2),
                RoG.STREET_BET_ODDS
            )
            for i in range(0, 3):
                wheel.add_outcome(n + i, oc)

    @classmethod
    def add_corner_bets(cls, wheel):
        """Add all Corner Bet outcomes to the corresponding bins."""
        for row in range(0, 11):
            for i in range(1, 3):
                n = 3 * row + i
                oc = Outcome(
                    '{} {}-{}-{}-{}'.format(
                        RoG.CORNER_BET_NAME, n, n + 1, n + 3, n + 4),
                    RoG.CORNER_BET_ODDS
                )
                for j in [n, n + 1, n + 3, n + 4]:
                    wheel.add_outcome(j, oc)

    @classmethod
    def add_line_bets(cls, wheel):
        """Add all Line Bet outcomes to the corresponding bins."""
        for row in range(0, 11):
            n = 3 * row + 1
            oc = Outcome(
                '{:s} {:d}-{:d}-{:d}-{:d}-{:d}-{:d}'
                    .format(RoG.LINE_BET_NAME,
                            n, n + 1, n + 2, n + 3, n + 4, n + 5),
                RoG.LINE_BET_ODDS
            )
            for i in range(0, 6):
                wheel.add_outcome(n + i, oc)

    @classmethod
    def add_dozen_bets(cls, wheel):
        """Add all Dozen Bet outcomes to the corresponding bins."""
        for dozen in range(0, 3):
            oc = Outcome('{} {}'.format(RoG.DOZEN_BET_NAME, dozen + 1),
                         RoG.DOZEN_BET_ODDS)
            for n in range(0, 12):
                bin_number = 12 * dozen + n + 1
                wheel.add_outcome(bin_number, oc)

    @classmethod
    def add_column_bets(cls, wheel):
        """Add all Column Bet outcomes to the corresponding bins."""
        for col in range(0, 3):
            oc = Outcome('{} {}'.format(RoG.COLUMN_BET_NAME, col + 1),
                         RoG.DOZEN_BET_ODDS)
            for row in range(0, 12):
                bin_number = 3 * row + col + 1
                wheel.add_outcome(bin_number, oc)

    @classmethod
    def add_even_money_bets(cls, wheel):
        """Add all Even Money Bet outcomes to the corresponding bins."""
        red = Outcome(RoG.RED_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)
        black = Outcome(RoG.BLACK_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)
        even = Outcome(RoG.EVEN_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)
        odd = Outcome(RoG.ODD_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)
        high = Outcome(RoG.HIGH_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)
        low = Outcome(RoG.LOW_BET_NAME, RoG.EVEN_MONEY_BET_ODDS)

        for bin_number in range(1, 37):
            if bin_number < 19:
                wheel.add_outcome(bin_number, low)
            else:
                wheel.add_outcome(bin_number, high)

            if bin_number % 2 == 0:
                wheel.add_outcome(bin_number, even)
            else:
                wheel.add_outcome(bin_number, odd)

            if bin_number in RoG.RED_BINS:
                wheel.add_outcome(bin_number, red)
            else:
                wheel.add_outcome(bin_number, black)
