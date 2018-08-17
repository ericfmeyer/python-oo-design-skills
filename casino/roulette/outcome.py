"""Package: casino.roulette
Module: outcome

Implements the Outcome class.
"""


class Outcome(object):
    """Outcome contains a single outcome on which a bet can be placed.

    An outcome is composed of a name and odds.
    It is responsible for calculating the payout amount.

    Collaborators:
        - Wheel: collects outcomes into bins.
        - Table: holds bets on outcomes.
        - Player: places bets on outcomes.
        - Game: collects wins and losses based on the outcomes contained in
            the winning bin.
        - Bet: is placed on an outcome.
        - Bin: contains a collection of outcomes.
    """

    def __init__(self, name, odds):
        """Initialize the Outcome instance with given name and odds.

        :param name: (str) name of the outcome (e.g. "Split 1-2").
        :param odds: (int) odds of the outcome (e.g. 17)
                Note: the denominator is assumed to be 1 (e.g. 17:1)
        """
        self.name = name
        self.odds = odds

    def win_amount(self, amount):
        """Return the amount multiplied by this Outcome odds.

        :param amount: (int) the amount being bet
        :return: (int) the amount won
        """
        return amount * self.odds

    def __eq__(self, other):
        """Compare the name attributes of self and other.

        :param other: (Outcome) other Outcome to compare against.
        :return: (boolean) returns True if the names match.
        """
        return self.name == other.name

    def __ne__(self, other):
        """Compare the name attributes of self and other.

        :param other: (Outcome) other Outcome to compare against.
        :return: (boolean) returns True if the names do not match.
        """
        return self.name != other.name

    def __hash__(self):
        """Hash value for this Outcome.

        :return: (int) the hash value of the name of this Outcome.
        """
        return hash(self.name)

    def __str__(self):
        """Easy to read string representation of this Outcome.

        :return: (str) string of the form "name (odds:1)".
        """
        return "{name:s} ({odds:d}:1)".format_map(vars(self))

    def __repr__(self):
        """Detailed representation of this Outcome object.

        :return: (str) string of the form "Outcome ('name', odds)".
        """
        return "{class_:s}({name!r}, {odds!r})".format(
            class_=type(self).__name__, **vars(self))
