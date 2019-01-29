"""Implements the SevenReds player class."""

from casino.roulette.game import Game
from casino.roulette.martingale import Martingale


class SevenReds(Martingale):
    """This player waits for seven Red wins in a row before betting Black."""

    def __init__(self, table, wheel):
        """Create instance of SevenReds player based on Martingale player.

        :param table: (Table) the table to place bets on.
        :param wheel: (Wheel) the wheel instance which defines all Outcomes.

        Members:
            reds_to_go: (int) number of reds to win before the player bets.
        """
        super().__init__(table, wheel)
        self.reds_to_go = 7

    def place_bets(self):
        """Place a bet if there has been at least 7 reds in a row."""
        if self.reds_to_go == 0:
            super().place_bets()

    def winners(self, set_of_outcomes):
        """Used by Game to notify player of the winning outcomes.

        If red is in the set of Outcomes, decrements reds_to_go.
        Otherwise, reset reds_to_go to 7.
        :param set_of_outcomes: (set of Outcomes)
        """
        if self.wheel.get_outcome(Game.RED_BET_NAME) in set_of_outcomes:
            if self.reds_to_go > 0:
                self.reds_to_go -= 1
        else:
            self.reds_to_go = 7
