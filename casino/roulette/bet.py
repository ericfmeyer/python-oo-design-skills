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
        self.amount = amount
        self.outcome = outcome

    pass
