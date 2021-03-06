import unittest

from casino.roulette.bet import Bet
from casino.roulette.binbuilder import BinBuilder
from casino.roulette.game import Game
from casino.roulette.player import Player
from casino.roulette.table import Table
from casino.roulette.wheel import Wheel


class PlayerTest(unittest.TestCase):
    """Test the implementation of the class Player."""

    def setUp(self):
        self.table = Table()
        self.wheel = Wheel()
        BinBuilder().build_bins(self.wheel)
        self.player = Player(self.table, self.wheel)

    def test_can_create_player(self):
        self.assertIsNotNone(self.player)

    def test_player_updates_stake_with_a_win(self):
        bet_amount = 100
        the_bet = Bet(bet_amount, self.wheel.get_outcome(Game.ODD_BET_NAME))
        self.assertEqual(self.player.stake, 0)
        self.player.win(the_bet)
        self.assertEqual(self.player.stake, 200)

    def test_player_stake_does_not_change_with_a_loss(self):
        # amount has already been deducted when placing the bet
        bet_amount = 100
        the_bet = Bet(bet_amount, self.wheel.get_outcome(Game.ODD_BET_NAME))
        self.assertEqual(self.player.stake, 0)
        self.player.lose(the_bet)
        self.assertEqual(self.player.stake, 0)

    def test_can_set_the_player_stake(self):
        expected_stake = 10
        self.player.set_stake(expected_stake)
        self.assertEqual(self.player.stake, expected_stake)

    def test_can_set_the_player_rounds(self):
        expected_rounds = 6
        self.player.set_rounds(expected_rounds)
        self.assertEqual(self.player.rounds_to_go, expected_rounds)

    def test_player_is_playing_if_stake_and_rounds_not_zero(self):
        self.player.set_rounds(1)
        self.player.set_stake(1)
        self.assertTrue(self.player.is_playing())

    def test_player_stops_playing_if_rounds_reach_zero(self):
        self.player.set_rounds(0)
        self.player.set_stake(1)
        self.assertFalse(self.player.is_playing())

    def test_player_stops_playing_if_stake_reaches_zero(self):
        self.player.set_rounds(1)
        self.player.set_stake(0)
        self.assertFalse(self.player.is_playing())

    def test_after_player_places_bets_rounds_to_go_decreases(self):
        self.assertEqual(self.player.rounds_to_go, 0)
        self.player.place_bets()
        self.assertEqual(self.player.rounds_to_go, -1)


if __name__ == '__main__':
    unittest.main()
