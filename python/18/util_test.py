import unittest
import util

class UtilTest(unittest.TestCase):

  def test_eval_no_parens(self):
    self.assertEqual(71, util.eval_no_parens("1 + 2 * 3 + 4 * 5 + 6"))
    self.assertEqual(42, util.eval_no_parens("42"))
    pass

  def test_eval(self):
    self.assertEqual(51, util.eval('1 + (2 * 3) + (4 * (5 + 6))'))
    self.assertEqual(26, util.eval('2 * 3 + (4 * 5)'))
    self.assertEqual(437, util.eval('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    self.assertEqual(12240, util.eval('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
    self.assertEqual(13632, util.eval('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

  def test_eval_no_parens_part_2(self):
    self.assertEqual(231, util.eval_no_parens_part2('1 + 2 * 3 + 4 * 5 + 6'))

if __name__ == '__main__':
    unittest.main()


