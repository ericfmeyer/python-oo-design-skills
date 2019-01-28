import unittest

from casino.roulette.bet import Bet
from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.sevenreds import SevenReds
from casino.roulette.table import Table
from casino.roulette.wheel import Wheel


class SevenRedsTest(unittest.TestCase):
    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)
        self.the_player = SevenReds(self.table, self.wheel)

    def test_sevenreds_player_exists(self):
        self.assertIsNotNone(self.the_player)
        self.assertEqual(self.the_player.reds_to_go, 7)

    def test_sevenreds_correctly_decrements_reds_to_go(self):
        self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        self.assertEqual(self.the_player.reds_to_go, 6)

    def test_sevenreds_correctly_resets_reds_to_go(self):
        self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        self.the_player.winners({self.wheel.get_outcome(Game.BLACK_BET_NAME)})
        self.assertEqual(self.the_player.reds_to_go, 7)

    def test_sevenreds_player_does_not_place_bets_given_no_seven_reds(self):
        for _ in range(6):
            self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        self.the_player.place_bets()
        self.assertNotIn("Bet(1, Black (1:1))", str(self.table.bets))

    def test_sevenreds_player_can_place_bet_after_seven_reds(self):
        for _ in range(7):
            self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        self.the_player.place_bets()
        self.assertIn("Bet(1, Black (1:1))", str(self.table.bets))

    def test_sevenreds_player_stake_is_down_after_placing_a_bet(self):
        for _ in range(7):
            self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        self.assertEqual(self.the_player.stake, 0)
        self.the_player.place_bets()
        self.assertEqual(self.the_player.stake, -1)

    def test_sevenreds_player_stake_is_correct_after_a_loss(self):
        for _ in range(7):
            self.the_player.winners({self.wheel.get_outcome(Game.RED_BET_NAME)})
        the_bet = Bet(1, self.wheel.get_outcome(Game.BLACK_BET_NAME))
        self.assertEqual(self.the_player.stake, 0)
        self.the_player.place_bets()
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.stake, -1)

    def test_sevenreds_player_bet_multiplier_correctly_updates(self):
        amount = 1
        the_bet = Bet(amount, self.wheel.get_outcome(Game.BLACK_BET_NAME))
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 2)
        self.the_player.lose(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 4)
        self.the_player.win(the_bet)
        self.assertEqual(self.the_player.bet_multiplier, 1)


if __name__ == '__main__':
    unittest.main()
