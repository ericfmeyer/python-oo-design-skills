"""Package: casino.roulette
Module: player

Implements the Player class.
"""


class Player(object):
    """Player places bets on outcomes.

    It is responsible for updating the player's stake.

    Collaborators:
        - Game: player is notified by the game of win/loss.
        - Bet: player places bets on outcomes.
        - Outcome: player places bets on outcomes.
        - Table: used by player to place a bet on a specific outcome.
    """
    def __init__(self, table):
        """Create instance of Player.

        :param table: (Table) the table to place bets on.
        """
        self.stake = 0
        self.rounds_to_go = 0
        self.table = table

    def playing(self):
        """Return True if Player is still playing.

        :return: (bool) True if still playing.
        """
        return True

    def place_bets(self):
        """Update the Table with the various Bets."""
        pass
