import unittest
import part1

class Part1Test(unittest.TestCase):

  def test_solve(self):
    self.assertEqual(306, part1.solve('test_input.txt'))
    self.assertEqual(35370, part1.solve('input.txt'))

if __name__ == '__main__':
    unittest.main()

