"""Implements the IntegerStatistics class."""

import math


class IntegerStatistics(list):
    """Calculate several simple statistics of Integer values in a list."""

    def mean(self):
        """Return the mean of the list of values."""
        return sum(self) / len(self)

    def stddev(self):
        """Return the standard deviation of the list of values.

        The value returned has 5 decimal digits.
        """
        m = self.mean()
        return round(
            math.sqrt(sum((x - m)**2 for x in self) / (len(self) - 1)),
            ndigits=5
        )
