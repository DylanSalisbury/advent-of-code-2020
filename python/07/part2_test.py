import unittest
import part2

class Part2Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(421550, part2.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


