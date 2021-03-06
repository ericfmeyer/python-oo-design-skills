"""Implements the Player class."""


class Player(object):
    """Player places bets on outcomes.

    It is responsible for tracking and updating the player's stake.

    Collaborators:
        - Game: player is notified by the game of win/loss.
        - Bet: player places bets on outcomes.
        - Outcome: player places bets on outcomes.
        - Table: used by player to place a bet on a specific outcome.
    """

    def __init__(self, table, wheel):
        """Create instance of Player.

        :param table: (Table) the table to place bets on.
        """
        self.stake = 0
        self.rounds_to_go = 0
        self.table = table
        self.wheel = wheel

    def is_playing(self):
        """Return True if Player is still playing.

        :return: (bool) True if still playing.
        """
        return self.rounds_to_go > 0 and self.stake > 0

    def place_bets(self):
        """Update the Table with the various Bets."""
        self.rounds_to_go -= 1

    def win(self, bet):
        """Notification from the game that the given bet was a winner.

        :param bet: (Bet) the bet which won
        """
        print("{} has won!".format(bet))
        self.stake += bet.win_amount()

    def lose(self, bet):
        """Notification from the game that the given bet was a loser.

        :param bet: (Bet) the bet that lost
        """
        print("{} has lost!".format(bet))

    def set_stake(self, value):
        """Set the player's stake with the given value.

        :param value: (int) the player's stake
        """
        self.stake = value

    def set_rounds(self, value):
        """Set the player's rounds to go with the given value.

        :param value: (int) the player's duration
        """
        self.rounds_to_go = value

    def winners(self, set_of_outcomes):
        """Notification from the game about the winning Outcomes."""
        pass
