"""Implements the Passenger57 class.

Stub player - always bets on black.
"""

from casino.roulette.bet import Bet
from casino.roulette.game import Game
from casino.roulette.player import Player


class Passenger57(Player):
    """Passenger57 always bets on Black.

    Passenger57 gets the Black outcome from the Wheel,
    constructs a bet on that outcome, and places the bet.
    """

    def __init__(self, table, wheel):
        """Create instance of Passenger57 that always bets on Black.

        :param table: (Table) the table to place bets on.
        :param wheel: (Wheel) the wheel instance which defines all Outcomes.
        """
        super().__init__(table, wheel)
        self.black = wheel.get_outcome(Game.BLACK_BET_NAME)

    def place_bets(self):
        """Place a bet on Black outcome."""
        super().place_bets()
        amount = 50
        self.stake -= amount
        self.table.place_bet(Bet(amount, self.black))
