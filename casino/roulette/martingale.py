"""Implements the Martingale class."""

from casino.roulette.bet import Bet
from casino.roulette.game import RouletteGame as RoG
from casino.roulette.player import Player


class Martingale(Player):
    """This player follows the Martingale betting strategy.

    The player doubles their bet on every loss and resets their bet to a base
    amount on each win.
    """

    def __init__(self, table, wheel):
        """Create a Martingale player instance.

        :param table: (Table) the table to place bets.
        :param wheel: (Wheel) the wheel go get outcomes.
        """
        super().__init__(table, wheel)
        self.loss_count = 0
        self.bet_multiplier = 1
        self.black_outcome = self.wheel.get_outcome(RoG.BLACK_BET_NAME)

    def place_bets(self):
        """Place bet on the table."""
        self.stake -= self.bet_multiplier
        self.table.place_bet(Bet(self.bet_multiplier, self.black_outcome))

    def win(self, bet):
        """Notification from the game that the bet won.

        Resets the loss count and bet multiplier.
        """
        super().win(bet)
        self.loss_count = 0
        self.bet_multiplier = 1

    def lose(self, bet):
        """Notification from the game that the bet lost.

        Increments the loss count and updates the bet multiplier.
        """
        super().lose(bet)
        self.loss_count += 1
        self.bet_multiplier = 2 ** self.loss_count
