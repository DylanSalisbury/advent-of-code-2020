import unittest
import util

class UtilTest(unittest.TestCase):

  def test_rel_from_str(self):
    self.assertEqual((1, -1), util.rel_from_str('esew'))
    self.assertEqual((0, 0), util.rel_from_str('nwwswee'))
    pass

if __name__ == '__main__':
    unittest.main()


