import unittest

from casino.roulette.table import Table


class TableTest(unittest.TestCase):
    """Test the implementation of the class Table."""
    def setUp(self):
        self.table = Table()

    def test_can_create_table(self):
        self.assertIsNotNone(self.table)


if __name__ == '__main__':
    unittest.main()
