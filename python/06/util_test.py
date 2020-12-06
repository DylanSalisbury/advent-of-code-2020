import unittest
import util

class UtilTest(unittest.TestCase):

  def test_line_to_set(self):
    self.assertEqual({'a', 'b'}, util.line_to_set('ab'))
    self.assertEqual({'a', 'b'}, util.line_to_set('ba'))
    self.assertEqual({'a'}, util.line_to_set('a'))
    pass

  def test_group_to_set(self):
    self.assertEqual({'a', 'b'}, util.group_to_set('ab\nba'))
    self.assertEqual({'a', 'b'}, util.group_to_set('a\nb'))
    self.assertEqual({'a'}, util.group_to_set('a'))
    self.assertEqual({'a'}, util.group_to_set('a\na'))
    self.assertEqual({'a', 'b', 'c'}, util.group_to_set('a\nac\nbc'))
    pass

if __name__ == '__main__':
    unittest.main()


