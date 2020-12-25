from collections import deque
import unittest
import util

class UtilTest(unittest.TestCase):

  def test_play_round(self):
    player1 = deque((9, 2, 6, 3, 1))
    player2 = deque((5, 8, 4, 7, 10))
    util.play_round(player1, player2)
    self.assertEqual((2, 6, 3, 1, 9, 5), tuple(player1))
    self.assertEqual((8, 4, 7, 10), tuple(player2))
    pass

  def test_parse(self):
    player1, player2 = util.parse(open('test_input.txt'))
    self.assertEqual((9, 2, 6, 3, 1), tuple(player1))
    self.assertEqual((5, 8, 4, 7, 10), tuple(player2))

if __name__ == '__main__':
    unittest.main()
