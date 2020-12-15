import unittest
import util

class UtilTest(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(0, util.solve(10, (0, 3, 6)))
    self.assertEqual(1, util.solve(2020, (1, 3, 2)))
    self.assertEqual(10, util.solve(2020, (2, 1, 3)))
    self.assertEqual(27, util.solve(2020, (1, 2, 3)))
    self.assertEqual(78, util.solve(2020, (2, 3, 1)))
    self.assertEqual(438, util.solve(2020, (3, 2, 1)))
    self.assertEqual(1836, util.solve(2020, (3, 1, 2)))

  def test_solve_part2(self):
    inputs = (
      (175594, (0, 3, 6)),
      (2578, (1, 3, 2)),
      (3544142, (2, 1, 3)),
      (261214, (1, 2, 3)),
      (6895259, (2, 3, 1)),
      (18, (3, 2, 1)),
      (362, (3, 1, 2)))

    print('')
    for i in inputs:
      self.assertEqual(i[0], util.solve(30000000, i[1]))
      print('Passed for %s' % str(i[1]))

if __name__ == '__main__':
    unittest.main()


