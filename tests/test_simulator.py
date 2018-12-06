import unittest

from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.player import Player
from casino.roulette.table import Table
from casino.roulette.wheel import Wheel
from casino.simulator.simulator import Simulator


class SimulatorTest(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)
        self.test_simulator = Simulator(
            Game(self.wheel, self.table),
            Player(self.wheel, self.table),
        )

    def test_simulator_can_be_created(self):
        self.assertIsNotNone(self.test_simulator)

    def test_simulator_has_correct_default_values(self):
        self.assertEqual(self.test_simulator.init_duration, 250)
        self.assertEqual(self.test_simulator.init_stake, 100)
        self.assertEqual(self.test_simulator.samples, 50)
        self.assertFalse(self.test_simulator.durations)
        self.assertFalse(self.test_simulator.maxima)

    def test_simulator_session_returns_results(self):
        self.test_simulator.session()
        self.assertTrue(self.test_simulator.durations)
        self.assertTrue(self.test_simulator.maxima)


if __name__ == '__main__':
    unittest.main()
