"""Implements the Wheel class."""

from random import Random

from casino.roulette.bin import Bin


class Wheel(object):
    """Collection of bins that randomly selects the outcomes that win.

    It holds the collection of all bins, and picks a bin at random.

    Collaborators:
        - Game: spins the wheel.
        - Bin: wheel has 38 bins and picks a winning bin.
        - Outcome: wheel selects the outcomes that win.
    """

    def __init__(self):
        """Create a new Wheel with 38 empty bins."""
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = Random()
        self.all_outcomes = dict()

    def add_outcome(self, number, outcome):
        """Add the outcome to the bin given by the number.

        :param number: (int) bin number - 0-37 inclusive.
        :param outcome: (Outcome) outcome to add.
        :return:
        """
        self.bins[number].add(outcome)
        self.all_outcomes[outcome.name] = outcome

    def next(self):
        """Return a bin at random.

        :return: (Bin) the winning bin.
        """
        return self.rng.choice(self.bins)

    def get_bin(self, n):
        """Return the given Bin from the collection.

        :param n: (int) bin number - 0-37 inclusive.
        :return: (Bin) the requested bin.
        """
        return self.bins[n]

    def get_outcome(self, name):
        """Return an outcome based on the name.

        :param name: (str) name of the outcome.
        :return: (Outcome) the outcome associated to the name.
        """
        return self.all_outcomes.get(name)
