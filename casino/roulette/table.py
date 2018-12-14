"""Implements the Table class."""


class InvalidBet(Exception):
    """Raised when the player attempts to place an invalid bet.

    An invalid bet is a bet which exceeds the table's limit.
    """

    pass


class Table(object):
    """Collection of bets placed by players on outcomes.

    A table has a betting limit, and the sum of all players' bets
    must be less than or equal to this limit.

    A table also has a betting minimum.

    We assume a single player in the simulation.

    Collaborators:
        - Game: uses table to compute the amount won and lost.
        - Bet: collected by table.
        - Outcome: collected by table.
        - Player: uses table to place bets on specific outcomes.
    """

    TABLE_MIN = 10
    TABLE_LIMIT = 300

    def __init__(self):
        """Create an instance of a Table.

        Class members:
            - limit: the table limit.
            - minimum: the minimum bet amount.
            - bets: list of bets placed by players.
        """
        self.limit = self.TABLE_LIMIT
        self.minimum = self.TABLE_MIN
        self.bets = list()

    def place_bet(self, bet):
        """Add the bet to the list of working bets.

        :param bet: a bet instance to add to the table.
        """
        self.bets.append(bet)

    def clear_bets(self):
        """Remove all bets from the table."""
        self.bets.clear()

    def __iter__(self):
        """Return an iterator over the available list of bets."""
        return self.bets[:].__iter__()

    def __str__(self):
        """Return string of all the current bets.

        :return: (str) string of all the bets.
        """
        return '\n'.join(str(bet) for bet in self.bets)

    def __repr__(self):
        """Return string of the form Table( bet, bet, bet ).

        :return: (str) Table( bet, bet, bet ).
        """
        return 'Table( {} )'.format(', '.join(repr(bet) for bet in self.bets))

    def is_valid(self):
        """Return true if all bets on the table are valid.

        :return: True if all bets valid.
        """
        total = 0
        for bet in self.bets:
            if bet.amount < self.minimum:
                raise InvalidBet
            total += bet.amount

        if total > self.limit:
            raise InvalidBet

        return True
