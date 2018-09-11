import unittest

from casino.roulette.bet import Bet
from casino.roulette.game import RouletteGame as RoG
from casino.roulette.outcome import Outcome


class BetTest(unittest.TestCase):
    """Test the implementation of the class Bet."""

    def setUp(self):
        self.black_bet = Bet(10, Outcome(RoG.black_bet_name,
                                         RoG.even_money_bet_odds))
        self.straight_bet = Bet(5, Outcome(
            RoG.straight_bet_name + ' 35', RoG.straight_bet_odds)
                                )

    def test_can_create_bet(self):
        self.assertIsNotNone(self.black_bet)

    def test_win_amount_is_correct_for_black_bet(self):
        expected = 20  # 10 * 1 + 10
        self.assertEqual(expected, self.black_bet.win_amount())

    def test_win_amount_is_correct_for_straight_bet(self):
        expected = 180  # 5 * 35 + 5
        self.assertEqual(expected, self.straight_bet.win_amount())

    def test_lose_amount_is_correct(self):
        self.assertEqual(10, self.black_bet.lose_amount())
        self.assertEqual(5, self.straight_bet.lose_amount())

    def test_string_representation(self):
        self.assertEqual("10 on Black (1:1)", str(self.black_bet))
        self.assertEqual("5 on Number 35 (35:1)", str(self.straight_bet))

    def test_repr(self):
        self.assertEqual("Bet(10, Black (1:1))", repr(self.black_bet))
        self.assertEqual("Bet(5, Number 35 (35:1))", repr(self.straight_bet))


if __name__ == '__main__':
    unittest.main()
