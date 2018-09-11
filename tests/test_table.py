import unittest

from casino.roulette.bet import Bet
from casino.roulette.outcome import Outcome
from casino.roulette.table import InvalidBet
from casino.roulette.table import Table


class TableTest(unittest.TestCase):
    """Test the implementation of the class Table."""

    def setUp(self):
        self.table = Table()
        self.bet_split = Bet(10, Outcome("Split 1-2", 17))
        self.bet_straight = Bet(5, Outcome("Number 17", 35))
        self.bet_red = Bet(25, Outcome("Red", 1))

    def test_can_create_table(self):
        self.assertIsNotNone(self.table)

    def test_place_bet_adds_bet_to_table(self):
        self.table.place_bet(self.bet_split)
        self.assertEqual(1, len(self.table.bets))

    def test_place_bet_can_add_same_bet(self):
        self.table.place_bet(self.bet_split)
        self.table.place_bet(self.bet_split)
        self.assertEqual(2, len(self.table.bets))
        for elem in self.table:
            self.assertEqual(self.bet_split, elem)

    def test_place_bet_can_different_bets(self):
        self.table.place_bet(self.bet_split)
        self.table.place_bet(self.bet_red)
        self.table.place_bet(self.bet_straight)
        self.assertEqual(self.bet_split, self.table.bets[0])
        self.assertEqual(self.bet_red, self.table.bets[1])
        self.assertEqual(self.bet_straight, self.table.bets[2])

    def test_iter_returns_iterator_on_list_of_bets(self):
        self.table.place_bet(self.bet_split)
        for bet in self.table:
            self.assertIsInstance(bet, Bet)

    def test_string_representation_for_one_bet(self):
        self.table.place_bet(self.bet_split)
        expected = "10 on Split 1-2 (17:1)"
        self.assertEqual(expected, str(self.table))

    def test_string_representation_for_many_bets(self):
        self.table.place_bet(self.bet_split)
        self.table.place_bet(self.bet_red)
        expected = "10 on Split 1-2 (17:1)\n25 on Red (1:1)"
        self.assertEqual(expected, str(self.table))

    def test_representation_for_one_bet(self):
        self.table.place_bet(self.bet_split)
        expected = "Table( Bet(10, Split 1-2 (17:1)) )"
        self.assertEqual(expected, repr(self.table))

    def test_representation_for_many_bets(self):
        self.table.place_bet(self.bet_split)
        self.table.place_bet(self.bet_red)
        expected = "Table( Bet(10, Split 1-2 (17:1)), Bet(25, Red (1:1)) )"
        self.assertEqual(expected, repr(self.table))


# TODO: finish test of is_valid()
class TableIsValidTest(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_is_valid_raises_exception_for_bet_under_min(self):
        under_min_bet = Bet(9, Outcome("Red", 1))
        self.table.place_bet(under_min_bet)
        self.assertRaises(InvalidBet, self.table.is_valid)

    def test_is_valid_raises_exception_for_bet_over_max(self):
        one_bet_over_max = Bet(301, Outcome("Red", 1))
        self.table.place_bet(one_bet_over_max)
        self.assertRaises(InvalidBet, self.table.is_valid)

    def test_is_valid_returns_true_for_minimum_bet(self):
        at_min_bet = Bet(10, Outcome("Red", 1))
        self.table.place_bet(at_min_bet)
        self.assertTrue(self.table.is_valid())

    def test_is_valid_with_bets_exceeding_limit(self):
        bet1 = Bet(291, Outcome("Red", 1))
        bet2 = Bet(10, Outcome("Red", 1))
        self.table.place_bet(bet1)
        self.assertTrue(self.table.is_valid())
        self.table.place_bet(bet2)
        self.assertRaises(InvalidBet, self.table.is_valid)

    def test_is_valid_with_bets_below_limit(self):
        bet1 = Bet(280, Outcome("Red", 1))
        bet2 = Bet(10, Outcome("Red", 1))
        bet3 = Bet(10, Outcome("Red", 1))
        self.table.place_bet(bet1)
        self.assertTrue(self.table.is_valid())
        self.table.place_bet(bet2)
        self.assertTrue(self.table.is_valid())
        self.table.place_bet(bet3)
        self.assertTrue(self.table.is_valid())


if __name__ == '__main__':
    unittest.main()
