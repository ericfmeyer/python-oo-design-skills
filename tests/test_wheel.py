import unittest

from casino.roulette.wheel import Wheel


class WheelTest(unittest.TestCase):
    """Test the implementation of the class Wheel."""
    def setUp(self):
        self.test_wheel = Wheel()

    def test_can_create_wheel(self):
        self.assertIsNotNone(self.test_wheel)


if __name__ == '__main__':
    unittest.main()
