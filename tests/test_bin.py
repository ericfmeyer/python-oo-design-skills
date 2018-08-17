import unittest

from casino.roulette.bin import Bin
from casino.roulette.outcome import Outcome


class BinTest(unittest.TestCase):
    """Test the implementation of the class Bin."""

    def setUp(self):
        self.oc1 = Outcome("Red", 1)
        self.oc2 = Outcome("Even", 1)
        self.oc3 = Outcome("Split 1-2", 17)
        self.bin1 = Bin([self.oc1])
        self.bin2 = Bin([self.oc1, self.oc2, self.oc3])

    def test_can_create_bin_with_one_outcome(self):
        self.assertIsNotNone(self.bin1)

    def test_bin_with_one_element_has_correct_size(self):
        self.assertEqual(len(self.bin1), 1)

    def test_can_create_bin_with_many_elements(self):
        self.assertIsNotNone(self.bin2)

    def test_bin_with_many_elements_has_correct_size(self):
        self.assertEqual(len(self.bin2), 3)

    def test_bin_has_correct_elements(self):
        self.assertTrue(self.oc1 in self.bin1)
        self.assertTrue(self.oc1 in self.bin2)
        self.assertTrue(self.oc2 in self.bin2)
        self.assertTrue(self.oc3 in self.bin2)


if __name__ == '__main__':
    unittest.main()
