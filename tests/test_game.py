import unittest

from casino.roulette.game import RouletteGame


class GameTest(unittest.TestCase):
    """Test the implementation of the class Game."""

    def setUp(self):
        self.game = RouletteGame()

    def test_can_create_game(self):
        self.assertIsNotNone(self.game)


if __name__ == '__main__':
    unittest.main()
