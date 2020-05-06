import unittest
from hangman import Game

class GameTest(unittest.TestCase):
    def setUp(self):
        self.Game = Game("berry")

    def test_done(self):
        self.Game.add_guess('b')
        self.Game.add_guess('e')
        self.Game.add_guess('r')
        self.Game.add_guess('y')
        self.assertTrue(self.Game.done())

    def test_done_incomplete(self):
        self.Game.add_guess('b')
        self.assertFalse(self.Game.done())

    def test_status(self):
        m = self.Game.status()
        for v in m:
            self.assertFalse(v)
        self.Game.add_guess('r')
        m = self.Game.status()
        self.assertTrue(len(m) == 5)
        self.assertFalse(m[0])
        self.assertFalse(m[1])
        self.assertTrue(m[2])
        self.assertTrue(m[3])
        self.assertFalse(m[4])


if __name__ == '__main__':
    unittest.main()
