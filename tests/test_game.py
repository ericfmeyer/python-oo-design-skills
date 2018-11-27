import unittest

from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.passenger57 import Passenger57
from casino.roulette.table import Table
from casino.roulette.wheel import Wheel


class GameTest(unittest.TestCase):
    """Test the implementation of the class Game."""

    def setUp(self):
        table = Table()
        wheel = Wheel()
        BinBuilder().build_bins(wheel)
        self.game = Game(wheel, table)
        self.player = Passenger57(table, wheel)

    def test_can_create_game(self):
        self.assertIsNotNone(self.game)

    def test_one_cycle(self):
        for i in range(3):
            self.game.cycle(self.player)


if __name__ == '__main__':
    unittest.main()
