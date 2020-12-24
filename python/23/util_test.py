import unittest
import util

class UtilTest(unittest.TestCase):

  def test_moves(self):
    self.assertEquals('92658374', util.moves('389125467', 10))
    self.assertEquals('67384529', util.moves('389125467', 100))
    pass

if __name__ == '__main__':
    unittest.main()


