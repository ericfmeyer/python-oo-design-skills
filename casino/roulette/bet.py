"""Package: casino.roulette
Module: bet

Implements the Bet class.
"""


class Bet(object):
    """Bet holds the amount bet on a particular outcome.

    Collaborators:
        - Outcome: is paired with bet.
        - Table: collects all player bets.
        - Player: creates bets.
    """

    def __init__(self, amount, outcome):
        """Create a new bet of a specific amount on a specific outcome.

        :param amount: (int) the amount bet on the outcome.
        :param outcome: (Outcome) the outcome being bet on.
        """
        # TODO: associate bet with a player
        self.amount = amount
        self.outcome = outcome

    def win_amount(self):
        """Return the amount won.

        :return: (int) amount won.
        """
        return self.amount + self.outcome.win_amount(self.amount)

    def lose_amount(self):
        """Return the amount lost.

        :return: (int) amount lost.
        """
        return self.amount

    def __str__(self):
        """String representation of the form 'amount on outcome'.

        :return: (str) 'amount on outcome'.
        """
        return '{:d} on {:s}'.format(self.amount, str(self.outcome))

    def __repr__(self):
        """String representation of the form 'Bet(amount, outcome)'.

        :return: (str) 'Bet(amount, outcome)'.
        """
        return 'Bet({:d}, {:s})'.format(self.amount, str(self.outcome))
