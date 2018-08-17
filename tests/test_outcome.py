import unittest

from casino.roulette.outcome import Outcome


class TestOutcome(unittest.TestCase):
    """Tests the implementation of the class Outcome."""

    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Red", 1)
        self.oc3 = Outcome("Split 1-2", 17)

    def test_can_create_outcome(self):
        self.assertIsNotNone(self.oc1)

    def test_same_outcomes_are_equal(self):
        self.assertEqual(self.oc1, self.oc2)

    def test_different_outcomes_are_not_equal(self):
        self.assertNotEqual(self.oc1, self.oc3)

    def test_same_outcomes_have_same_hash(self):
        self.assertEqual(hash(self.oc1), hash(self.oc2))

    def test_different_outcomes_have_different_hash(self):
        self.assertNotEqual(hash(self.oc1), hash(self.oc3))

    def test_outcome_str_representation_is_correct(self):
        self.assertEqual(self.oc1.__str__(), "Red (1:1)")
        self.assertEqual(self.oc3.__str__(), "Split 1-2 (17:1)")

    def test_outcome_repr_is_correct(self):
        self.assertEqual(self.oc1.__repr__(), "Outcome('Red', 1)")
        self.assertEqual(self.oc3.__repr__(), "Outcome('Split 1-2', 17)")

    def test_win_amount_returns_correct_value(self):
        self.assertEqual(self.oc1.win_amount(13), 13)
        self.assertEqual(self.oc3.win_amount(5), 85)


if __name__ == '__main__':
    unittest.main()
