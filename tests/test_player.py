import unittest

from casino.roulette.player import Player
from casino.roulette.table import Table


class PlayerTest(unittest.TestCase):
    """Test the implementation of the class Player."""

    def setUp(self):
        self.player = Player(Table())

    def test_can_create_player(self):
        self.assertIsNotNone(self.player)


if __name__ == '__main__':
    unittest.main()
