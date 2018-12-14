import unittest

from casino.roulette.bet import Bet
from casino.roulette.binbuilder import BinBuilder
from casino.roulette.martingale import Martingale
from casino.roulette.game import Game
from casino.roulette.table import Table
from casino.roulette.wheel import Wheel


class MartingaleTest(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)
        self.the_player = Martingale(self.table, self.wheel)

    def test_martingale_player_exists(self):
        self.assertIsNotNone(self.the_player)
        self.assertEqual(self.the_player.loss_count, 0)
        self.assertEqual(self.the_player.bet_multiplier, 1)

    def test_martingale_player_can_place_a_bet(self):
        self.the_player.place_bets()
        self.assertIn("Bet(1, Black (1:1))", str(self.table.bets))

    def test_martingale_player_stake_is_down_after_placing_a_bet(self):
        self.assertEqual(self.the_player.stake, 0)
        self.the_player.place_bets()
        self.assertEqual(self.the_player.stake, -1)

    def test_martingale_player_stake_is_correct_after_a_loss(self):
        the_bet = Bet(1, self.wheel.get_outcome(Game.BLACK_BET_NAME))
        self.assertEqual(self.the_player.stake, 0)
        self.the_player.place_bets()
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.stake, -1)

    def test_martingale_player_bet_multiplier_correctly_updates(self):
        amount = 1
        the_bet = Bet(amount, self.wheel.get_outcome(Game.BLACK_BET_NAME))
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 2)
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 4)
        self.the_player.win(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 1)

    def test_after_martingale_player_places_bets_rounds_to_go_decreases(self):
        self.assertEqual(self.the_player.rounds_to_go, 0)
        self.the_player.place_bets()
        self.assertEqual(self.the_player.rounds_to_go, -1)


if __name__ == '__main__':
    unittest.main()
