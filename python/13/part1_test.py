import unittest
import part1

class Part1Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(295, part1.solve('test_input.txt'))
    self.assertEqual(410, part1.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()


