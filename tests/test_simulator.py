import unittest

from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.passenger57 import Passenger57
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
            Passenger57(self.table, self.wheel),
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
        session_results = self.test_simulator.session()
        self.assertTrue(session_results)

    def test_simulator_can_gather_results(self):
        self.test_simulator.gather()
        self.assertTrue(self.test_simulator.durations)
        self.assertTrue(self.test_simulator.maxima)

    def test_simulator_returns_correct_results_given_non_random_spins(self):
        expected_durations = [52, 2, 2, 4, 24, 2, 6, 4, 98, 4, 250, 4, 12, 38,
                              6, 84, 2, 250, 12, 2, 150, 6, 8, 2, 8, 2, 4, 28,
                              2, 20, 6, 20, 6, 2, 26, 82, 2, 2, 4, 2, 2, 14, 38,
                              2, 14, 12, 4, 10, 2, 10]
        expected_maxima = [300, 50, 50, 100, 200, 50, 200, 100, 650, 150, 800,
                           100, 150, 300, 150, 500, 50, 1200, 200, 50, 800, 100,
                           150, 50, 250, 50, 100, 300, 50, 250, 150, 200, 100,
                           50, 250, 450, 50, 50, 100, 50, 50, 250, 400, 50, 200,
                           200, 150, 150, 50, 200]
        self.wheel.rng.seed(1)
        self.test_simulator.gather()
        self.assertEqual(self.test_simulator.durations, expected_durations)
        self.assertEqual(self.test_simulator.maxima, expected_maxima)


if __name__ == '__main__':
    unittest.main()
