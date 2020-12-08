import unittest
import util

class UtilTest(unittest.TestCase):

  def test_parse_line(self):
    i = util.parse_line('acc +36')
    self.assertEqual(i[0], 'acc')
    self.assertEqual(i[1], 36)
    i = util.parse_line('acc +36\n')
    self.assertEqual(i[0], 'acc')
    self.assertEqual(i[1], 36)
    i = util.parse_line('acc -36')
    self.assertEqual(i[0], 'acc')
    self.assertEqual(i[1], -36)
    # self.assertEqual(expected, util.func(args))
    pass

if __name__ == '__main__':
    unittest.main()


