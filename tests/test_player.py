import unittest

from casino.roulette.player import Player


class PlayerTest(unittest.TestCase):
    """Test the implementation of the class Player."""

    def setUp(self):
        self.player = Player()

    def test_can_create_player(self):
        self.assertIsNotNone(self.player)


if __name__ == '__main__':
    unittest.main()
