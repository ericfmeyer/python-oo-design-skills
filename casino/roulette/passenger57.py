"""Package: casino.roulette
Module: passenger57

Implements the Passenger57 class.

Stub player - always bets on black.
"""

from casino.roulette.bet import Bet
from casino.roulette.game import RouletteGame as RoG


class Passenger57(object):
    """Passenger57 always bets on Black.

    Passenger57 gets the Black outcome from the Wheel,
    constructs a bet on that outcome, and places the bet.
    """
    def __init__(self, table, wheel):
        """

        :param table: (Table) the table to place bets on.
        :param wheel: (Wheel) the wheel instance which defines all Outcomes.
        """
        self.table = table
        self.black = wheel.get_outcome(RoG.BLACK_BET_NAME)

    def place_bets(self):
        """Place a bet on Black outcome."""
        self.table.place_bet(Bet(50, self.black))

    def win(self, bet):
        """Notification from the game about the bet that won.

        :param bet: (Bet) the bet that won.
        """
        print("{} has won!".format(bet))

    def lose(self, bet):
        """Notification from the game about the bet that lost.

        :param bet: (Bet) the bet that lost.
        """
        print("{} has lost!".format(bet))
