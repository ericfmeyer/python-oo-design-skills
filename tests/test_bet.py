import unittest

from casino.roulette.bet import Bet


class BetTest(unittest.TestCase):
    """Test the implementation of the class Bet."""
    def setUp(self):
        self.bet = Bet()

    def test_can_create_bet(self):
        self.assertIsNotNone(self.bet)


if __name__ == '__main__':
    unittest.main()
